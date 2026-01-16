<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Task 4: High Availability, Disaster Recovery & Cost Optimization</h3>

---

## 🎯 Objective
Implement a **production-ready, highly available infrastructure** with **disaster recovery capabilities** and **cost optimization strategies** using **AWS CDK**. This task builds upon the previous CI/CD pipeline by adding resilience, monitoring, backup strategies, and cost-efficient resource management.

---

## 💡 Summary / What I built

**Task 4** expands the previous architecture by adding **resilience, monitoring, and cost-efficiency**:

1. **High Availability & Disaster Recovery**
   - Multi-AZ deployment for RDS, ECS, ALB, and NAT Gateways
   - RDS automatic failover and synchronous replication to standby
   - ECS service runs minimum 2 tasks with health checks
   - ALB cross-zone load balancing with connection draining
   - S3 Standard storage with versioning and lifecycle to Glacier
   - CloudFront global caching and automatic failover

2. **Monitoring & Logging**
   - CloudWatch Log Groups for ECS and application logs
   - CloudWatch Alarms for critical metrics
   - Container Insights enabled for ECS cluster
   - Centralized logging with configurable retention

3. **Backup & Recovery**
   - RDS daily automated backups (7-day retention, 5-min point-in-time recovery)
   - AWS Backup for weekly snapshots (30-day retention)
   - S3 versioning with lifecycle to Glacier after 180 days
   - ECR lifecycle policy retains last 10 images
   - Infrastructure code in Git for repeatable deployments

4. **Cost Optimization**
   - Multi-AZ deployment balanced with cost considerations
   - S3 lifecycle policies for automatic archival
   - ECR image cleanup to reduce storage costs
   - CloudFront caching reduces origin requests
   - Auto-scaling ensures resource usage matches demand

---

## 📋 Table of Contents

* [Architecture Overview](#architecture-overview)
* [Implementation Details](#implementation-details)
* [Deployment & Verification](#deployment--verification)
* [Cost Estimation](#cost-estimation)
* [Deployment Checklist](#deployment-checklist)
* [Destroying Resources](#destroying-resources)
* [References](#references)

---

## 🔧 Architecture Overview

```
AWS Multi-AZ Architecture
│
├── VPC (10.0.0.0/16)
│   ├── Public Subnets (2 AZs) - ALB, NAT Gateways
│   ├── Private Subnets (2 AZs) - ECS Tasks
│   └── Isolated Subnets (2 AZs) - RDS Aurora
│
├── Compute Layer
│   ├── ECS Cluster (Container Insights enabled)
│   ├── ECS Service (min 2 tasks, auto-scaling)
│   └── ALB (cross-zone, 300s connection draining)
│
├── Database Layer
│   ├── Aurora PostgreSQL 15.8 (Multi-AZ)
│   ├── Writer Instance (db.t3.medium)
│   ├── Reader Instance (db.t3.medium)
│   └── AWS Backup (weekly snapshots, 30-day retention)
│
├── Storage Layer
│   ├── S3 Frontend Bucket (versioned, Glacier lifecycle)
│   ├── S3 Uploads Bucket (versioned, Glacier lifecycle)
│   ├── S3 CloudFront Logs Bucket
│   └── ECR Repository (lifecycle: keep 10 images)
│
├── CDN Layer
│   └── CloudFront Distribution (global edge network)
│
└── Monitoring
    ├── CloudWatch Logs (7-day retention)
    └── CloudWatch Alarms (CPU, Memory thresholds)
```

---

## ✅ Prerequisites

1. **AWS Account** with admin privileges
2. **Node.js** v18+ (LTS recommended)
3. **AWS CDK** installed globally:
```bash
npm install -g aws-cdk
```

4. **AWS CLI** configured:
```bash
aws configure
```

5. **IAM Permissions** for:
   - VPC, Subnets, NAT Gateways, Internet Gateway
   - RDS Aurora, AWS Backup
   - ECS, ECR, ALB
   - S3, CloudFront
   - CloudWatch Logs and Alarms

---

## 🚀 Setup Instructions

### Step 1: Clone the repository
```bash
git clone <repo-url>
cd cdk-ecs-cicd/cdk
git checkout feature/ha-dr-cost
```

### Step 2: Install dependencies
```bash
npm install
```

### Step 3: Configure AWS credentials
```bash
aws configure
```
Provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-east-1)
- Default output format (json)

### Step 4: Bootstrap CDK (first-time only)
```bash
cdk bootstrap aws://<ACCOUNT_ID>/us-east-1
```

---

## 🛠 Implementation Details

### 1. Networking & HA Design

**VPC Configuration**
- CIDR: 10.0.0.0/16
- 2 Public Subnets (10.0.1.0/24, 10.0.2.0/24) across 2 AZs
- 2 Private Subnets (10.0.10.0/24, 10.0.11.0/24) across 2 AZs
- 2 Isolated Subnets (10.0.20.0/28, 10.0.21.0/28) across 2 AZs
- 2 NAT Gateways for high availability
- Internet Gateway for public subnet access

**Security Groups**
- ALB SG: Inbound 80 from 0.0.0.0/0
- ECS SG: Inbound from ALB SG
- RDS SG: Inbound 5432 from ECS SG

### 2. RDS Aurora PostgreSQL - Multi-AZ

**Configuration**
- Engine: Aurora PostgreSQL 15.8
- Writer Instance: db.t3.medium
- Reader Instance: db.t3.medium (automatic failover)
- Storage: Encrypted with AWS managed keys
- Backup Window: 03:00-04:00 UTC
- Automated Backups: 7-day retention
- Point-in-time Recovery: 5-minute granularity

**AWS Backup Integration**
- Weekly snapshots every Sunday at 02:00 UTC
- Snapshot retention: 30 days
- Backup vault with encryption

### 3. ECS Backend & ALB

**ECS Cluster**
- Container Insights enabled for monitoring
- Fargate launch type

**Application Load Balancer**
- Internet-facing
- Cross-zone load balancing enabled
- Target group with health checks:
  - Interval: 30 seconds
  - Timeout: 5 seconds
  - Healthy threshold: 2
  - Unhealthy threshold: 3
- Connection draining: 300 seconds

### 4. Frontend & CloudFront

**S3 Buckets**
- Frontend Bucket: Versioned, Glacier lifecycle after 180 days
- Uploads Bucket: Versioned, Glacier lifecycle after 180 days
- CloudFront Logs Bucket: Object ownership configured for ACL access

**CloudFront Distribution**
- HTTPS redirect enabled
- Logging enabled
- Global edge network for low latency
- Default root object: index.html

### 5. Container Registry

**ECR Repository**
- Image scanning on push enabled
- Lifecycle policy: Keep last 10 images
- Automatic cleanup of old images

### 6. Monitoring & Logging

**CloudWatch Configuration**
- Log Group: /aws/ecs/ha-dr-stack
- Retention: 7 days
- Container Insights: Enabled

**CloudWatch Alarms**
- High CPU Alarm: Threshold 80%
- Evaluation periods: 1
- Metric: ECS cluster CPU utilization

---

## 🎯 Deploying the Stack

### Step 1: Synthesize CloudFormation template
```bash
cdk synth HaDrCostStack
```
This generates the CloudFormation template in `cdk.out/` directory.

### Step 2: Deploy the stack
```bash
cdk deploy HaDrCostStack --require-approval never
```

**Options**:
- `--profile <profile-name>`: Use specific AWS CLI profile
- `--region <region>`: Deploy to specific region
- `--require-approval always`: Require approval before deployment

### Step 3: Verify deployment
```bash
# Check CloudFormation stack status
aws cloudformation describe-stacks --stack-name HaDrCostStack

# View stack outputs
aws cloudformation describe-stacks --stack-name HaDrCostStack --query "Stacks[0].Outputs"
```

---

## 🧪 Deployment & Verification

### Verification Steps

**1. Verify VPC Resources**
```cmd
aws ec2 describe-vpcs --filters "Name=tag:Name,Values=HaDrCostStack/HaDrVpc"
aws ec2 describe-nat-gateways --filter "Name=state,Values=available"
```

**2. Verify RDS Cluster**
```cmd
aws rds describe-db-clusters --db-cluster-identifier hadrcoststack-hadrrds
aws rds describe-db-instances --filters "Name=db-cluster-id,Values=hadrcoststack-hadrrds"
```

**3. Verify ECS Cluster**
```cmd
aws ecs describe-clusters --clusters HaDrCostStack-HaDrCluster
aws ecs list-services --cluster HaDrCostStack-HaDrCluster
```

**4. Verify S3 Buckets**
```cmd
aws s3 ls | findstr hadrcoststack
```

**5. Verify CloudFront Distribution**
```cmd
aws cloudfront list-distributions --query "DistributionList.Items[?Comment==''].DomainName"
```

**6. Verify ECR Repository**
```cmd
aws ecr describe-repositories --repository-names hadrcoststack-apprepository
```

**7. Verify AWS Backup**
```cmd
aws backup list-backup-plans
aws backup list-backup-selections --backup-plan-id <plan-id>
```

---

## 💰 Cost Estimation

**Estimated Monthly Costs (Production – us-east-1)**

| Service | Configuration | Unit Cost | Estimated Monthly Cost (USD) |
|---------|--------------|-----------|------------------------------|
| ECS Fargate | 2 tasks, 0.5 vCPU, 1 GB RAM | $0.0126/vCPU-h + $0.0016/GB-h | $17 |
| RDS Aurora PostgreSQL | db.t3.medium Multi-AZ (2 instances) | $0.068/hr × 2 instances × 730 hrs | $99 |
| ALB | 1 ALB, 2 LCUs | $0.0225/hr + $0.008/LCU-hr | $33 |
| S3 Standard | 100 GB + 10k requests | $0.023/GB + $0.005 per 1k requests | $3 |
| CloudFront | 1 TB data transfer | $0.085/GB | $85 |
| NAT Gateway | 2 AZs | $0.045/hr × 2 × 730 hrs + data | $66 |
| Route 53 | 1 Hosted Zone | $0.50/month | $0.50 |
| CloudWatch Logs | 10 GB | $0.50/GB ingestion + $0.03/GB storage | $5.30 |
| ECR | 10 GB storage | $0.10/GB | $1 |
| AWS Backup | 50 GB backup storage | $0.05/GB | $2.50 |
| **Total Estimated Monthly Cost** | | | **~$312** |

**Cost Optimization Opportunities**
- Use Fargate Spot for dev/staging (70% savings)
- RDS Reserved Instances for production (up to 60% savings)
- S3 Intelligent-Tiering for automatic cost optimization
- Scheduled scaling for non-production environments
- VPC endpoints to reduce NAT Gateway data transfer

---

## ✅ Deployment Checklist

### Phase 1: Network Foundation
- [x] VPC with CIDR 10.0.0.0/16, DNS hostnames/resolution enabled
- [x] Deploy subnets: 2 public, 2 private, 2 isolated across different AZs
- [x] Internet Gateway and 2 NAT Gateways configured
- [x] Route tables configured for public, private, and isolated subnets
- [x] Security groups for ALB, ECS, RDS with least-privilege rules

### Phase 2: Database & Backup
- [x] RDS Aurora PostgreSQL 15.8 with Multi-AZ enabled
- [x] Writer and reader instances deployed (db.t3.medium)
- [x] Automated backups configured (7-day retention)
- [x] AWS Backup plan created (weekly snapshots, 30-day retention)
- [x] Database credentials stored in Secrets Manager

### Phase 3: Compute & Load Balancing
- [x] ECS Cluster created with Container Insights enabled
- [x] ECR repository with lifecycle policy (keep 10 images)
- [x] ALB deployed with cross-zone load balancing
- [x] Target group configured with health checks
- [x] Connection draining set to 300 seconds

### Phase 4: Storage & CDN
- [x] S3 buckets created with encryption and versioning
- [x] S3 lifecycle rules configured (Glacier after 180 days)
- [x] CloudFront distribution deployed with logging
- [x] CloudFront log bucket with proper ACL configuration

### Phase 5: Monitoring & Logging
- [x] CloudWatch Log Groups configured (7-day retention)
- [x] CloudWatch alarms for CPU utilization (80% threshold)
- [x] Container Insights enabled for ECS monitoring

### Phase 6: Validation & Documentation
- [x] All resources verified in AWS Console
- [x] Stack outputs documented (ALB DNS, CloudFront URL, ECR URI, RDS endpoint)
- [x] Cost estimation completed and documented
- [x] Deployment checklist created
- [x] README documentation updated

---

## 🧹 Destroying Resources

To clean up all resources created by this task:

```bash
cdk destroy HaDrCostStack --force
```

This removes:
- **VPC**: All subnets, NAT Gateways, Internet Gateway, route tables
- **RDS Aurora**: Database cluster, writer/reader instances
- **ECS**: Cluster, services, task definitions
- **ALB**: Load balancer, target groups, listeners
- **S3 Buckets**: Frontend, uploads, CloudFront logs (with all contents)
- **CloudFront**: Distribution
- **ECR**: Repository and all images
- **CloudWatch**: Log groups and alarms
- **AWS Backup**: Backup plans and selections
- **IAM Roles & Policies**: Service roles

> **Warning**: Destroying the stack will delete all data including RDS databases, S3 buckets, and backup snapshots. Export any important data before proceeding.

---

## 📚 References

* [AWS VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/)
* [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/)
* [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/)
* [Amazon ECS Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
* [Application Load Balancer Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/)
* [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/cloudfront/)
* [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/)
* [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

---

## 🔭 Next Steps / Improvements

1. **Auto-Scaling Policies**: Implement target tracking scaling for ECS tasks
2. **Multi-Region DR**: Add cross-region replication for S3 and RDS
3. **WAF Integration**: Add AWS WAF rules to CloudFront and ALB
4. **Secrets Rotation**: Implement automatic rotation for RDS credentials
5. **Cost Anomaly Detection**: Enable AWS Cost Anomaly Detection
6. **Enhanced Monitoring**: Add custom CloudWatch metrics and dashboards
7. **Disaster Recovery Testing**: Automate DR drills and failover testing

---

## 📞 Contact

- Email: hassan.u@dplit.com

> Task 4 provides a production-ready, highly available infrastructure with comprehensive disaster recovery and cost optimization strategies using AWS CDK best practices.
