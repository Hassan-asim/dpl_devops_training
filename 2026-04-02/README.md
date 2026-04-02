<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • GitLab Integration Setup, AWS Pipeline Configuration Planning & Course Continuation</h3>

---

## 🎯 Objective Recap
- Facilitate CodeCommit to GitLab repository migration with Basit.
- Investigate and plan CodePipeline source change task.
- Research GitLab connection setup in AWS Developer Tools.
- Continue ongoing AWS courses.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CodePipeline, Developer Tools, Connections
- **GitLab Instance:** gitlab.dplit.com
- **Projects:** Nova Via (multi-tenant project)

---

## 📚 Notes & Key Learnings

### 1. GitLab Repository Setup and CodeCommit Migration
- **Activities Completed:**
  - Created all required GitLab repositories: mm-backend, mm-enterprise, mm-cms, mm-event, mm-checkout.
  - Set up main branches in each repository to serve as default branches.
  - Coordinated with Basit on migration of codebases from AWS CodeCommit to GitLab.
- **Key Learning:** Default branches in GitLab must be created first to allow pushing from local repositories during migration.
- **Status:** Migration in progress, awaiting Basit's progress on repository transfers.

### 2. AWS CodePipeline GitLab Integration Research
- **Task Context:** Exploring how to update CodePipeline to use GitLab as the source instead of CodeCommit.
- **Findings:**
  - AWS Developer Tools provides a Connections feature for source integrations.
  - GitLab self-managed connections are required for gitlab.dplit.com (not gitlab.com SaaS).
  - Connection setup requires careful configuration of VPC selection and access token.
- **Challenges:**
  - VPC selection criteria for GitLab connection setup needs clarification.
  - Access token setup process requires further investigation.
- **Next Steps:**
  - Requested Ali to create the GitLab connection in AWS Developer Tools.
  - Plan to update CodePipeline configuration to use GitLab as source after connection is established.

### 3. Course Continuation
- Continued AWS training course as scheduled.
- Work in progress on assigned learning modules.

---

## 📋 Action Items & Timeline

### Completed Today
- ✓ GitLab repository creation (mm-backend, mm-enterprise, mm-cms, mm-event, mm-checkout)
- ✓ AWS GitLab connection research and documentation
- ✓ Coordination with Basit on migration strategy

### Pending
- ⏳ Basit's response on CodeCommit to GitLab migration progress
- ⏳ Ali to create GitLab connection in AWS Developer Tools
- ⏳ CodePipeline source configuration update (scheduled for tomorrow)

### Key Implementation Notes
- GitLab self-managed instance (gitlab.dplit.com) uses different connection setup than SaaS gitlab.com
- Default branch creation in GitLab is prerequisite for successful repository migration
- Connection setup requires clarification on VPC access requirements

---