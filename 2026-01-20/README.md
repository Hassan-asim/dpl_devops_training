<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Task 5: Full-Stack Cloud Architecture Implementation</h3>

---

## 🎯 Objective
Design and implement a **production-ready, cloud-native three-tier architecture** featuring **React frontend**, **NestJS backend**, and **PostgreSQL database** with comprehensive **CI/CD pipeline**, **high availability**, **security**, and **monitoring** using **AWS CDK**.

---

## 💡 Summary / What I built

**Task 5** implements a complete **AWS Cloud Architecture Specification** with the following components:

1. **Frontend Infrastructure**
   - React SPA hosted on S3 with CloudFront CDN distribution
   - Custom domain with SSL certificate via ACM
   - Optimized caching and global edge network delivery

2. **Backend Services**
   - NestJS API on ECS Fargate with Application Load Balancer
   - Auto-scaling configuration (2-10 tasks) with health checks
   - Container registry with ECR and lifecycle policies

3. **Database Layer**
   - RDS PostgreSQL Multi-AZ with automated backups
   - Secure database access via Bastion host
   - Point-in-time recovery and enhanced monitoring

4. **CI/CD Pipeline**
   - GitLab (on-premise) integration with AWS CodeBuild
   - Automated frontend deployment to S3/CloudFront
   - Backend containerization and ECS deployment

5. **Security & Monitoring**
   - Comprehensive IAM roles and security groups
   - Secrets management with AWS Secrets Manager
   - CloudWatch logging, metrics, and alarms
   - X-Ray distributed tracing

---

## 📋 Table of Contents

* [Architecture Overview](#architecture-overview)
* [Infrastructure Components](#infrastructure-components)
* [Implementation Progress](#implementation-progress)
* [Security Implementation](#security-implementation)
* [Monitoring & Logging](#monitoring--logging)
* [CI/CD Pipeline](#cicd-pipeline)
* [Cost Optimization](#cost-optimization)
* [Deployment Checklist](#deployment-checklist)
* [Evidence & Screenshots](#evidence--screenshots)
* [Next Steps](#next-steps)

---

## 🔧 Architecture Overview

```
AWS Cloud-Native Three-Tier Architecture
│
├── Frontend Tier (S3 + CloudFront)
│   ├── React SPA on S3 (versioned, encrypted)
│   ├── CloudFront Distribution (global CDN)
│   ├── Route 53 (custom domain)
│   └── ACM Certificate (SSL/TLS)
│
├── Application Tier (ECS + ALB)
│   ├── Application Load Balancer (Multi-AZ)
│   ├── ECS Fargate Cluster (Container Insights)
│   ├── NestJS API (2-10 tasks, auto-scaling)
│   └── ECR Repository (image lifecycle)
│
├── Database Tier (RDS + Bastion)
│   ├── RDS PostgreSQL Multi-AZ (encrypted)
│   ├── Automated Backups (7-day retention)
│   ├── Bastion Host (secure access)
│   └── Database Subnet Group (isolated)
│
├── Storage Layer
│   ├── S3 User Uploads (encrypted, lifecycle)
│   └── S3 Logs (CloudFront, ALB access logs)
│
├── CI/CD Pipeline
│   ├── GitLab (on-premise source)
│   ├── CodeBuild (frontend + backend)
│   ├── ECR (container registry)
│   └── Automated deployments
│
└── Monitoring & Security
    ├── CloudWatch (logs, metrics, alarms)
    ├── X-Ray (distributed tracing)
    ├── Secrets Manager (credentials)
    └── IAM (roles, policies)
```

---

## 🛠 Infrastructure Components

### 1. Networking Foundation
**VPC Configuration**
- CIDR Block: 10.0.0.0/16 with DNS hostnames enabled
- Public Subnets (2 AZs): 10.0.1.0/24, 10.0.2.0/24 (ALB, Bastion, NAT)
- Private Subnets (2 AZs): 10.0.10.0/24, 10.0.11.0/24 (ECS tasks)
- DB Subnets (2 AZs): 10.0.20.0/24, 10.0.21.0/24 (RDS instances)
- Internet Gateway, NAT Gateways (2 for HA)
- VPC Endpoints: S3 Gateway, ECR/CloudWatch Interface

**Security Groups**
- ALB SG: Inbound 443/80 from 0.0.0.0/0 → Outbound 3000 to ECS SG
- ECS SG: Inbound 3000 from ALB SG → Outbound 5432 to RDS SG, 443 to S3
- RDS SG: Inbound 5432 from ECS SG and Bastion SG
- Bastion SG: Inbound 22 from specific IPs → Outbound 5432 to RDS SG

### 2. Frontend Infrastructure (S3 + CloudFront)
**S3 Configuration**
- Static website hosting with versioning enabled
- SSE-S3 encryption, private bucket with CloudFront OAI
- Lifecycle policies for cost optimization

**CloudFront Distribution**
- HTTP/2 + HTTP/3 support, TLSv1.2+ security policy
- Cache TTL: 86400s, error page redirect to /index.html for SPA routing
- Access logging enabled to dedicated S3 bucket

**DNS & SSL**
- Route 53 A record (alias) pointing to CloudFront
- ACM Certificate in us-east-1 region with DNS validation

### 3. Backend Infrastructure (ECS + ALB)
**Application Load Balancer**
- Internet-facing, deployed across 2+ AZs
- Health check endpoint: /health (30s interval)
- SSL termination with ACM certificate
- Access logs stored in S3

**ECS Configuration**
- Fargate launch type with Container Insights enabled
- Task Definition: 0.5-1 vCPU, 1-2GB RAM, awsvpc networking
- Container image from ECR, port 3000 exposed
- CloudWatch logs integration, environment variables from Secrets Manager

**ECS Service**
- Desired count: 2 tasks minimum
- Rolling update deployment
- Target tracking auto-scaling (CPU 70%, Memory 70%)
- Scaling range: min 2, max 10 tasks

### 4. Database Layer (RDS PostgreSQL)
**RDS Configuration**
- Engine: PostgreSQL 15.x/16.x
- Instance class: db.t4g.medium (prod) / db.t4g.small (dev)
- Storage: gp3 SSD, 100GB with auto-scaling to 500GB
- Encryption: AWS KMS managed keys

**High Availability**
- Multi-AZ deployment in private subnets across 2 AZs
- Automated daily backups with 7-day retention
- Point-in-time recovery enabled (5-minute granularity)
- Enhanced monitoring with Performance Insights

**Database Access**
- Bastion host (EC2 t3.micro) in public subnet with Elastic IP
- SSH key pair authentication with restricted security group
- SSH tunneling support: `ssh -i key.pem -L 5432:rds-endpoint:5432 ec2-user@bastion-ip -N`
- AWS SSM Session Manager integration

### 5. Storage & File Management
**S3 User Uploads**
- Private bucket with IAM access from ECS
- SSE-KMS encryption with versioning enabled
- Lifecycle policies: S3 IA after 90 days, Glacier after 180 days
- Access logging enabled for audit trails

---

## 🔐 Security Implementation

### IAM Roles & Policies
- **ECS Task Role**: S3 read/write (uploads), Secrets Manager read, CloudWatch Logs write
- **ECS Execution Role**: ECR pull, CloudWatch Logs write, Secrets Manager read
- **CodeBuild Role**: S3 write, ECR push, ECS update-service, CloudFront invalidation
- **Bastion Role**: SSM Session Manager, CloudWatch Logs write

### Secrets Management
- Database credentials, API keys, JWT secrets in AWS Secrets Manager
- Automated credential rotation (30-day cycle for RDS passwords)
- All secrets encrypted with AWS KMS customer-managed keys
- Non-sensitive configuration in SSM Parameter Store

### Encryption Strategy
- **In Transit**: TLS 1.2+ on CloudFront, ALB, RDS connections
- **At Rest**: RDS (KMS), S3 (SSE-KMS), EBS volumes (KMS), ECR images (AES-256)
- **Secrets**: Secrets Manager and SSM Parameter Store with KMS encryption

---

## 📊 Monitoring & Logging

### CloudWatch Configuration
**Log Groups**
- /aws/ecs/nestjs-app (application logs)
- /aws/codebuild/* (build logs)
- /aws/rds/postgresql (database logs)
- VPC Flow Logs (network monitoring)

**Retention Policies**
- Production: 30 days
- Development/Staging: 7 days

**Metrics & Alarms**
- ECS: CPU/Memory utilization monitoring
- ALB: Response time, request count, 4xx/5xx errors
- RDS: CPU, connections, latency monitoring
- Custom alarms: High CPU (>80%), High Memory (>80%), ALB 5xx errors (>10/5min)

### Distributed Tracing
- X-Ray tracing enabled on NestJS application
- 5% sampling rate for performance optimization
- Custom CloudWatch dashboard for real-time monitoring

---

## 🚀 CI/CD Pipeline

### Pipeline Components
**GitLab Integration (On-Premise)**
- Source code repository with webhook integration
- Automated triggers on push/merge to main branch

**CodeBuild Projects**
- **Frontend Build**: React app compilation, S3 upload, CloudFront invalidation
- **Backend Build**: Docker image creation, ECR push, ECS service update

### Build Specifications

**Frontend Buildspec**
```yaml
phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - npm ci
  build:
    commands:
      - npm run build
  post_build:
    commands:
      - aws s3 sync build/ s3://$S3_BUCKET --delete
      - aws cloudfront create-invalidation --distribution-id $CF_DIST --paths "/*"
```

**Backend Buildspec**
```yaml
phases:
  pre_build:
    commands:
      - aws ecr get-login-password | docker login --username AWS --password-stdin $ECR
      - IMAGE_TAG=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
  build:
    commands:
      - docker build -t $ECR/$REPO:$IMAGE_TAG .
      - docker tag $ECR/$REPO:$IMAGE_TAG $ECR/$REPO:latest
  post_build:
    commands:
      - docker push $ECR/$REPO:$IMAGE_TAG && docker push $ECR/$REPO:latest
      - aws ecs update-service --cluster $CLUSTER --service $SERVICE --force-new-deployment
```

---

## 💰 Cost Optimization

### Estimated Monthly Costs (Production - us-east-1)

| Service | Configuration | Estimated Cost (USD) |
|---------|--------------|---------------------|
| ECS Fargate | 2 tasks, 0.5 vCPU, 1GB | $17 |
| RDS PostgreSQL | db.t4g.nano Multi-AZ | $25 |
| Application Load Balancer | 1 ALB, standard usage | $18 |
| S3 Storage | 100 GB + requests | $3 |
| CloudFront | 1 TB data transfer | $85 |
| NAT Gateway | 2 AZs | $66 |
| Route 53 | Hosted Zone | $0.50 |
| CloudWatch Logs | 10 GB | $5.30 |
| ECR + Secrets Manager | Standard usage | $2 |
| **Total Estimated Monthly Cost** | | **~$222** |

### Cost Optimization Strategies
- Fargate Spot for dev/staging environments (70% savings)
- RDS Reserved Instances for production (up to 70% savings)
- S3 Intelligent-Tiering for automatic optimization
- Scheduled scaling for non-production environments
- VPC endpoints to reduce NAT Gateway charges

---

## ✅ Deployment Checklist

### Phase 1: Network Foundation ✅
- [x] VPC with CIDR 10.0.0.0/16, DNS hostnames/resolution enabled
- [x] Deploy subnets: 2 public, 2 private, 2 database across AZs
- [x] Internet Gateway, NAT Gateways, route tables configured
- [x] Security groups for ALB, ECS, RDS, Bastion with least-privilege
- [x] VPC endpoints for S3 (gateway) and ECR/CloudWatch (interface)

### Phase 2: Database & Access ✅
- [x] RDS subnet group, PostgreSQL Multi-AZ deployment
- [x] Database credentials in Secrets Manager with auto-rotation
- [x] Bastion host (t3.micro) in public subnet with Elastic IP
- [x] Database connectivity testing via SSH tunnel

### Phase 3: Backend Services ✅
- [x] ECR repository with lifecycle policy
- [x] ECS cluster with Container Insights enabled
- [x] Task definition with proper resource allocation
- [x] ALB with target group and health checks
- [x] ECS service with auto-scaling policies

### Phase 4: Frontend & DNS 🔄
- [x] S3 buckets with encryption and versioning
- [x] ACM certificate for custom domain (us-east-1)
- [x] CloudFront distribution with S3 origin
- [ ] Route 53 configuration (pending domain setup)
- [ ] Frontend build and deployment testing

### Phase 5: CI/CD Pipeline 🔄
- [x] CodeBuild projects (frontend + backend) with IAM roles
- [x] Buildspec files for automated deployment
- [ ] GitLab webhook configuration
- [ ] End-to-end pipeline testing

### Phase 6: Monitoring & Finalization 🔄
- [x] CloudWatch Log Groups with retention policies
- [x] CloudWatch alarms for critical metrics
- [ ] CloudWatch dashboard creation
- [ ] X-Ray tracing implementation
- [ ] Load testing and security scanning

---

## 🖼️ Evidence & Screenshots

### Database Connection Verification
**Successful database connection with 200 status:**

![Database Connection](./images/database%20connesvtion%20200%20status%20with%20display%20the%20users%20.png)

### Frontend Implementation
**CI/CD pipeline architecture frontend:**

![Frontend Architecture](./images/frontend%20of%20teh%20cicd%20pipelind%20architecture%20task%20.png)

### Project Implementation Progress
**Implementation checklist and progress:**

![Implementation Checklist](./images/project%20impolementation%20cheacklist%20.png)

---

## 🔭 Next Steps

### Immediate Tasks
1. **Complete Frontend Deployment**: Finalize S3/CloudFront configuration
2. **GitLab Integration**: Set up webhooks and test CI/CD pipeline
3. **Domain Configuration**: Complete Route 53 and SSL setup
4. **Load Testing**: Validate auto-scaling and performance
5. **Security Review**: Conduct security assessment and penetration testing

### Future Enhancements
1. **Multi-Region DR**: Cross-region replication for disaster recovery
2. **WAF Integration**: Web Application Firewall for enhanced security
3. **Container Optimization**: Implement multi-stage Docker builds
4. **Advanced Monitoring**: Custom metrics and distributed tracing
5. **Cost Optimization**: Reserved instances and Spot integration

---

## 📚 References

* [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
* [Amazon ECS Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
* [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
* [NestJS Documentation](https://nestjs.com/)
* [React Deployment Guide](https://create-react-app.dev/docs/deployment/)
* [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/)

---

## 📞 Contact

- Email: hassan.u@dplit.com

> Task 5 represents a comprehensive cloud-native architecture implementation, demonstrating production-ready infrastructure with modern DevOps practices and AWS best practices.

Made by Sufi Hassan Asim — 2026-01-20