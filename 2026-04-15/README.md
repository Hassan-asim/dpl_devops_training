<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • MM-Enterprise QA Pipeline, Checkpoint Presentation & CSP Troubleshooting</h3>

---

## 🎯 Objective Recap
- Continue MM-Enterprise QA pipeline follow-up and confirm environment fix status.
- Prepare and validate the checkpoint presentation for today.
- Continue AWS training while waiting on blockers.
- Document troubleshooting steps for the CSP eval error and PM2 process issue.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **Projects:** MM-Enterprise QA pipeline, DynamoDB local practice app, AI SDLC research
- **Artifact:** `DevOps-Training-Progress-Checkpoint-2.pptx`

---

## 📚 Notes & Key Learnings

### 1. MM-Enterprise QA Pipeline Follow-up
- Basit confirmed and applied the `.env` source path correction.
- The pipeline is now showing: Build Stage fixed and working, Deploy Stage fixed and working.
- The next step is to connect with Basit on the production pipeline task under his supervision.

### 2. AWS Training / Upskilling
- Continued progress on AWS Skill Builder:
  - Amazon DynamoDB – Troubleshooting course (in progress)
  - AWS Cloud Practitioner course (in progress)
- Used available time to keep learning while waiting on the remaining dependency/blocker.

### 3. Local DynamoDB Practice App
- Built a local runnable e-commerce version to mimic DynamoDB operations without AWS deployment.
- Verified local testing flows and DynamoDB-like process handling while AWS account access is unavailable.

### 4. Checkpoint Presentation Preparation
- Created the actual checkpoint PPT and validated it multiple times.
- Ensured content is accurate, fact-checked, and free of misleading information.
- Presentation is prepared for today.

### 5. Guide to Fix Eval Error
- Created a comprehensive guide: `guide to fix the eval error.md`
- **Topic:** Fixing Content Security Policy (CSP) issues that prevent JavaScript execution and cause apps to load without styling.
- **Content Covers:**
  - Problem identification (`unsafe-eval` browser error)
  - Root cause analysis (strict CSP blocking React/Next.js hydration)
  - Step-by-step fixes for NGINX, Next.js config, and Cloudflare
  - Temporary and production-ready solutions
- **Purpose:** Troubleshooting guide for deployment and styling issues in web applications.

### 6. Server Research and PM2 Debugging
- Researched the issue further and updated Basit on the findings.
- Connected to EC2 `i-06bac72aea44abbd4` (`mm-dev`) to inspect runtime state.
- Observed `pm2 list` output indicating the daemon started but the process list is not synchronized with the saved list.
- Noted this as the main anomaly and will continue investigation tomorrow.
- Additional research confirmed that CSS is loading successfully with 200 status, and the eval error is the primary issue.
- Communicated findings to Basit via message, highlighting the eval error as the key anomaly and providing PM2 status details.

### 7. AI SDLC Research
- Started initial research on AI software development lifecycle topics.
- Preparing notes for today’s checkpoint discussion and future AI integration planning.

---

## 📋 Action Items & Timeline

### Completed Today
- ✓ Confirmed Basit's `.env` path fix and pipeline validation.
- ✓ Built and tested the local DynamoDB practice app.
- ✓ Created and validated the checkpoint presentation.
- ✓ Created the CSP eval error troubleshooting guide.
- ✓ Investigated the mm-dev PM2 status and server environment.

### Pending
- ⏳ Follow up on mm-dev app resource loading and `node-env` error.
- ⏳ Continue AWS Skill Builder courses.
- ⏳ Deliver the checkpoint presentation.
- ⏳ Continue AI SDLC research after the checkpoint.

### Key Notes
- Basit’s `.env` fix is completed and the pipeline is working again.
- Local DynamoDB app covers practice testing until AWS access is restored.
- Checkpoint presentation is ready and fact-checked.
- PM2 synchronization issue on EC2 remains under investigation.
- AI SDLC research is in progress for long-term improvement.
