<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Nova Project Infrastructure, Claude Review Research & AWS Troubleshooting — 2026-03-13</h3>

---

## 🎯 Objective
Complete Nova project infrastructure mirroring (Wildcard SSL, CloudFront, ALB); research `claude_review` and demo repository; continue AWS troubleshooting training; attend onboarding session; manage production environment disk space and security inquiries.

---

## 💡 Summary
Finalized infrastructure changes for the Nova project, including wildcard certificates and SSL configurations for the portal, API, and video CDN, and submitted the merge request. Conducted research and set up a demo repository for `claude_review`, though full testing was limited by API credits. Attended an onboarding session on Islamic Business Practices. Proactively managed production security by advising against sharing secrets in chat and monitored a critical disk space issue on the production environment, coordinating with leadership for a resolution to prevent deployment failures.

---

## 🚀 Development & Infrastructure Operations

**1. Nova Project Infrastructure Mirroring:**
- Configured wildcard certificates for domain `novalifeapp.com`.
- Implemented custom domain and SSL on CloudFront for `portal-dev.novalifeapp.com`.
- Configured custom domain and SSL on video CDN CloudFront for `video-cdn-dev.novalifeapp.com`.
- Configured custom domain and SSL on Application Load Balancer (ALB) for `api-dev.novalifeapp.com`.
- Followed Rahbar project CI/CD implementation as a reference for mirroring logic.
- Submitted Merge Request (MR #11) to Hazar for review: [gitlab.dplit.com/nova-via/cicd/-/merge_requests/11](https://gitlab.dplit.com/nova-via/cicd/-/merge_requests/11).

---

## 📚 Training & Professional Development

**1. Claude Review Research:**
- Researched `claude_review` tool and established a demo repository for testing.
- Successfully set up the environment and configuration.
- Full testing was restricted by lack of API credits, but the initial setup was successful.

**2. AWS Troubleshooting Course:**
- Continued watching the troubleshooting course modules started previously.
- Focused on deepening diagnostic skills and methodology for cloud environments.

**3. Onboarding Session:**
- Attended the "Islamic Business Practices" onboarding session conducted by Saad.

---

## 🎯 Cross-Functional Collaboration & Operations

**1. Security Best Practices:**
- Addressed an inquiry regarding secret values by advising the team member to fetch them directly from AWS Secrets Manager.
- Reinforced that sharing secrets in chat is not a best practice to maintain system security.

**2. Production Monitoring & Incident Management:**
- Investigated production environment disk space following a query from Khurrum.
- Confirmed that previous changes to increase disk space were not applied to production.
- Identified that disk space is currently 90% full.
- Escalated the situation to Hazar to obtain approval for necessary changes, ensuring upcoming production deployments do not fail.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Finished Nova project infrastructure changes (SSL, CloudFront, ALB).
- ✅ Submitted MR #11 for Nova via CICD for review.
- ✅ Researched `claude_review` and configured demo repository.
- ✅ Attended Islamic Business Practices onboarding session.
- ✅ Provided guidance on secure secret retrieval via Secrets Manager.
- ✅ Monitored production disk space and escalated capacity issues.

**Key Learnings:**
- Infrastructure mirroring requires precise synchronization of certificates and SSL settings across diverse services like CloudFront and ALB.
- Maintaining security protocols, such as discouraging secret sharing in chat, is critical for organizational integrity.
- Proactive capacity monitoring of production resources (e.g., disk space) is essential to ensure deployment reliability.

**Next Steps:**
1. Follow up on the Nova project MR review and address any feedback.
2. Resolve API credit issues to complete the `claude_review` testing phase.
3. Complete the remaining modules of the AWS troubleshooting course.
4. Monitor the production disk space resolution and support the upcoming production deployment.
