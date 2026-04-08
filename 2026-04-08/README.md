<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • MM Pipeline Migration Fixes, CodeBuild Environment Updates & Deployment Path Resolution</h3>

---

## 🎯 Objective Recap
- Fix mm-enterprise pipeline errors after source migration to GitLab.
- Resolve CodeBuild Node.js version compatibility issues.
- Fix deployment path mismatches between QA and production environments.
- Address .env file location issues in deployment scripts.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CodeBuild, CodePipeline, EC2
- **GitLab Instance:** gitlab.dplit.com
- **Projects:** Miracle Morning (MM)

---

## 📚 Notes & Key Learnings

### 1. mm-enterprise Pipeline Fixes
- **Collaboration with Basit:**
  - Connected with Basit to address pipeline errors post-migration.
  - Analyzed and researched issues while Basit was occupied with sprint work.
  - Provided fixes and updates to Basit for implementation.

### 2. CodeBuild Environment Fix
- **Problem:** Build failing due to unsupported Node.js version on old Linux image.
  - Node v20 not supported on previous standard image.
  - EBADENGINE warnings from @tailwindcss/oxide and eslint-visitor-keys.
- **Solution:**
  - Updated CodeBuild environment to Standard 6 (aws/codebuild/amazonlinux2-x86_64-standard:6.0).
  - Verified Node v20 and npm version support in install phase.
- **Result:** Build completed successfully.

### 3. Deployment Path Resolution
- **Problem:** Deployment failure due to incorrect path in start.sh.
  - Script pointed to production path `/var/www/partner-mm-prod`.
  - appspec.yml deploys to QA path `/var/www/qa-partner.miraclemorning.com`.
- **Solution:**
  - Updated start.sh to use QA instance path.
  - Added directory existence verification before commands.
- **Result:** Deployment script runs without path-related failures.

### 4. Environment File Issue
- **Problem:** .env file not found during ApplicationStart phase.
  - Error: `cp: cannot stat '../environments/partner/.env': No such file or directory`.
  - .env located in production folder instead of QA folder.
- **Action Needed:**
  - Update start.sh to copy .env from correct QA environment path.
  - Ensure environment variables available before PM2 startup.
- **Status:** Basit will handle this fix when available.

### 5. PM2 Deployment Verification
- Confirmed pm2 stop handles non-running processes gracefully.
- PM2 starts application using updated ecosystem config for QA environment.

### 6. Course Continuation
- Continued AWS training courses as scheduled.
- Work in progress on assigned learning modules.

---

## 📋 Action Items & Timeline

### Completed Today
- ✓ CodeBuild environment updated to support Node v20
- ✓ Deployment paths corrected for QA environment
- ✓ Build and deployment script fixes implemented
- ✓ Analysis and fixes provided to Basit

### Pending
- ⏳ .env file path correction in start.sh (Basit to implement)
- ⏳ Final deployment verification after .env fix

### Key Implementation Notes
- Standard 6 CodeBuild image required for Node v20 compatibility
- Deployment scripts must distinguish between QA and production paths
- Environment file locations vary between environments and must be correctly referenced
- PM2 commands are robust and handle edge cases appropriately

---