# DevOps Training Progress Report - Checkpoint 2
**Name:** Sufi Hassan Asim  
**Period:** February 9, 2026 - April 10, 2026  
**Checkpoint Date:** April 10, 2026  
**Next Checkpoint:** Week of April 17, 2026  

---

## 📋 Executive Summary

This report covers the work completed and progress made since my last checkpoint on **January 2026**. During this period, I have been actively involved in multiple DevOps projects including CI/CD pipeline management, cloud infrastructure operations, Miracle Morning GitLab migration, and cross-team collaboration. I have also focused on improving my communication and collaboration skills based on feedback from my previous checkpoint.

---

## 🔙 Previous Checkpoint Overview (Brief Context)

In my last checkpoint (January 2026), I focused on:
- FBR Digital Invoicing Project - API testing, integration, and production application design
- AWS Cloud Architecture - VPC infrastructure, ECS Fargate services, GitLab CI/CD pipelines
- High Availability & Disaster Recovery - Multi-AZ architecture with monitoring and backup
- Full-Stack Cloud Architecture - Deployed three-tier architecture with React frontend and NestJS backend
- Sindh Ombudsman CMS onboarding and production issue research
- The Breath Source (TBS) project onboarding and microservices documentation
- NGAGE project onboarding

**Key Feedback Received:**
- Need to improve communication with team members
- Should proactively share progress updates
- Required more active collaboration on tasks

---

## 🎯 Key Achievements Since Last Checkpoint (Feb 9 - Apr 10, 2026)

### 1. **CI/CD Pipeline Development & Troubleshooting**

**Duration:** February 20 - April 8, 2026

**Key Accomplishments:**

#### a) Sindh Frontend Pipeline Fixes (Feb 20)
- Fixed dependency errors across DEV, UAT, PROD pipelines
- Upgraded Node.js from v18 to v20
- Added clean dependency installation (`rm -rf node_modules`)
- Implemented build caching for faster deployments
- Added pre_build phase for better organization

#### b) Pipeline Timeout Resolution (Mar 6)
- Identified frontend deployment timeout issue (300s insufficient)
- Increased timeout to 600s
- Learned lesson about applying changes to correct repository

#### c) Disk Space Issue Resolution (Mar 9)
- Identified disk space nearly full as root cause of deployment failures
- Implemented disk space increment solution (30GB EBS GP3 volumes)
- Applied fix based on Hazar's previous DEV solution

#### d) CodeBuild Environment Update (Apr 8)
- Updated CodeBuild to Standard 6 image for Node v20 support
- Ensured compatibility with latest Node.js versions

#### e) Lambda CDK Pipeline
- Developed auto-deploy pipeline for Lambda CDK repo
- Encountered deployment failures at deploy stage
- Ultimately deleted pipeline and developed new pipeline code (under review)

---

### 2. **Sindh Ombudsman CMS Project Operations**

**Duration:** February 12 - March 24, 2026

**Production Database Operations:**
- Executed numerous approved queries on Sindh production RDS for data correction, reporting, and maintenance
- Always followed approval chain (Rohan, Ali Imran, Salman)
- Updated **10 escalation queries** on production database improving:
  - Business day calculations
  - Duplicate prevention
  - Complaint type filtering
  - NULL handling

**Infrastructure & Lambda Work:**
- Deployed Lambda and SQS stacks to PROD for notification logic (Feb 27)
- Configured 3 new Lambda function name environment variables in DEV backend (Mar 2)
- Investigated and resolved Lambda function errors in UAT and PROD caused by missing DynamoDB table resource attachments in IAM policies (Mar 19-24)
- Deleted specified tables from DynamoDB after obtaining approvals (Mar 16)

**Daily Operations:**
- Performed infrastructure monitoring: CloudFormation, CloudFront, EC2, ECS, ALB, target groups, CI/CD pipelines

---

### 3. **Miracle Morning (MM) Project - CodeCommit to GitLab Migration** ⭐ Major Project

**Duration:** April 1 - April 7, 2026

**Migration Scope:** 5 repositories (mm-backend, mm-enterprise, mm-cms, mm-event, mm-checkout)

**What I Accomplished:**

#### a) Migration Planning & Setup (Apr 1-2)
- Created comprehensive migration plan for all 5 repositories
- Created all GitLab repositories with main branches
- Researched AWS CodeStar Connections for GitLab self-managed integration

#### b) Connection Establishment (Apr 3)
- Successfully established AWS GitLab connection using access token
- Resolved 403 error through collaboration with Ali

#### c) Pipeline Migration (Apr 3-7)
- **mm-backend (PROD):** Completed and verified
- **mm-event:** Completed, required node_modules cleanup
- **mm-checkout:** Completed by Basit
- **mm-cms:** Completed, configured VITE_* environment variables
- **mm-enterprise:** Required CodeBuild image update to Standard 6 for Node v20

#### d) IAM Fix (Apr 7)
- Resolved GitLab connection issue by adding `codestar-connections:UseConnection` permission to IAM role

#### e) Documentation
- Created two comprehensive guides for dev team:
  - **SSM Parameter Store based .env management**
  - **Multi-EC2 single-master variable automation**

---

### 4. **Nova Via / NovaLife Project**

**Duration:** March 4 - April 8, 2026

**Key Contributions:**

#### a) Infrastructure Mirroring (Mar 13-17)
- Configured wildcard certificates
- Set up custom domain SSL on CloudFront:
  - `portal-dev.novalifeapp.com`
  - `video-cdn-dev.novalifeapp.com`
- Configured ALB: `api-dev.novalifeapp.com`

#### b) CloudFront Signed Cookies Fix (Mar 4)
- Resolved signed cookies rejection issue
- **Root cause:** Private key stored as binary secret but fetched as plain string
- Validated end-to-end using CloudShell with base64 decode, OpenSSL verification, and Python cryptography for cookie generation

#### c) S3 Permission Fix (Mar 30)
- Added s3:PutObject permission to app service task role
- Created MR #18

#### d) App Service Stack & ECS
- Deployed changes for JWT value retrieval
- Resolved environment variable accessibility issues
- Added dedicated CloudWatch Log Group for complaint audit logs in ecs-service.ts (Apr 1, Apr 8)
- Created MR for review

#### e) Secrets Management
- Updated ElevenLabs webhook/secret values multiple times
- Updated ECS task definitions to consume new secrets
- Approved secret stack approach discussed with Hazar

---

### 5. **AWS Training & Professional Development** 📚

**Continuous Learning Throughout Period:**

| Course | Platform | Status | Date |
|--------|----------|--------|------|
| AWS for Beginners with Hands-on Labs | KodeKloud | In Progress | Feb 25 - Mar |
| Amazon Elastic Block Store Troubleshooting | AWS Skill Builder | ✅ Completed | Mar 25 |
| Troubleshooting: Amazon ECS | AWS Skill Builder | ✅ Completed | Apr 7 |
| Troubleshooting: Amazon DynamoDB | AWS Skill Builder | In Progress | Apr 7 - Present |
| AWS Cloud Quest Cloud Practitioner | AWS Skill Builder | In Progress (Assignments 1-2 completed) | Mar 30 - Present |
| Terraform Fundamentals | Self-study | Learned init/plan/apply workflow | Mar 5 |

**Hands-on Experiments:**
- **AWS SAM/CloudFormation Experiments (Mar 25-26):**
  - Experiment 1: IAM policy overwrite behavior
  - Experiment 2: No-change deployment
  - Experiment 3: Existing role conflicts
  - Experiment 4: CLI vs console consistency

- **EC2 Reserved Instance Strategy (Mar 27):**
  - Developed comprehensive RI purchasing plan with 4 strategy options
  - Recommended two consecutive 1-year All-Upfront RIs

- **db-bastion EC2 Automation Planning (Mar 30-31):**
  - Developed automation plan for EC2 lifecycle management
  - Stop at midnight PKT, start at 9 AM PKT
  - Used CDK + EventBridge + SSM Automation with AWS-managed runbooks
  - Refined approach based on Hazar's feedback

---

### 6. **Cross-Functional Collaboration & Team Support**

**Team Collaboration:**
- Assisted team members (Afifa, Khurrum, Daniyal, Salman, Izza, Basit) with troubleshooting and infrastructure tasks
- Onboarded new DevOps team member (Hazaifa/Huzaifa) on CDK structure and CloudWatch logs implementation
- Attended checkpoint feedback meetings with Muneeb

**Training & Onboarding Sessions Attended:**
- Scrum (Parts 1-2)
- Career Growth
- Islamic Business Practices
- DPL Marketing Strategy
- Communication/Interpersonal Influence
- REBEL Speaker sessions
- All-hands meetings

---

## 📢 Communication & Collaboration Improvements

**Addressing Previous Checkpoint Feedback:**

Based on feedback that I needed to improve communication, I made conscious efforts to:

### ✅ What I Improved:

1. **Regular Progress Updates:**
   - Started updating the cloud team group about my progress and next plans
   - Shared daily/weekly status updates via group messages
   - Used DMs and in-person communication more frequently with Hazar

2. **Proactive Task Communication:**
   - Asked team if they had additional tasks for me while waiting on dependencies
   - Communicated blockers and dependencies clearly (e.g., waiting on Basit for pipeline fix)
   - Shared learning progress and upskilling activities

3. **Active Collaboration:**
   - Worked directly with team members on tasks:
     - Collaborated with **Ali** to resolve GitLab 403 error
     - Worked with **Basit** on pipeline migration and planning production pipeline work
     - Supported **Huzaifa** (new hire) with CloudWatch logs MR queries
   - Participated in code reviews and MR approvals

4. **Documentation:**
   - Created comprehensive guides for the team (SSM Parameter Store, Multi-EC2 automation)
   - Maintained daily progress documentation in training folders
   - Documented migration plans and troubleshooting steps

### 🔄 Areas for Further Improvement:

- **More frequent check-ins:** Could benefit from scheduled regular check-ins rather than ad-hoc updates
- **Proactive problem-solving:** Should escalate blockers earlier rather than waiting
- **Meeting participation:** Could contribute more actively in team meetings
- **Knowledge sharing:** Should share learnings and solutions more broadly with the team

---

## 🛠️ Current Status & Pending Items

### Active Tasks:

| Task | Status | Dependency | Next Steps |
|------|--------|------------|------------|
| MM-Enterprise QA Pipeline | ⏳ Pending | Waiting for Basit | Environment path correction and re-run pipeline |
| Production Pipeline Work | ⏳ Planned | After QA pipeline fix | Work with Basit under supervision |
| AWS DynamoDB Troubleshooting Course | 🔄 In Progress | Self-paced | Complete remaining modules |
| AWS Cloud Practitioner Course | 🔄 In Progress | Self-paced | Continue assignments |
| Lambda CDK Pipeline | 🔄 Under Review | Team review | Await feedback and finalize |
| MM-Enterprise Pipeline (GitLab) | ✅ Working | None | Monitor and maintain |

### Completed Recent Work (April 10, 2026):

- ✓ Followed up on QA pipeline status (still pending .env fix)
- ✓ Progressed on AWS training courses
- ✓ Updated cloud team on progress and requested additional tasks
- ✓ Supported new hire (Huzaifa) with CloudWatch logs MR queries

---

## 📊 Metrics & Impact Summary

| Category | Metric | Value |
|----------|--------|-------|
| **Cost Optimization** | Reserved Instance Planning | 27% savings with 1-year RI |
| **Infrastructure** | Repositories Migrated | 5 (CodeCommit → GitLab) |
| **Pipelines** | CI/CD Pipelines Fixed/Deployed | 8+ across multiple projects |
| **Training** | AWS Certificates Earned | 2 (EBS Troubleshooting, ECS Troubleshooting) |
| **Training** | Courses In Progress | 3 (DynamoDB, Cloud Practitioner, Cloud Quest) |
| **Collaboration** | Team Members Supported | 7+ (Ali, Basit, Salman, Huzaifa, etc.) |
| **Documentation** | Guides Created | 2 comprehensive team guides |
| **Production** | Database Queries Executed | 20+ (all approved) |

---

## 🎯 Next Week Plan (April 17-24, 2026)

### Priority 1: Complete Pending Tasks
- [ ] Follow up with Basit on MM-Enterprise QA pipeline .env fix
- [ ] Collaborate with Basit on production pipeline work (post-QA fix)
- [ ] Complete Lambda CDK pipeline based on review feedback

### Priority 2: Training Completion
- [ ] Finish AWS DynamoDB Troubleshooting course
- [ ] Complete AWS Cloud Practitioner assignments
- [ ] Start advanced ECS/EKS troubleshooting course

### Priority 3: New Tasks & Initiatives
- [ ] Request additional tasks from cloud team
- [ ] Propose db-bastion EC2 automation implementation
- [ ] Support any production deployments or migrations
- [ ] Assist new team members with onboarding

### Priority 4: Communication Goals
- [ ] Schedule regular check-ins with Hazar (2-3x per week)
- [ ] Share daily progress updates in cloud team group
- [ ] Propose knowledge-sharing session on GitLab migration learnings
- [ ] Document and share troubleshooting guides

---

## 💡 Key Learnings & Takeaways

### Technical Learnings:
1. **CI/CD Pipeline Management:** Deep understanding of CodeBuild, CodePipeline, and GitLab integrations
2. **Troubleshooting:** Systematic approach to identifying and resolving infrastructure issues
3. **IAM Policies:** Critical importance of proper permissions in Lambda/DynamoDB integrations
4. **CloudFront & SSL/TLS:** Hands-on experience with signed cookies, custom domains, and certificate configuration
5. **Cost Optimization:** Practical experience with Reserved Instances and infrastructure right-sizing

### Soft Skills Learnings:
1. **Communication is Key:** Proactive updates prevent misunderstandings and build trust
2. **Collaboration Accelerates Learning:** Working with seniors (Basit, Ali, Hazar) fast-tracked problem-solving
3. **Documentation Matters:** Creating guides helps both the team and personal understanding
4. **Asking for Help is Strength:** Reaching out when blocked is better than struggling silently

---

## 🙏 Acknowledgments

- **Hazar:** For guidance, task assignments, and feedback on communication
- **Basit:** For collaboration on pipeline work and planned supervision
- **Ali:** For help with GitLab connection troubleshooting
- **Muneeb:** For checkpoint feedback and continuous improvement guidance
- **Cloud Team:** For collaboration and knowledge sharing
- **Huzaifa:** For engaging in knowledge exchange during onboarding

---

## 📝 Self-Reflection

Since my last checkpoint, I have made significant progress both technically and in terms of communication. I've worked on multiple high-impact projects including the Miracle Morning GitLab migration, resolved critical production issues, and contributed to team documentation.

**What went well:**
- Completed GitLab migration for MM project (5 repositories)
- Resolved multiple production issues (Lambda, CloudFront, S3 permissions)
- Improved communication frequency and quality
- Supported team members and new hires
- Created comprehensive documentation for the team

**What needs improvement:**
- Could be more proactive in seeking out new tasks
- Should escalate blockers earlier
- Need to contribute more in meetings
- Should share knowledge more systematically

**Commitment for Next Checkpoint:**
I am committed to continuing my technical growth while further improving my communication, collaboration, and proactive engagement with the team.

---

**Report Prepared By:** Sufi Hassan Asim  
**Date:** April 10, 2026  
**Next Checkpoint:** Week of April 17, 2026
