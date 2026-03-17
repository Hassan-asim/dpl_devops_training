<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Nova Project Infrastructure, Sindh Database Operations & Stack Deployments — 2026-03-16</h3>

---

## 🎯 Objective
Continue Nova project infrastructure task (wildcard certificates, SSL configuration); execute approved Sindh database queries; manage DynamoDB table cleanup; deploy Nova via app service stack changes; finalize environment variable updates; coordinate on certificate stack provisioning.

---

## 💡 Summary
Continued the Nova project infrastructure task assigned by Hazar, awaiting further approval before proceeding with deployment. Executed approved database queries on Sindh project to correct complaint status and disposal records. Performed DynamoDB table cleanup for the Sindh project after obtaining necessary approvals. Implemented app service stack changes for Nova via to enable JWT value retrieval, deployed to AWS. Finalized the environment variable MR from last Friday, merging changes into main for both dev.yaml and prod.yaml. Coordinated with Hazar on the certificate stacks task, awaiting approval to proceed.

---

## 🚀 Development & Infrastructure Operations

**1. Nova Project Infrastructure (Continued):**
- Continued work on wildcard certificate provisioning for domain `novalifeapp.com`.
- Prepared configurations for custom domain and SSL on CloudFront: `portal-dev.novalifeapp.com`, `video-cdn-dev.novalifeapp.com`.
- Prepared configurations for custom domain and SSL on ALB: `api-dev.novalifeapp.com`.
- Following Rahbar project CI/CD implementation as reference: [gitlab.dplit.com/rahber-crm/cicd](https://gitlab.dplit.com/rahber-crm/cicd).
- Work in progress at: [gitlab.dplit.com/nova-via/cicd](https://gitlab.dplit.com/nova-via/cicd).
- Awaiting Hazar's approval on how to proceed (per his instruction to ask before deploying).

**2. Sindh Project Database Operations:**
- Executed approved database queries to correct complaint status and disposal records:
  - Updated `tbl_complain` set `complain_status = 'Disposed Off (Relief Allowed)'` where `id = 2785` and `diary_number = '0002427/2026'`.
  - Updated `tbl_complain_disposal` set `disposal_type_id = 5`, `disposal_reason_id = 14` where `complain_id = 2785` and `id = 787`.
- Correction reason: Complaint was mistakenly marked as "Closed (Sub-Judice)"; corrected to "Non-Monetary (with Direction)" with updated disposal type and reason.
- Queries reviewed and approved by Rohan Ahmed.

**3. Sindh DynamoDB Table Cleanup:**
- Deleted specified tables from DynamoDB in Sindh project as requested by Izza.
- Performed cleanup after obtaining approval from Hazar.

**4. Nova Via App Service Stack Deployment:**
- Added code to update app service stack to enable JWT value retrieval for Afifa.
- Changes approved by Hazar, merged into main branch.
- Successfully deployed stack to AWS in Nova via project.

**5. Environment Variable Updates:**
- Followed up on environment variable MR created last Friday (dev.yaml and prod.yaml changes).
- Obtained Hazar's approval and merged changes into main branch.

**6. Certificate Stack Provisioning:**
- Inquired with Hazar about proceeding with certificate stacks task.
- Awaiting approval before proceeding.

---

## 📚 Training & Professional Development

No formal training sessions today; focus was on infrastructure operations and cross-functional collaboration.

---

## 🎯 Cross-Functional Collaboration & Operations

**1. Database Operations Coordination:**
- Coordinated with Khurrum and Rohan Ahmed on Sindh database query execution and approval.

**2. DynamoDB Cleanup:**
- Coordinated with Izza on table deletion requirements and Hazar for approval.

**3. Nova Via Stack Deployment:**
- Collaborated with Afifa on app service stack changes for JWT value retrieval.
- Ensured proper approval workflow with Hazar before merging and deploying.

**4. Environment Variable Management:**
- Followed up on pending MR for environment variable additions.
- Coordinated with Hazar for approval and merge into main.

**5. Certificate Stack Planning:**
- Coordinated with Hazar on timing and approval for certificate stack provisioning task.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Continued Nova project infrastructure configuration (wildcard SSL, CloudFront, ALB).
- ✅ Executed approved Sindh database correction queries.
- ✅ Performed DynamoDB table cleanup for Sindh project.
- ✅ Deployed Nova via app service stack changes for JWT retrieval.
- ✅ Merged environment variable updates (dev.yaml, prod.yaml) into main.
- ✅ Coordinated on certificate stack provisioning task.

**Key Learnings:**
- Database corrections require proper approval workflows and precise query execution to maintain data integrity.
- DynamoDB table cleanup should follow approval protocols to prevent accidental data loss.
- App service stack changes for JWT handling require careful implementation and testing before deployment.

**Next Steps:**
1. Await Hazar's approval to proceed with Nova project infrastructure deployment.
2. Proceed with certificate stack provisioning upon approval.
3. Monitor deployed Nova via app service stack for JWT functionality.
4. Continue AWS troubleshooting course modules.
