<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Onboarding & Operations — 2026-01-29</h3>

---

## 🎯 Objective
Summarize onboarding meetings (Sindh, TBS, NGAGE), operational monitoring tasks assigned, access changes completed, and the training session attended.

---

## 💡 Summary
- Met with Umair for a detailed onboarding walkthrough of **Sindh**, **TBS**, and **NGAGE** projects; clarified scope, contacts, and documentation.
- Assigned to monitor **Sindh** logs/metrics during a deployment (Khurrum); no incidents observed.
- Granted **CloudFront (read-only)** access to Izza and verified permissions.
- Attended a **self-organization** onboarding session led by Waleed.

---

## 🗓 Meetings

### 1) Onboarding session with Umair
**Purpose:** Project onboarding and gap review for Sindh/TBS/NGAGE

**Outcomes:**
- Project scopes and immediate priorities clarified
- Key contacts and repositories identified for each project
- Missing documentation items noted and assigned for follow-up

**Action items:**
- Verify repository and documentation access (Tehsindh, TBS, NGAGE)
- Schedule technical deep-dive if required

---

## ⚙️ Operational Tasks

### 2) Monitoring assignment — (Assigned by Khurrum)
**Task:** Monitor **Sindh** CloudWatch logs and metrics during deployment

**What I checked:**
- CloudWatch metric graphs (CPU, memory, latency)
- Application log groups for error traces
- Health checks and alarms

**Status:** No errors or anomalies observed during deployment. Metrics remained within expected thresholds.

**Recommendations:**
- Add CloudWatch alarms for ErrorRate and p95 latency (if missing)
- Consider a small runbook for on-call alert responses for Sindh

---

### 3) CloudFront Access for Izza
**Request:** Read-only access to CloudFront distributions

**Action taken:**
- Created/attached read-only IAM permissions for Izza
- Verified `ListDistributions` and `GetDistributionConfig` operations succeed for her role

**Evidence:**
- Add a screenshot of the IAM assignment and Izza's successful console view (store in `images/`)

---

## 📚 Training & Onboarding

### 4) Self-organization session — Waleed
**Topic:** Self-organization and team onboarding practices

**Outcome:** Learned improved note-taking, documentation standards, and handoff best practices. Plan to apply these to project READMEs.


---

**Author:** Sufi Hassan Asim  
**Date:** 2026-01-29

