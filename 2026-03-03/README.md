<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Deployment Error, Env Variables & Secrets — 2026-03-03</h3>

---

## 🎯 Objective
Review AWS training material, diagnose and resolve a frontend deployment error in the Sindh project, collaborate on environment variable changes across CI/CD and EC2 instances, update ElevenLabs webhook secrets, and attend a speaker session.

---

## 💡 Summary
Watched additional modules of the KodeKloud AWS for Beginners course. Investigated an admin frontend deployment failure in the Sindh project, identified missing `fix_permission.sh` script and coordinated with Hazar to resolve the issue; retried pipeline which surfaced another error (Hazar agreed to handle). Added three new configuration variables in the CICD repository per Khurrum's request, then submitted a merge request to update backend EC2 environment variables (DEV, UAT, PROD); after review the change was deemed unnecessary and the dev team was advised to hard‑code the values since they will not change. Updated ElevenLabs webhook secret value with Hazars approval at Afifa’s request, and notified Afifa when complete. Finished the day by attending the rebel speaker session.

---

## 🚀 Development & Infrastructure Operations

**1. Sindh Admin Frontend Deployment Troubleshooting:**
- Received report of deployment error during pipeline run.
- Diagnosed root cause: missing `fix_permission.sh` script in deployment artifacts.
- Communicated findings to Hazar and the project group.
- Collaborated with Hazar on a fix; retried the pipeline which revealed a new error.
- Hazar elected to apply the subsequent fix himself.

**2. Environment Variable Requests:**
- Khurrum requested three new AWS variables and their values for use in code.
- Implemented required changes in the `cicd` sub‑repository and opened a merge request.
- Also proposed adding the variables on backend EC2 instances (DEV, UAT, PROD) via MR.
- Hazar reviewed and concluded the variables should be handled directly in the application code since their values are static.
- Conveyed decision to the development team accordingly.

**3. ElevenLabs Webhook Secret Update:**
- Afifa asked for the ElevenLabs webhook secret value to be updated.
- Obtained Hazar’s approval, performed the change, and confirmed with Afifa.

---

## 📚 Training & Professional Development

**AWS for Beginners (KodeKloud):**
- Continued watching course material provided by Hazar (same module link as previous days).

**Speaker Session:**
- Attended the rebel speaker session later in the day.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Continued KodeKloud AWS training.
- ✅ Investigated and reported Sindh admin frontend deployment error.
- ✅ Collaborated with Hazar to resolve deployment issues.
- ✅ Handled environment variable change request and subsequent review.
- ✅ Updated ElevenLabs webhook secret as requested by Afifa.
- ✅ Attended rebel speaker session.

**Next Steps:**
1. Follow up with Hazar for status of remaining deployment error fix.  
2. Inform developers to implement the three configuration values in code.  
3. Continue AWS training modules.  
4. Monitor Sindh pipeline for any recurrence of the error.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-03-03
