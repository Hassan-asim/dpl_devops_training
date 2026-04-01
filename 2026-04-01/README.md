<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • CloudWatch Log Group Implementation, ECS Course Progress & CodeCommit to GitLab Migration Planning</h3>

---

## 🎯 Objective Recap
- Implement CloudWatch Log Group for Complaint Audit Logs as requested by Afifa.
- Continue ECS troubleshooting course and reach 60% completion.
- Complete AWS Cloud Quest Cloud Practitioner assignment #2.
- Create migration plan for moving repositories from AWS CodeCommit to GitLab.
- Execute off-hours Prod Sindh RDS queries as requested by Khurrum.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CloudWatch, IAM, CDK
- **Projects:** Nova Via, Sindh

---

## 📚 Notes & Key Learnings

### 1. CloudWatch Log Group Implementation for Complaint Audit Logs
- **Task Request:** Afifa requested creation of a new CloudWatch log group for Complaint Audit Logs with access for the app service stack.
- **Analysis and Design:**
  - Analyzed infrastructure requirements for adding logging support.
  - Designed approach to create dedicated CloudWatch Log Group for audit logging.
  - Planned IAM updates to allow App Service task role to write logs.
  - Reviewed existing codebase patterns for consistency.
- **Implementation:**
  - Added enableComplaintAuditLogs flag following existing optional features pattern (enableSes, enableBedrock).
  - Created CloudWatch Log Group with appropriate IAM permissions.
  - Added export for log group name following existing EcsLogGroupName pattern.
- **Code Review Discussion with Hazar:**
  - Discussed whether enableComplaintAuditLogs should be always enabled vs optional.
  - Explained export usage: consistent with existing EcsLogGroupName export for potential future monitoring, not currently imported.
- **Status:** Merge request created and sent for approval.

### 2. ECS Troubleshooting Course Progress
- Continued "Troubleshooting: Amazon Elastic Container Service" course.
- Achieved 60% completion.
- Enhanced understanding of ECS troubleshooting techniques and best practices.

### 3. AWS Cloud Quest Cloud Practitioner
- Started new gamified learning course on AWS Skillbuilder.
- Working on assignment #2, in progress.
- Course URL: [AWS Cloud Quest Cloud Practitioner](https://skillbuilder.aws/learn/FU5WCYVGKY/aws-cloud-quest-cloud-practitioner/JF9TKU68GT)

### 4. CodeCommit to GitLab Migration Planning
- **Context:** Ali introduced Basit, who needs project repositories migrated from AWS CodeCommit to GitLab.
- **Planning Activities:**
  - Discussed migration requirements with Ali and Basit.
  - Produced comprehensive migration plan and guide.
  - Identified repository names: mm-backend, mm-enterprise, mm-cms, mm-event, mm-checkout.
  - Outlined migration strategy, responsibilities, and timeline.
- **Migration Plan Highlights:**
  - Standard migration using git mirror for most repositories.
  - Special handling for repositories with sensitive history (e.g., .env files).
  - Post-migration pipeline updates to use GitLab as source.
- **Status:** Repositories created in GitLab, ready for migration execution.

### 5. Production Sindh RDS Queries
- Completed off-hours production database queries in Sindh project as requested by Khurrum.
- Ensured safe query execution during non-peak hours and confirmed result validity.

---

## 📋 Migration Plan Summary

### Repository List
- mm-backend
- mm-enterprise
- mm-cms
- mm-event
- mm-checkout

### Key Migration Steps
1. Clone repository from CodeCommit using mirror mode.
2. Add GitLab as remote.
3. Push all data to GitLab.
4. Verify branches, commits, and tags in GitLab.

### Special Considerations
- Repositories with .env in commit history require clean migration (no mirror).
- Pipeline integration will be updated after successful migration.

---
