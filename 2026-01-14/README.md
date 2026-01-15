<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Task 1: NetworkingStack Deployment & Task 2: CICD Pipeline with CDK</h3>

---

## 🎯 Objective
Implement and deploy two critical AWS CDK stacks for an ECS CI/CD project:
1. **Task 1**: NetworkingStack - Foundation networking infrastructure
2. **Task 2**: CICD Pipeline - Automated build pipeline with GitLab integration

---

## 💡 Summary / What I built

### Task 1 – NetworkingStack Deployment Report

**Author:** **Sufi Hassan Asim**  
**Date:** **2026-01-14**

#### Overview
The **NetworkingStack** provides foundation networking components for the ECS CI/CD project:
- VPC (10.0.0.0/16) with public/private/database subnets
- Internet Gateway and NAT gateways for routing
- Route tables and security groups
- VPC endpoints for S3, ECR, and CloudWatch (private access)

#### Steps Followed
1. Environment setup
```bash
cd E:\DPL\training-project\cdk-ecs-cicd\cdk
git checkout feature/networking-stack
npm install
```
> Note: Fixed dependency conflicts in `package.json` to align with AWS CDK v2.

2. Stack implementation
- `NetworkingStack` created in `lib/networking-stack.ts`
- Resources defined: VPC, 2 public subnets, 2 private subnets, 2 database subnets, IGW, 2 NAT gateways, route tables, SGs, VPCEndpoints

3. Deployment
```bash
cdk synth
cdk deploy NetworkingStack
```
- Validation: Verified resources in AWS Console under VPC, EC2, and RDS

#### Obstacles & Solutions
- `YOUR_IP/32` placeholder in Bastion SG → replaced with actual public IP `/32`
- Deprecated `cidr` property in `VpcProps` → updated to `ipAddresses` for CDK v2
- npm install conflicts → updated dependencies in `package.json`

#### Key Takeaways
- Followed CDK networking best practices
- Implemented VPCEndpoints for private access
- Achieved subnet isolation with proper routing

**Note:** Changed the template to use **2 private** and **2 public** subnets after PO(s) advised this is best practice. Deleted the old stack and redeployed successfully.

---

### Task 2 – CICD Pipeline with AWS CDK

#### Overview
Task 2 creates an **end-to-end CI/CD pipeline** with the following goals:

1. Connect a GitLab repository (`GTO/cdk-ecs-cicd`) to AWS CodePipeline using **CodeStar Connections**
2. Build frontend and backend code with **AWS CodeBuild**
3. Store build artifacts in an **S3 bucket**
4. Enable future deployment stages (ECS, S3, Lambda, etc.) as needed

#### Architecture

```
GitLab Repository (feature/pipeline branch)
         │
         ▼
   CodeStar Connections
         │
         ▼
   AWS CodePipeline
   ┌─────────────────────┐
   │  Source Stage       │
   │  (GitLabSource)     │
   └─────────────────────┘
         │
         ▼
   ┌─────────────────────┐
   │  Build Stage        │
   │  FrontendBuild      │
   │  BackendBuild       │
   └─────────────────────┘
         │
         ▼
    S3 Artifact Bucket
```

#### Prerequisites
1. AWS Account with admin privileges
2. Node.js v18+ (LTS recommended)
3. AWS CDK installed globally: `npm install -g aws-cdk`
4. AWS CLI configured: `aws configure`
5. GitLab Repository: Group `GTO`, Repo `cdk-ecs-cicd`, Branch `feature/pipeline`

#### Setup Instructions

1. **Clone the repo**:
```bash
git clone <repo-url>
cd cdk-ecs-cicd/cdk
```

2. **Install dependencies**:
```bash
npm install
```

3. **Create CodeStar Connection**:
```bash
aws codestar-connections create-connection --connection-name GTO-GitLab-Connection --provider-type GitLab
```
- Copy the `ConnectionArn` from the output
- Update the pipeline stack with this ARN

#### Pipeline Details
- **Stack Name**: `CicdPipelineStack`
- **Pipeline Name**: `Task2Pipeline`
- **Artifact Bucket**: `PipelineArtifactBucket` (auto-created)
- **Stages**:
  1. **Source**: Pulls from GitLab `feature/pipeline` branch
  2. **Build**:
     - **FrontendBuild**: Uses `buildspec/frontend/buildspec.yml`
     - **BackendBuild**: Uses `buildspec/backend/buildspec.yml`
  3. **Optional Deploy Stage** (can be added later for ECS, S3, etc.)

#### BuildSpec Files
- **Frontend**: `buildspec/frontend/buildspec.yml`
- **Backend**: `buildspec/backend/buildspec.yml`

Each buildspec defines:
- Environment setup
- Install commands
- Build commands
- Artifact output location

Example snippet for frontend:
```yaml
version: 0.2
phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - npm install
  build:
    commands:
      - npm run build
artifacts:
  files:
    - '**/*'
  base-directory: dist
```

#### Deploying the Pipeline

1. Ensure your `bin/cdk.ts` points to the correct stacks:
```typescript
new CicdPipelineStack(app, 'CicdPipelineStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: 'us-east-1' },
});
```

2. Bootstrap CDK environment (first-time only):
```bash
cdk bootstrap aws://<ACCOUNT_ID>/us-east-1
```

3. Deploy the pipeline:
```bash
cdk deploy CicdPipelineStack --app "ts-node bin/cdk.ts" --require-approval never
```

4. Verify pipeline in AWS Console: **CodePipeline → Task2Pipeline**

#### Testing
1. Push code changes to `feature/pipeline` branch in GitLab
2. CodePipeline will trigger automatically
3. Check CodeBuild logs to verify builds
4. Artifacts will appear in the S3 bucket

#### Destroying Resources

To clean up all resources created by this task:
```bash
cdk destroy CicdPipelineStack --app "ts-node bin/cdk.ts" --force
```

Removes:
- CodePipeline
- CodeBuild projects
- Artifact S3 bucket

Optionally delete **CodeStar connection**:
```bash
aws codestar-connections delete-connection --connection-arn <ConnectionArn>
```

---

## 📁 Evidence (images)
Screenshots documenting Task 1 and Task 2 implementation and verification.

![AWS Documentation PDF](./images/00be1f94-b97f-402a-8d6b-43647a2a31d1.pdf)

![Architecture Diagram PDF](./images/0e9d10ad-35c7-4daf-a8e3-505261acf9d8.pdf)

![Configuration Reference PDF](./images/656b4d1a-3dc5-4576-82e0-c48e516cbb95.pdf)

![CDK Stack Documentation PDF](./images/760a479f-d107-4b46-980a-44ba7556b47d.pdf)

![Pipeline Architecture PDF](./images/ccb584a7-0f92-4ee3-85c3-f143914f2671.pdf)

![AWS Cloud Economics Certificate](./images/certificate%20of%20compleation%20aws%20cloud%20echonomics.png)

![AWS Database in Practice Certificate](./images/certificate%20of%20compleation%20aws%20database%20in%20practice.png)

![AWS DynamoDB NoSQL DB Certificate](./images/certificate%20of%20compleation%20aws%20dynamodb%20NoSQL%20DB.png)

![AWS File System in the Cloud Certificate](./images/certificate%20of%20compleation%20aws%20file%20system%20in%20the%20cloud.png)

![AWS Networking Concepts Certificate](./images/certificate%20of%20compleation%20aws%20networking%20concepts.png)

![Database in Practice Lab Completion](./images/DatabasesinPractice%20lab%20compleation.png)

---

## 🔧 Key Design Principles

### NetworkingStack
- **Multi-tier architecture**: Public, private, and database subnets
- **High availability**: Resources spread across multiple AZs
- **Security isolation**: Separate security groups for different tiers
- **Private endpoints**: VPC endpoints for AWS services without internet gateway

### CICD Pipeline
- **GitLab integration**: Native CodeStar Connections support
- **Parallel builds**: Frontend and backend build simultaneously
- **Artifact management**: Centralized S3 bucket for all artifacts
- **Extensible design**: Easy to add deployment stages

---

## 🔭 Next steps / Improvements
- Deploy ECS clusters and services with Task 3
- Implement automated testing in the pipeline
- Add approval gates for production deployments
- Implement infrastructure monitoring with CloudWatch

---

## 📞 Contact
- Email: hassan.u@dplit.com

> Tasks 1 and 2 provide the foundation for an enterprise-grade CI/CD infrastructure on AWS using infrastructure-as-code best practices.
