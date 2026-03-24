<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Lambda Policy Resolution (UAT & PROD), Production Deployment Support & Infrastructure Request — 2026-03-24</h3>

---

## 🎯 Objective
Resolve Lambda function policy issues in UAT and production environments; support production deployment changes; respond to infrastructure request for meeting room app; monitor pipeline health during production deployments.

---

## 💡 Summary
Investigated and resolved Lambda function policy issue reported by Afifa in UAT environment; identified missing resource attachments, obtained approval from Hazar, implemented changes, and confirmed resolution. Extended the same fix to production environment by adding required tables to policy after receiving the list from Afifa. Remained available for production deployment changes as requested by Khurrum; monitored pipeline health during deployments with successful completion. Responded to meeting room app infrastructure request; awaiting further instructions from Hazar regarding access permissions.

---

## 🚀 Development & Infrastructure Operations

**1. Lambda Function Policy Resolution (UAT Environment):**
- Investigated error reported by Afifa in Lambda function within UAT environment.
- Root cause identified: policy did not have the required resources attached that the function was attempting to access.
- Communicated findings to Hazar and requested guidance on preferred approach.
- Received approval to add tables to the permission list.
- Implemented policy changes to include required resource attachments.
- Coordinated with Afifa for testing; confirmed issue resolved and functioning correctly.

**2. Lambda Function Policy Extension (Production Environment):**
- Requested list of tables from Afifa for production environment policy updates.
- Received table list and implemented corresponding policy changes in production.
- Ensured production Lambda function has proper resource access permissions.
- Changes applied to maintain consistency between UAT and production environments.

**3. Production Deployment Support:**
- Responded to Khurrum's request to be available for production deployment changes.
- Maintained availability and readiness to support production environment modifications.
- Monitored pipeline health during production deployments as a precautionary measure.
- Verified all deployments completed successfully with no issues or failures detected.

**4. Meeting Room App Infrastructure Request:**
- Added to new group for basic/low-cost infrastructure deployment for meeting room app backend.
- Request: Provide environment by Tuesday for Daniyal (GTO) project deployment.
- Constraint identified: Lacking permissions to grant access without approval; Hazar offline for authorization.
- Conducted preliminary research on infrastructure requirements.
- Escalated to Hazar via message for further instructions and approval process.
- Status: Awaiting further instructions; no response received yet.

---

## 🔍 Troubleshooting & Problem Resolution

**1. Lambda Policy Resource Access Issue (UAT):**
- **Symptom:** Afifa reported Lambda function error in UAT environment.
- **Investigation:** Analyzed policy configuration and resource attachments.
- **Finding:** Policy missing required resource definitions for function access targets.
- **Action:** Communicated findings to Hazar; received approval to add tables to permission list.
- **Resolution:** Implemented policy changes; Afifa confirmed functionality restored.

**2. Lambda Policy Resource Access Issue (Production):**
- **Requirement:** Extend UAT fix to production environment for consistency.
- **Action:** Requested table list from Afifa; implemented policy changes in production.
- **Resolution:** Production Lambda function now has proper resource access permissions.

---

## 🎯 Cross-Functional Collaboration & Operations

**1. Lambda Policy Support:**
- Collaborated with Afifa to investigate, identify, and resolve Lambda function error root cause.
- Coordinated with Hazar on resolution strategy and obtained necessary approvals.
- Extended solution from UAT to production environment for complete resolution.

**2. Production Deployment Readiness:**
- Responded to Khurrum's request for production deployment support.
- Maintained availability for critical production environment changes.
- Monitored pipeline health during deployments; all changes deployed successfully.

**3. Meeting Room App Infrastructure Planning:**
- Engaged with new project request for backend deployment infrastructure.
- Conducted initial research on low-cost infrastructure options.
- Initiated approval process with Hazar for access permissions.
- Awaiting further instructions to proceed with environment provisioning.

**4. Pipeline Health Monitoring:**
- Conducted proactive monitoring of production deployment pipelines.
- Verified all deployments completed without issues or failures.
- Ensured production stability during change implementation.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Investigated Lambda function policy issue in UAT environment.
- ✅ Identified missing resource attachments and obtained approval for resolution.
- ✅ Implemented policy changes in UAT; confirmed resolution with Afifa.
- ✅ Extended policy fix to production environment with required table list.
- ✅ Remained available for production deployment changes.
- ✅ Monitored pipeline health during production deployments (all successful).
- ✅ Responded to meeting room app infrastructure request; escalated for approval.

**Key Learnings:**
- Lambda function policies must explicitly define all resources the function needs to access across all environments.
- Environment consistency (UAT to production) is critical for reliable application behavior.
- Proactive pipeline monitoring during deployments ensures early detection of potential issues.
- Cross-environment policy management requires careful coordination and documentation.
- Infrastructure access requests require proper approval chains and timely follow-up.

**Next Steps:**
1. Await further instructions from Hazar regarding meeting room app infrastructure provisioning.
2. Continue routine infrastructure monitoring across all projects.
3. Support any additional production deployment changes as required.
4. Monitor Lambda function performance in both UAT and production environments.
5. Document policy change procedures for future reference and consistency.
