<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • GitLab Migration Execution, AWS Pipeline Updates & Deployment Troubleshooting</h3>

---

## 🎯 Objective Recap
- Complete GitLab repository migration from CodeCommit.
- Establish AWS GitLab connection and update Dev pipeline.
- Resolve deployment issues and environment configuration.
- Plan production pipeline migration.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CodePipeline, CodeStar Connections, EC2
- **GitLab Instance:** gitlab.dplit.com
- **Projects:** Miracle Morning (multi-tenant project)

---

## 📚 Notes & Key Learnings

### 1. GitLab Repository Migration Completion
- **Activities Completed:**
  - Created all required GitLab repositories: mm-backend, mm-enterprise, mm-cms, mm-event, mm-checkout.
  - Set up main branches as default branches in each repository.
  - Collaborated with Basit to successfully migrate codebases from AWS CodeCommit to GitLab.
- **Key Learning:** Proper branch setup is essential for seamless migration and deployment workflows.

### 2. AWS GitLab Connection Establishment
- **Connection Setup:**
  - Explored AWS CodeStar Connections for GitLab integration.
  - Successfully established connection for gitlab.dplit.com using access token.
  - Resolved initial 403 forbidden error through collaboration with Ali.
- **Key Finding:** Self-managed GitLab connections do not require VPC configuration, simplifying setup.

### 3. Dev Pipeline Migration and Deployment
- **Pipeline Update:**
  - Updated Dev pipeline (Miracle-morning-Dev-NodeJs-App-CICD-Pipeline) to use GitLab (mm-backend) as source.
  - Verified successful source stage change.
- **Deployment Issue Resolution:**
  - Encountered deployment failure due to missing appspec.yml (excluded by .gitignore).
  - Fixed by including appspec.yml in the repository.
  - Deployment stage completed successfully after resolution.
- **Environment Configuration:**
  - Identified missing .env file in GitLab repository (present in CodeCommit).
  - Temporarily resolved by manually copying .env to EC2 instance and adjusting paths.
  - Confirmed Dev application is running successfully.

### 4. Production Pipeline Planning
- **Risk Mitigation:** Deferred Prod pipeline (MiracleMorning-Stage-CICD) update to avoid production risks.
- **Next Steps:** Plan to implement proper environment variable management (likely via AWS Secrets Manager) before production migration.

### 5. Course Continuation
- Continued AWS training course as scheduled.
- Work in progress on assigned learning modules.

---

## 📋 Action Items & Timeline

### Completed Today
- ✓ GitLab repository creation and migration completion
- ✓ AWS GitLab connection establishment
- ✓ Dev pipeline source update to GitLab
- ✓ Deployment issue resolution (appspec.yml inclusion)
- ✓ Dev environment configuration and verification

### Pending
- ⏳ Implement proper environment variable management strategy
- ⏳ Update Prod pipeline to GitLab
- ⏳ Validate production deployment

### Key Implementation Notes
- appspec.yml must be included in repository despite .gitignore for CodeDeploy functionality
- Environment variables require secure management solution (AWS Secrets Manager recommended)
- Self-managed GitLab connections simplify AWS integration compared to SaaS

---