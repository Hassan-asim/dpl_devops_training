<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • MM Project Pipeline Migration, CMS Configuration & DynamoDB Troubleshooting Course</h3>

---

## 🎯 Objective Recap
- Complete ECS troubleshooting course and obtain certificate.
- Start new DynamoDB troubleshooting course.
- Migrate MM project pipelines from CodeCommit to GitLab source.
- Create environment setup guides for development team.
- Resolve pipeline source integration and deployment issues.
- Analyze repository migration status and plan remaining work.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CodePipeline, CodeBuild, IAM, SSM Parameter Store
- **Projects:** Miracle Morning (MM), Sindh CMS

---

## 📚 Notes & Key Learnings

### 1. ECS Troubleshooting Course Completion
- Completed "Troubleshooting: Amazon Elastic Container Service" course.
- Certificate of completion saved in `images/` folder.

### 2. DynamoDB Troubleshooting Course Started
- Started new course: "Troubleshooting: Amazon DynamoDB"
- Course URL: [AWS Skillbuilder - DynamoDB Troubleshooting](https://skillbuilder.aws/renderer/?module_id=JUQMYVKMV4%3A001.000.002&product_id=1X8WNBRHH3%3A001.000.002&registration_id=152204e4-a4c1-597c-a7f8-093f70f038f2&referrer=https%3A%2F%2Fskillbuilder.aws%2Flearn%2FC9VBXQJM86%2Famazon-dynamodb--troubleshooting%2F1X8WNBRHH3&navigation=digital)
- Progress: In progress.

### 3. MM Project Pipeline Migration
- Successfully migrated multiple MM project pipelines from CodeCommit to GitLab source.
- **Pipelines Migrated:**
  - `mm-backend` (Production)
  - `mm-event`
  - `mm-checkout` (completed by Basit using provided steps)
  - `mm-cms` (completed)
- **Pipeline Source Integration Fix:**
  - Resolved GitLab connection issue by adding IAM permission: `codestar-connections:UseConnection`
  - Policy: `AllowGitLabConnection`
  - **Error Resolved:** `Unable to use Connection: arn:aws:codeconnections:us-east-1:649871028995:connection/d2f844bb-b963-4b3c-ae1b-2c57b2f10ef0. The provided role does not have sufficient permissions.`
  - **Action:** Added required policy to the IAM role to grant CodeConnections access.
  - **Result:** Released changes and source stage completed successfully.
  - Enabled pipelines to fetch code from GitLab successfully.

### 4. CMS Pipeline Configuration
- Identified CMS as a frontend (Vite) application.
- Configured environment variables in CodeBuild using `VITE_*` format.
- Ensured proper environment variable handling for Vite applications.

### 5. mm-event Pipeline Deployment Fix
- **Issue:** Deployment failure due to leftover `node_modules` from previous builds.
- **Root Cause:** `start.sh` script not cleaning old files before deployment.
- **Resolution:** Coordinated manual cleanup with Basit; deployment succeeded.

### 6. Environment Setup Guides Created
- Created and shared two comprehensive guides for development team:
  - **SSM Parameter Store based `.env` management**
  - **Multi-EC2 single-master variable automation**
- Included demo examples for easy implementation.

### 7. Repository Migration Analysis
- Identified 4 extra pipelines dependent on repositories not yet migrated to GitLab.
- **Pending Migration:** `MiracleMorning-portalApp` repo (no mirror in GitLab yet).
- **Status:** Repositories not ready for migration; codebase still in development.
- Will coordinate with Basit when repositories are ready for pipeline source change.

---

## 📋 Pipeline Migration Summary

| Pipeline | Source Change | Status | Notes |
|----------|---------------|--------|-------|
| mm-backend (Prod) | CodeCommit → GitLab | ✅ Completed | Verified deployment and stability |
| mm-event | CodeCommit → GitLab | ✅ Completed | Required manual node_modules cleanup |
| mm-checkout | CodeCommit → GitLab | ✅ Completed | Completed by Basit using provided steps |
| mm-cms | CodeCommit → GitLab | ✅ Completed | Repository and pipeline migrated |
| mm-enterprise | CodeCommit → GitLab | ⏳ Pending | Repository analyzed and reviewed |
| MiracleMorning-portalApp (4 pipelines) | CodeCommit → GitLab | 🚧 Not Ready | Codebase not migrated yet; pending development completion |

---

## 🧪 Troubleshooting & Problem Resolution

### 1. GitLab Connection Permission Issue
- **Symptom:** Pipelines unable to fetch code from GitLab.
- **Error:** `Unable to use Connection: arn:aws:codeconnections:us-east-1:649871028995:connection/d2f844bb-b963-4b3c-ae1b-2c57b2f10ef0. The provided role does not have sufficient permissions.`
- **Investigation:** Reviewed IAM permissions for CodeStar Connections.
- **Finding:** Missing `codestar-connections:UseConnection` permission.
- **Resolution:** Added `AllowGitLabConnection` policy to IAM role; released changes and source stage completed successfully.

### 2. mm-event Deployment Failure
- **Symptom:** Pipeline failed during deployment stage.
- **Investigation:** Analyzed build logs and deployment behavior.
- **Finding:** Leftover `node_modules` from previous builds causing conflicts.
- **Root Cause:** `start.sh` script not cleaning old files before deployment.
- **Resolution:** Coordinated manual cleanup with Basit; deployment succeeded.

---

## 📝 Documentation Created

| Document | Purpose | Audience |
|----------|---------|----------|
| SSM Parameter Store Setup Guide | Guide for `.env` management using AWS SSM | Development Team |
| Multi-EC2 Single-Master Variable Setup Guide | Guide for environment variable automation across multiple EC2 instances | Development Team |

---

## 📚 Training & Professional Development

**1. ECS Troubleshooting Course:**
- Course: "Troubleshooting: Amazon Elastic Container Service"
- Status: ✅ Completed
- Certificate: Saved in `images/` folder

**2. DynamoDB Troubleshooting Course:**
- Course: "Troubleshooting: Amazon DynamoDB"
- Progress: In progress
- Focus: DynamoDB diagnostic techniques, common failure patterns, and resolution strategies

---

## 🖼️ Evidence & Screenshots

### Course Completion Certificates
- ![ECS Troubleshooting Course Completion](./images/certificate%20of%20completion.png) — Certificate of completion for ECS Troubleshooting course

### Pipeline Migration Evidence
- ![Pipeline Source Change](./images/pipeline_source_change.png) — Pipeline source updated to GitLab
- ![GitLab Connection Fix](./images/gitlab_connection_fix.png) — IAM permission fix applied

---

## ✅ Daily Summary
- Completed ECS troubleshooting course and obtained certificate of completion.
- Started new DynamoDB troubleshooting course on AWS Skillbuilder.
- Successfully migrated MM project pipelines (backend, event, checkout) from CodeCommit to GitLab source.
- Resolved GitLab connection issue by adding required IAM permissions for CodeStar Connections.
- Fixed mm-event deployment failure caused by leftover node_modules; coordinated cleanup with Basit.
- Configured CMS pipeline environment variables using VITE_* format for frontend application.
- Created and shared comprehensive environment setup guides for development team (SSM Parameter Store & Multi-EC2 automation).
- Analyzed repository migration status; identified pending repos and dependencies.
- Coordinated with Basit on remaining pipeline migrations; task postponed to next day due to scheduling.
- Next steps: Complete remaining MM pipeline migrations (mm-enterprise, MiracleMorning-portalApp); continue DynamoDB troubleshooting course; support development team with environment setup guide implementation.

Made by Sufi Hassan Asim — 2026-04-07
