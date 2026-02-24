<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • UAT Stack Migration, Git Conflict Resolution & Pipeline Fixes — 2026-02-23</h3>

---

## 🎯 Objective
Migrate UAT Frontend and Backend stacks to T4g.medium (ARM64) instances, resolve AWS CDK deployment issues, manage git branch merges and conflicts, and assist in fixing the Dev Frontend Admin Pipeline.

---

## 💡 Summary
Successfully updated `FrontendStackUat` and `BackendStackUat` to utilize T4g.medium ARM64 instances, ensuring cost-efficiency and performance improvements. Verified all changes using `cdk diff` and resolved specific deployment hurdles related to UserData and launch templates. Managed the migration workflow within the `feature/uat-t4g-medium-migration` branch, which included resolving complex `package-lock.json` merge conflicts after pulling the latest updates from the main branch. Additionally, provided technical assistance to Khurrum for the Dev Frontend Admin Pipeline, updating the `buildspec.yml` with a more recent Node.js version and revised build commands, leading to a successful pipeline run.

---

## 🚀 Infrastructure & Deployment

**1. UAT Stack Migration to T4g.medium (ARM64):**
- Updated `FrontendStackUat` and `BackendStackUat` configuration to transition from x86 to ARM64 architecture (T4g.medium).
- Performed rigorous verification using `cdk diff` to confirm that only intended instance type and architecture changes were staged.
- Resolved deployment-time errors related to AWS CDK's handling of UserData and its interaction with EC2 Launch Templates.
- Successfully deployed the updated stacks to the AWS UAT environment.

**2. Git Workflow & Merge Resolution:**
- Developed changes within the dedicated `feature/uat-t4g-medium-migration` branch.
- Synchronized the feature branch with the `main` branch, necessitating the manual resolution of merge conflicts within `package-lock.json`.
- Finalized the branch state and prepared it for a formal Merge Request (MR) into the main codebase.

---

## 🔧 Pipeline Support & Fixes

**1. Dev Frontend Admin Pipeline Troubleshooting:**
- Assisted Khurrum in diagnosing a build stage failure within the Dev Frontend Admin Pipeline.
- Implemented fixes in the `buildspec.yml` file, specifically upgrading the Node.js runtime environment.
- Refined the build commands to align with the new environment requirements.
- Verified the fix by monitoring a successful end-to-end build of the pipeline.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Migrated UAT Frontend/Backend stacks to T4g.medium.
- ✅ Resolved CDK deployment issues (UserData/Launch Templates).
- ✅ Handled branch merges and `package-lock.json` conflicts.
- ✅ Fixed build failure in Dev Frontend Admin Pipeline.

**Next Steps:**
- Monitor UAT environment stability on the new T4g instances.
- Proceed with similar ARM64 migration strategies for other environments (e.g., PROD) if UAT remains stable.
- Finalize the MR review process for the UAT migration branch.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-02-23
