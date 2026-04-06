<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Pipeline Source Migration Completion, Environment Management Guides & Team Onboarding</h3>

---

## 🎯 Objective Recap
- Complete pipeline source migration from CodeCommit to GitLab for all Miracle Morning repositories.
- Create comprehensive guides for environment variable management and multi-EC2 setup.
- Onboard new DevOps team member with CDK and repository structure.
- Resolve deployment issues and ensure application stability.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CodePipeline, CodeBuild, SSM Parameter Store, IAM
- **GitLab Instance:** gitlab.dplit.com
- **Projects:** Miracle Morning (multi-tenant project)

---

## 📚 Notes & Key Learnings

### 1. Pipeline Source Migration Completion
- **Production Pipeline Update:**
  - Successfully updated production backend pipeline source to GitLab (mm-backend).
  - Verified deployment and confirmed application stability.
- **CMS Pipeline Configuration:**
  - Identified CMS as frontend Vite application.
  - Configured environment variables in CodeBuild using VITE_* format for proper frontend builds.
- **mm-event Pipeline Migration:**
  - Updated mm-event pipeline source to GitLab.
  - Resolved deployment failure caused by leftover node_modules.
  - Fixed start.sh script to properly clean old files before deployment.
- **Integration Fix:**
  - Resolved GitLab connection issue by adding IAM permission: codestar-connections:UseConnection.
  - Enabled successful code fetching from GitLab across all pipelines.

### 2. Environment Management Solutions
- **Multi-EC2 Single-Master Setup:**
  - Created comprehensive guide for automatic MASTER=true/false variable assignment.
  - Included set_master_var.sh script, appspec.yml hook configuration, and deployment flow.
  - Provided demo examples for dev team implementation.
- **SSM Parameter Store Guide:**
  - Drafted complete guide for secure environment variable storage.
  - Covered dev/prod environments for all 5 repositories (mm-backend, mm-checkout, mm-cms, mm-enterprise, mm-event).
  - Included scripts and appspec.yml setup for automatic .env injection during deployment.
- **Decision:** Proceed with source migration first, implement environment solutions afterward to minimize risk.

### 3. Team Onboarding and Collaboration
- **New Hire Onboarding:**
  - Conducted meeting with Ali and Hazaifa (new DevOps team member).
  - Familiarized with CDK structure and repository organization.
- **Dev Team Communication:**
  - Shared step-by-step guides in plain text format.
  - Explained demo examples and implementation approaches.
- **Collaboration with Basit:**
  - Coordinated pipeline source changes for remaining repositories.
  - Started CMS pipeline migration during meeting.

### 4. System Understanding and Debugging
- **Deployment Analysis:**
  - Analyzed pipeline failures and deployment behavior across different service types.
  - Improved understanding of environment handling, build vs runtime configurations, and deployment flows.
- **Course Continuation:**
  - Continued AWS training course as scheduled.
  - Work in progress on assigned learning modules.

---

## 📋 Action Items & Timeline

### Completed Today
- ✓ Production pipeline source update to GitLab
- ✓ CMS pipeline configuration and environment setup
- ✓ mm-event pipeline migration and deployment fix
- ✓ Multi-EC2 master variable setup guide creation
- ✓ SSM Parameter Store environment management guide
- ✓ New DevOps team member onboarding
- ✓ GitLab connection IAM permission fix

### Pending
- ⏳ Complete remaining pipeline source migrations
- ⏳ Implement SSM Parameter Store solution
- ⏳ Validate all deployments post-migration

### Key Implementation Notes
- Frontend applications require VITE_* prefixed environment variables in CodeBuild
- IAM codestar-connections:UseConnection permission is essential for GitLab integration
- Environment variable management should be implemented after source migration to avoid complications
- Multi-EC2 setups require careful master variable assignment to prevent conflicts

---