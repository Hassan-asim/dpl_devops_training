<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Private EC2 with SSM (CloudFormation)</h3>

---

## 🎯 Objective
Create a fully private EC2 instance (no public IP, no Internet Gateway/NAT) that can be accessed securely from a laptop using AWS Systems Manager (SSM). Automate the entire setup using CloudFormation and verify access and privacy.

---

## 💡 Summary / What I built
- CloudFormation template that deploys:
  - VPC (10.0.0.0/16) and a Private Subnet (10.0.1.0/24)
  - Route table and association for the private subnet
  - VPC Interface Endpoints for **ssm**, **ssmmessages**, and **ec2messages**
  - Security Groups: one for the EC2 instance (no inbound, all outbound) and one for endpoints (allow TCP 443 from EC2 SG)
  - IAM Role & Instance Profile attached to the EC2 (AmazonSSMManagedInstanceCore)
  - EC2 instance (Amazon Linux 2023, t2.micro) launched without a public IP and DependsOn endpoints

---

## 🔧 Key Design Principles
- **Private-only:** EC2 has no public IP and the subnet does not auto-assign public IPs (MapPublicIpOnLaunch: false).
- **SSM without Internet:** VPC interface endpoints allow SSM communication entirely inside AWS (no IGW/NAT required).
- **Tight Security:** EC2 SG blocks inbound traffic; endpoint SG allows only HTTPS from EC2 SG.
- **IAM for SSM:** EC2 role uses **AmazonSSMManagedInstanceCore** so the instance can register and communicate with SSM.
- **CloudFormation Ready:** Template ensures deterministic creation order (EC2 DependsOn endpoints) so SSM agent can register immediately.

---

## 📋 How it works (flow)
Your Laptop (AWS CLI / SSM) → AWS Systems Manager Service → VPC Endpoints (SSM/SSMMessages/EC2Messages) → Private EC2 (10.0.1.x)

All access is auditable and stays inside the AWS network; no public IPs involved.

---

## ✅ Verification Steps I performed
- Confirmed stack creation in the console (see screenshot).
- Verified EC2 is in the private subnet and has no public IP (`private instence details confermation on the management console.png`).
- Confirmed SSM agent registered using `aws ssm describe-instance-information` and started a session using `aws ssm start-session` (screenshot: `successfully created the private ec2 machine and  access it using teh ssm session .png`).
- Verified the instance is private via route/IP checks inside the SSM session (screenshot: `varifing that teh machine is private using teh ip routes matric bu accessing it in the local mechine via the ssm session pf teh private mechine .png`).

---

## 📁 Evidence (images)
Below are the embedded screenshots from the `images/` folder shown in chronological order (setup → deploy → verify). Click any image to open full size.

![AWS CLI version check](./images/aws%20cli%20version%20cheack%20using%20cmd%20on%20my%20local%20mechine.png)

![AWS credentials (aws configure)](./images/adding%20aws%20creindintials%20using%20aws%20configuration%20.png)

![SSM plugin installed on Windows](./images/installing%20the%20ssm%20plugin%20on%20windows%20.png)

![Stack creation in progress (console)](./images/stack%20creation%20in%20progress%20varification%20in%20the%20management%20consol%20.png)

![CloudFormation summary / EC2 private subnet](./images/creating%20an%20EC2%20machine%20with%20only%20a%20private%20subnet%20using%20%20cloud%20formation%20no%20public%20subnet%20no%20internet%20gateway%20.png)

![EC2 private instance details (console)](./images/private%20instence%20details%20confermation%20on%20the%20management%20console.png)

![SSM start-session success](./images/successfully%20created%20the%20private%20ec2%20machine%20and%20%20access%20it%20using%20teh%20ssm%20session%20.png)

![Private instance route check (inside SSM)](./images/varifing%20that%20teh%20machine%20is%20private%20using%20teh%20ip%20routes%20matric%20bu%20accessing%20it%20in%20the%20local%20mechine%20via%20the%20ssm%20session%20pf%20teh%20private%20mechine%20.png)

---

## 🔭 Next steps / Improvements
- Apply least-privilege IAM policies for the automation role.
- Add CloudWatch log forwarding or S3 lifecycle for collected logs.
- Add automation to run periodic SSM document to snapshot logs/configuration.

---

## 🧾 CloudFormation template (core resources)
Below is a compact, ready-to-read CloudFormation YAML snippet that implements the private-only EC2 + SSM VPC endpoints described above. Use this as a reference or paste into a `template.yaml` file and deploy with `aws cloudformation deploy --stack-name private-ec2-ssm --template-file template.yaml --capabilities CAPABILITY_NAMED_IAM`.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Private EC2 with SSM access via VPC Interface Endpoints (ssm, ssmmessages, ec2messages)
Parameters:
  VpcCidr:
    Type: String
    Default: 10.0.0.0/16
  PrivateSubnetCidr:
    Type: String
    Default: 10.0.1.0/24
  InstanceType:
    Type: String
    Default: t2.micro
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCidr
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Name
          Value: private-vpc

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PrivateSubnetCidr
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: private-subnet

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC

  PrivateSubnetRouteAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet
      RouteTableId: !Ref PrivateRouteTable

  EC2SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Private EC2 SG - no inbound, all outbound
      VpcId: !Ref VPC
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0

  EndpointSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Endpoint SG - allow HTTPS from EC2 SG
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          SourceSecurityGroupId: !Ref EC2SecurityGroup

  EC2SSMRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore

  EC2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Roles:
        - !Ref EC2SSMRole

  SSMMessagesEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref VPC
      ServiceName: !Sub com.amazonaws.${AWS::Region}.ssmmessages
      VpcEndpointType: Interface
      SecurityGroupIds:
        - !Ref EndpointSecurityGroup
      SubnetIds:
        - !Ref PrivateSubnet

  SSMEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref VPC
      ServiceName: !Sub com.amazonaws.${AWS::Region}.ssm
      VpcEndpointType: Interface
      SecurityGroupIds:
        - !Ref EndpointSecurityGroup
      SubnetIds:
        - !Ref PrivateSubnet

  EC2MessagesEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref VPC
      ServiceName: !Sub com.amazonaws.${AWS::Region}.ec2messages
      VpcEndpointType: Interface
      SecurityGroupIds:
        - !Ref EndpointSecurityGroup
      SubnetIds:
        - !Ref PrivateSubnet

  PrivateEC2:
    Type: AWS::EC2::Instance
    DependsOn:
      - SSMEndpoint
      - SSMMessagesEndpoint
      - EC2MessagesEndpoint
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: ami-0de53d8956e8dcf80 # Replace with latest Amazon Linux 2023 AMI in your region
      NetworkInterfaces:
        - DeviceIndex: 0
          SubnetId: !Ref PrivateSubnet
          AssociatePublicIpAddress: false
          GroupSet:
            - !Ref EC2SecurityGroup
      IamInstanceProfile: !Ref EC2InstanceProfile
      Tags:
        - Key: Name
          Value: private-ec2

Outputs:
  InstanceId:
    Value: !Ref PrivateEC2
    Export:
      Name: PrivateEC2InstanceId
```

> Note: Replace the sample `ImageId` with the correct Amazon Linux 2023 AMI for your region or use an SSM parameter (e.g., `/aws/service/ami-amazon-linux-latest/...`) to always select the current image.

---

## 🔁 Deployed both ways: CloudFormation + Management Console
- **CloudFormation:** I deployed the template above to create all resources in one step and verified SSM registration and sessions immediately after stack completion.
- **Management Console:** For clarity and learning, I also recreated the same resources via the AWS Console (VPC, subnet, endpoints, role, EC2) to confirm the exact sequence and surface any console-specific checks (subnet settings, endpoint subnets, SG linkages).

Both approaches produced the same result: a private EC2 accessible only via SSM.

---

## ✅ Verification & Common CLI commands
- aws ssm describe-instance-information
- aws ssm start-session --target <instance-id>
- aws ec2 describe-instances --instance-ids <instance-id> --query 'Reservations[].Instances[].[PrivateIpAddress,PublicIpAddress]'

---

Made by Sufi Hassan Asim — 2026-01-12
