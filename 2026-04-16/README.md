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

Learning / Upskilling

Continued progress on AWS training courses during available time while waiting on dependency/blocker:
 
and after  that updated hazar by asking him if tehre is anything he want me to do today 

and in teh mean time i prepared for my checkpoint which was shifted to today 16 april 

tehn i did a lot of reserch for the MM-enterprise qa pipeline even though teh pipoelien is successful tehre are teh isssue of the ui resources not being displayed on the apps url 
 What we checked (short version)
Network/infra is healthy: ALB, Cloudflare, EC2 all return 200 OK
JS assets (_next/static/*) load correctly
cf-cache-status = BYPASS → no CDN caching issue
No missing files or 404s in build output
Browser shows:
#__next = null
window.__NEXT_DATA__ = undefined

 What that means

Next.js is not hydrating the page at all.

That only happens when:

The HTML served is not a valid Next.js SSR output, or
The app is returning a fallback / incorrect server response, so React never boots.

So the JS loads, but the actual React app never initializes.

afterthat i was onboarded into a new task to make teh automation pipeine etc 
but right after that i was let go of the position and asked to off board from teh projects i am working on and submit the laptop and stuff to faizan 
