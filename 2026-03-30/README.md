<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • ECS Troubleshooting Course Completion, EC2 Automation Planning & Multi-Project Support</h3>

---

## 🎯 Objective Recap
- Complete ECS troubleshooting course and practice commands on Nova Via project.
- Complete AWS Cloud Quest Cloud Practitioner first assignment.
- Recreate Sindh project price estimate using AWS Pricing Calculator (On-Demand, 1-Year Reserved, 3-Year Reserved).
- Develop automation plan for db-bastion EC2 instance stop/start lifecycle management.
- Resolve Nova Via S3 permission issue and create MR.
- Execute approved production database query for Sindh project.
- Provide technical support for Node version troubleshooting.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** ECS, EC2, EventBridge, Systems Manager, S3, RDS
- **AWS CLI:** ECS commands for troubleshooting practice
- **Projects:** Nova Via, Sindh CMS

---

## 📚 Notes & Key Learnings

### 1. ECS Troubleshooting Course Completion
- Completed "Troubleshooting: Amazon Elastic Container Service" course.
- Practiced ECS CLI commands on Nova Via project for hands-on experience.

**Key AWS CLI Commands Learned:**

| Command | Purpose |
|---------|---------|
| `aws ecs list-clusters` | List all ECS clusters with basic information |
| `aws ecs describe-clusters` | Get detailed cluster information |
| `aws ecs list-services` | List services within a cluster |
| `aws ecs describe-services` | Get detailed service information |
| `aws ecs list-tasks` | List running tasks in a cluster |
| `aws ecs describe-tasks` | Get detailed task information |
| `aws ecs list-container-instances` | List container instances (EC2 launch type) |

**Log File Locations:**
- ECS Agent logs: `/var/log/ecs/ecs-agent.log.[timestamp]`
- ECS Init logs: `/var/log/ecs/ecs-init.log.[timestamp]`
- Log collector script: `ecs-logs-collector.sh`

**Docker Diagnostic Commands:**
- `docker ps` - List running containers
- `docker logs` - View container STDOUT/STDERR streams
- `docker inspect` - Get detailed container configuration

### 2. AWS Cloud Quest Cloud Practitioner
- Started new gamified learning course on Skillbuilder.
- Completed first assignment successfully.
- Course URL: [AWS Cloud Quest Cloud Practitioner](https://skillbuilder.aws/learn/FU5WCYVGKY/aws-cloud-quest-cloud-practitioner/JF9TKU68GT)

### 3. Sindh Project Price Estimate Recreation
- Recreated comprehensive price estimate using AWS Pricing Calculator.
- Compared three pricing models:
  - **On-Demand:** Pay-as-you-go, no commitment
  - **1-Year Reserved:** All upfront payment, maximum discount for 1-year term
  - **3-Year Reserved:** All upfront payment, maximum discount for 3-year term
- Service period: December 2025 - November 2027 (2 years)
- Recommended strategy: Two consecutive 1-Year Reserved Instances for optimal cost efficiency.

### 4. EC2 Instance Automation Plan (db-bastion)
- Developed comprehensive automation plan for EC2 lifecycle management.
- **Objective:** Stop instance daily at midnight PKT, start daily at defined morning time.
- **Approach:** AWS CDK + EventBridge + SSM Automation with AWS-managed runbooks.

### 5. Nova Via S3 Permission Resolution
- **Issue:** App service task role lacked `s3:PutObject` permission for output bucket.
- **Error:** `User: arn:aws:sts::471464546186:assumed-role/dev-AppServiceStack-AppServiceTaskRole30E9686C-8fwvlGyxRfgN/cfee86895ef649668a6d4b0b69f0b6fb is not authorized to perform: s3:PutObject on resource: "arn:aws:s3:::dev-media-output-471464546186-us-west-2/series_thumbnails/..."`
- **Resolution:** Added S3 bucket permissions to app service task role.
- **MR Created:** [MR #18](https://gitlab.dplit.com/nova-via/cicd/-/merge_requests/18)

### 6. ElevenLabs Webhook Update
- Updated ElevenLabs webhook value in Nova project.
- Notified Afifa to verify changes.

### 7. Node Version Troubleshooting Support
- Assisted Daniyal with Node version compatibility issue.
- **Resolution:** Updated from Node v18 to v20.

### 8. Sindh Production Database Query Execution
- Executed approved production database query after Rohan's approval.
- Coordinated with Khurrum for query execution timing.

---

## 📋 EC2 Automation Plan - db-bastion

### Implementation Overview

| Component | Technology | Purpose |
|-----------|------------|---------|
| Scheduling | Amazon EventBridge | Cron-based scheduling for stop/start |
| Automation | AWS Systems Manager | AWS-managed runbooks for lifecycle actions |
| Infrastructure | AWS CDK (TypeScript) | Infrastructure as Code for reproducible deployment |
| IAM | IAM Role | EventBridge to SSM Automation permissions |

### Schedule Configuration

| Action | Time (PKT) | Time (UTC) | Cron Expression |
|--------|------------|------------|-----------------|
| Stop | Midnight (12:00 AM) | 19:00 | `cron(0 19 * * ? *)` |
| Start | 9:00 AM | 04:00 | `cron(0 4 * * ? *)` |

### CDK Stack Structure

```
db-bastion-schedule-stack/
├── IAM Role (EventBridge → SSM Automation)
├── EventBridge Rule (Stop Schedule)
│   └── Target: SSM Document AWS-StopEC2Instance
└── EventBridge Rule (Start Schedule)
    └── Target: SSM Document AWS-StartEC2Instance
```

### IAM Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:StartAutomationExecution",
        "ec2:StopInstances",
        "ec2:StartInstances"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 📝 MR Created

| Project | MR # | Description | Status |
|---------|------|-------------|--------|
| Nova Via CICD | #18 | Add S3 bucket permissions to app service task role | Pending Review |

---

## 📚 Training & Professional Development

**1. ECS Troubleshooting Course:**
- Course: "Troubleshooting: Amazon Elastic Container Service"
- Status: ✅ Completed
- Hands-on practice: Applied CLI commands to Nova Via project

**2. AWS Cloud Quest Cloud Practitioner:**
- Course: Gamified Cloud Practitioner learning path
- Progress: Assignment 1 completed
- Certificate: Saved in `images/` folder

---

## 🖼️ Evidence & Screenshots

### Course Completion Certificates
- ![AWS Cloud Quest Assignment 1](./images/assignement%201.png) — AWS Cloud Quest Cloud Practitioner Assignment 1 completion certificate

### ECS Troubleshooting Practice
- ![ECS CLI Commands](./images/ecs_cli_commands.png) — ECS CLI command practice screenshots
- ![ECS Console Practice](./images/ecs_console_practice.png) — Nova Via ECS console exploration

### Sindh Price Estimate
- ![Pricing Calculator](./images/pricing_calculator.png) — AWS Pricing Calculator comparison (On-Demand vs Reserved)

---

## ✅ Daily Summary
- Completed ECS troubleshooting course with hands-on CLI practice on Nova Via project.
- Completed first assignment of AWS Cloud Quest Cloud Practitioner gamified course.
- Recreated Sindh project price estimate using AWS Pricing Calculator for all pricing tiers.
- Developed comprehensive EC2 automation plan for db-bastion instance stop/start lifecycle management using CDK + EventBridge + SSM.
- Resolved Nova Via S3 permission issue; created MR #18 for app service task role permissions.
- Updated ElevenLabs webhook value in Nova project; notified Afifa for verification.
- Provided Node version troubleshooting support to Daniyal (v18 → v20 upgrade).
- Executed approved production database query for Sindh project after Rohan's approval.
- Next steps: Await MR #18 review approval; implement db-bastion automation stack; continue AWS Cloud Quest course progression; monitor Sindh infrastructure post-query execution.

Made by Sufi Hassan Asim — 2026-03-30
