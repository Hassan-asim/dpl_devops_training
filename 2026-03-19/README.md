<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • AWS Training, Lambda Policy Investigation, Pipeline Debug & Infrastructure Support — 2026-03-19</h3>

---

## 🎯 Objective
Continue AWS training course; investigate Lambda function policy issue in UAT environment; support production deployment changes; troubleshoot UAT frontend pipeline deployment failure; research infrastructure access for new meeting room app.

---

## 💡 Summary
Continued AWS training course progress on Skillbuilder. Investigated Lambda function error reported by Afifa in UAT environment; identified that the policy lacked the required resource attachments and sought guidance from Hazar on the appropriate approach. Remained available for production deployment changes as requested by Khurrum. Investigated UAT frontend pipeline failure at deploy stage caused by Node version mismatch in fix_permission.sh script. Joined new group for meeting room app infrastructure request; conducted initial research and escalated to Hazar for permission approval guidance.

---

## 🚀 Development & Infrastructure Operations

**1. Lambda Function Policy Investigation (UAT):**
- Investigated error reported by Afifa in Lambda function within UAT environment.
- Root cause identified: policy did not have the required resources attached that the function was attempting to access.
- Communicated findings to Hazar and requested guidance on preferred approach:
  - Option A: Add tables to resources to enable console access.
  - Option B: Follow alternative approach as determined by team lead.
- Awaiting further instructions on resolution path.

**2. UAT Frontend Pipeline Failure Investigation:**
- Monitored pipelines and identified UAT frontend pipeline failure at deploy stage.
- Root cause identified: `fix_permission.sh` file failing due to Node version mismatch at deploy stage (not using LTS version).
- Documented error with screenshot from event logs.
- Escalated to Hazar with supporting evidence for resolution.

**3. Production Deployment Support:**
- Responded to Khurrum's request to be available for production deployment changes.
- Maintained availability and readiness to support production environment modifications.
- Stood by for deployment coordination and execution as needed.

**4. Meeting Room App Infrastructure Request:**
- Added to new group for basic/low-cost infrastructure deployment for meeting room app backend.
- Request: Provide environment by Tuesday for Daniyal (GTO) project deployment.
- Constraint identified: Lacking permissions to grant access without approval; Hazar offline for authorization.
- Conducted preliminary research on infrastructure requirements.
- Escalated to Hazar via message for further instructions and approval process.

---

## 📚 Training & Professional Development

**1. AWS Training Course:**
- Continued progress through AWS training course on Skillbuilder.
- Course URL: [skillbuilder.aws - Amazon Elastic Block Store Troubleshooting](https://skillbuilder.aws/renderer/?module_id=AS76YCA638%3A001.000.000&product_id=BEMA4TNCQ7%3A001.000.000&registration_id=8c1e2648-b430-59d7-9e88-b3b6b71eba3e&referrer=https%3A%2F%2Fskillbuilder.aws%2Flearn%2FWWAETUHGU3%2Famazon-elastic-block-store--troubleshooting%2FBEMA4TNCQ7&navigation=digital).
- Focused on EBS troubleshooting fundamentals and diagnostic techniques.

---

## 🔍 Troubleshooting & Problem Resolution

**1. Lambda Policy Resource Access Issue:**
- **Symptom:** Afifa reported Lambda function error in UAT environment.
- **Investigation:** Analyzed policy configuration and resource attachments.
- **Finding:** Policy missing required resource definitions for function access targets.
- **Action:** Communicated findings to Hazar; awaiting decision on resolution approach.

**2. UAT Frontend Pipeline Deploy Stage Failure:**
- **Symptom:** Pipeline failed at deploy stage during routine monitoring.
- **Investigation:** Examined event logs and deployment scripts.
- **Finding:** `fix_permission.sh` script failing due to non-LTS Node version at deploy stage.
- **Action:** Documented error with screenshot; escalated to Hazar with supporting evidence.

---

## 🎯 Cross-Functional Collaboration & Operations

**1. Lambda Policy Support:**
- Collaborated with Afifa to investigate and identify Lambda function error root cause.
- Coordinated with Hazar on resolution strategy and approval process.

**2. Production Deployment Readiness:**
- Responded to Khurrum's request for production deployment support.
- Maintained availability for critical production environment changes.

**3. Meeting Room App Infrastructure Planning:**
- Engaged with new project request for backend deployment infrastructure.
- Conducted initial research on low-cost infrastructure options.
- Initiated approval process with Hazar for access permissions.

**4. Pipeline Monitoring:**
- Conducted proactive monitoring of deployment pipelines.
- Identified and documented UAT frontend pipeline failure.
- Escalated with detailed error evidence for swift resolution.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Continued AWS training course progress.
- ✅ Investigated Lambda function policy issue in UAT environment.
- ✅ Identified missing resource attachments and escalated for guidance.
- ✅ Remained available for production deployment changes.
- ✅ Investigated UAT frontend pipeline failure; identified Node version issue.
- ✅ Responded to meeting room app infrastructure request; conducted research.

**Key Learnings:**
- Lambda function policies must explicitly define all resources the function needs to access.
- Pipeline deploy stage failures often stem from environment configuration mismatches (e.g., Node version).
- Proactive pipeline monitoring enables early detection and faster incident resolution.
- Infrastructure access requests require proper approval chains and permission validation.
- Low-cost infrastructure planning requires balancing performance requirements with cost constraints.

**Next Steps:**
1. Continue and complete remaining modules of AWS troubleshooting course.
2. Await Hazar's guidance on Lambda policy resolution approach.
3. Monitor UAT frontend pipeline for fix deployment and successful completion.
4. Await further instructions on meeting room app infrastructure provisioning.
5. Continue routine infrastructure monitoring across all projects.
6. Support any additional production deployment changes as required.
