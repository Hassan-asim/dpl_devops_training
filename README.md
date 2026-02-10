# dpl_devops_training

This repository now tracks my DevOps practice in **date-wise folders** so you can review each day's progress, artifacts, and supporting documents in one place. I'll continue to mirror this structure for future evaluations and test projects you share in the same folders.

## 📂 Repository Structure

- `YYYY-MM-DD/` – A dedicated folder for that day's work. Each contains:
  - `README.md` – the full daily report (study log, challenges, fixes, screenshots).
  - `images/` – screenshots embedded in the daily README.
  - Any practice assets (`user-data`, `meta-data`, `seed.iso`, scripts, etc.).

### Available Logs

| Date       | Highlights                                                          |
|------------|---------------------------------------------------------------------|
| 2026-02-09 | **EC2 Architecture Analysis & Monthly Progress Checkpoint:** Conducted comprehensive t3a (x86) vs t4g (ARM/Graviton) instance comparison; created detailed EC2 Instance Selection Justification Report; developed phased migration strategy ($380/mo t3a-only, $367/mo hybrid, $301/mo full-Graviton); attended monthly checkpoint meeting and presented progress accomplishments. |
| 2026-02-06 | **EC2 Cost Optimization & Sindh Production Operations:** Updated EC2 cost analysis spreadsheets with RFP-compliant instance recommendations (total $380/mo with 1yr reserved pricing); executed production database queries; monitored CodePipeline deployments; updated S3 configuration templates for Sindh infrastructure. |
| 2026-02-04 | **Complete Firebase Secret Integration:** Implemented end-to-end Firebase secret management with AWS Secrets Manager across CDK infrastructure and application service repositories; deployed to dev account (471464546186); created SecretsStack and updated AppServiceStack with proper IAM permissions; resolved merge conflicts and submitted MR #37 for review. |
| 2026-02-03 | **Billing Automation Completion & Database Query Updates:** Finalized automated monthly billing report system with Lambda, SNS, and EventBridge integration; updated and optimized ADVISORS_REPORT and REGIONAL_ESCALATION_REPORT database queries; successfully tested end-to-end billing automation workflow with monthly triggers. |
| 2026-02-02 | **AWS Billing Automation & Access Management:** Created automated monthly Cost & Usage Report system with Lambda processing and SNS notifications for finance team; configured Bedrock access for Izza with full permissions; set up S3 bucket and Athena access via AWS Identity Center (SSO). |
| 2026-01-31 | **Sindh UAT Validation:** Ran Sindh UAT validation via SSO and verification queries (successful); awaiting Khurrum's sign-off to run the same verification on PROD. |
| 2026-01-30 | **Repo Review & DB SSO Tests:** Reviewed GitLab repos (Sindh/TBS/NGAGE) for structure/CI/CD and tested Sindh DB SSO + verification queries successfully; added documentation action items. |
| 2026-01-29 | **Onboarding & Monitoring:** Onboarded to Sindh/TBS/NGAGE; monitored Sindh during a deployment (no incidents); granted CloudFront read-only access to Izza; attended self-organization session. |
| 2026-01-28 | **TBS Health Review & Ngage Onboarding:** Reviewed TBS health logs and ECS/Fargate service responsibilities; reported status to Ali Bhai; attended initial Ngage onboarding with Umair Bhai; continuing to learn project structure and CI/CD flows. |
| 2026-01-27 | **429 Error Investigation & The Breath Source Onboarding:** Identified root cause of 429 "too many requests" errors in production: lack of connection pooling causing idle connection pile-up on PostgreSQL RDS instance (max_connections = 838); reviewed application code, examined production configuration, used AWS SSM for secure database access; documented recommendations for connection pooling implementation and coordination with Ali Bhai for credentials; onboarded to new project "The Breath Source" with UmSir. |
| 2026-01-26 | **Sindh Ombudsman CMS Project Onboarding & SonarQube Configuration:** Completed initial onboarding for Sindh Ombudsman CMS project with Khurrun Bhai; reviewed GitLab repositories (sindh-ombudsman-cms and cicd); analyzed SonarQube code quality issues with duplicate line violations exceeding 3% threshold; identified action items for SonarQube configuration updates; discussed deployment configurations and CI/CD pipeline optimization; requested SonarQube credentials to update duplicate line threshold from 3% to 3.3%. |
| 2026-01-23 | **FBR Production Application Development & AWS Networking Certification:** Developed production-ready Streamlit-based FBR Digital Invoicing application with professional UI, secure API integration, automated setup scripts, and comprehensive user experience; completed AWS Networking Basics certification and Cursor AI course; application ready for immediate deployment with DPL Finance team. |
| 2026-01-22 | **FBR API Integration Testing & Production Token Resolution:** Conducted comprehensive FBR API testing, completed all DPL-assigned scenarios (SN018, SN019), generated 6 valid invoices, analyzed 51-page FBR documentation, developed automated testing scripts, and prepared evidence package for production token escalation; technical integration fully complete and production-ready. |
| 2026-01-21 | **DPL FBR Integration Planning & Documentation:** Developed comprehensive FBR (Federal Board of Revenue) integration plan with technical specifications, implementation roadmap, and compliance framework; created detailed documentation covering API integration, data validation, security requirements, and regulatory compliance; complete planning documents saved to `2026-01-21/`. |
| 2026-01-20 | **Task 5: Full-Stack Cloud Architecture:** Implemented production-ready three-tier architecture with React frontend (S3/CloudFront), NestJS backend (ECS Fargate), PostgreSQL database (RDS Multi-AZ), comprehensive CI/CD pipeline (GitLab→CodeBuild→ECR→ECS), security (IAM/Secrets Manager), and monitoring (CloudWatch/X-Ray); complete implementation checklist and database connectivity verification saved to `2026-01-20/images/`. |
| 2026-01-19 | **AWS Skill Builder Labs & Cloud Practitioner Certification:** Completed AWS Cloud Practitioner certification and four hands-on labs: Auto-Healing and Scaling Applications, Connecting VPCs, Core Security Concepts, and Highly Available Web Applications; all certificates and lab completion evidence saved to `2026-01-19/images/`. |
| 2026-01-16 | **Task 4: High Availability, Disaster Recovery & Cost Optimization:** Implemented production-ready, highly available infrastructure with disaster recovery capabilities and cost optimization strategies using AWS CDK; Multi-AZ deployment for RDS, ECS, ALB, NAT Gateways; comprehensive monitoring with CloudWatch and backup strategies with AWS Backup; cost estimation and optimization recommendations documented in `2026-01-16/`. |
| 2026-01-15 | **Task 3: CICD Pipeline with AWS CDK for GitLab:** Implemented comprehensive end-to-end CI/CD pipeline using AWS CDK (TypeScript) with GitLab integration via CodeStar Connections, parallel frontend/backend builds via CodeBuild, S3 artifact storage, and CloudWatch logging; complete buildspec files and deployment documentation saved to `2026-01-15/`. |
| 2026-01-14 | **Task 1: NetworkingStack + Task 2: CICD Pipeline:** Implemented NetworkingStack (VPC with public/private/database subnets, IGW, NAT gateways, VPC endpoints for S3/ECR/CloudWatch) and CICD Pipeline (CodePipeline, CodeBuild integration, GitLab source); overcame CDK v2 compatibility issues and redeployed with 2 private/2 public subnet configuration; certificates and architecture diagrams saved to `2026-01-14/images/`. |
| 2026-01-13 | **AWS Skill Builder Labs Completion:** Completed four hands-on labs – Networking Concepts, File Systems in the Cloud, First NoSQL Database, and Cloud Economics; verified certificates and digital badges; lab completion screenshots and certificates saved to `2026-01-13/images/`. |
| 2026-01-12 | **Private EC2 w/ SSM (CloudFormation):** Built a CloudFormation template to deploy a fully private EC2 (no public IP/IGW/NAT) plus VPC interface endpoints for SSM/SSMMessages/EC2Messages, IAM role and security groups; verified SSM start-session and saved evidence to `2026-01-12/images/`. |
| 2026-01-09 | **AWS Systems Manager (SSM) & EC2 logs automation:** Completed AWS Systems Manager course and implemented an SSM automation to upload EC2 logs to S3; verified logs in `2026-01-09/ec2-logs-20260108-083729/` and evidence in `2026-01-09/images/`. |
| 2026-01-08 | **Cloud Computing + Labs:** Completed Cloud Computing Essentials and lab exercises (Cloud First Steps & Computing Solutions labs); certificates and lab evidence saved in `2026-01-08/images/`. |
| 2026-01-07 | **Certifications completed:** Completed four courses – Advanced Linux Commands; Configuration Management & Cloud; Development with Amazon Q; Google AI Essentials. All certificates and screenshots saved to `2026-01-07/images/`. |
| 2026-01-06 | **CDK course completed + EC2 website hosted:** Completed the CDK course and lab (`hello-cdk/`), launched an EC2-hosted static website with Nginx and Certbot (Let's Encrypt); Elastic IP allocated and associated – awaiting DNS A record propagation to finalize the certificate. Screenshots and evidence: `2026-01-06/images/`. |
| 2026-01-05 | **Static site deployed + DNS fix:** Added website code to `static-website/` and `static-website-with-domain.yaml`; uploaded screenshots to `2026-01-05/images/`; fixed site access issue by changing VPN DNS to a public resolver (1.1.1.1) and flushing cache – site now works on and off VPN. |
| 2026-01-02 | **Static site w/ domain:** Requested ACM certificate and deployed domain-backed static site using `static-website-with-domain.yaml`; DNS validation pending – artifacts in `2026-01-02/`. |
| 2026-01-01 | **Static site:** Deployed S3 + CloudFront via CloudFormation; added `static-website-cloudformation.yaml`, `index.html`, `error.html`, and screenshots/certificates in `2026-01-01/`. |
| 2025-12-31 | **PO task:** Implemented initial CloudFormation practice template (`AWSTemplateFormatVersion 2010-09-09.yaml`) and added supporting screenshots and certificates in `2025-12-31/images/`; daily report created in `2025-12-31/`. |
| 2025-12-30 | **Learned:** AWS Single Sign-On (IAM Identity Center) – read official docs and watched an in-depth YouTube video; notes in `2025-12-30/` (no images). |
| 2025-12-29 | **Certificates added:** EBS, EBS Performance Optimization, and Security Best Practices (PNG) saved in `2025-12-29/` – daily report created with evidence in `images/`. |
| 2025-12-26 | AWS course modules: **Auto Scaling**, **Block Storage**, **EC2 for Windows instance**, **OMT**, **Outpost Server**, and **Scale Out Computing**; screenshots added in `2025-12-26/` (images embedded in report). |
| 2025-12-24 | Continued AWS training: **AWS Build with EC2** and **AWS EC2 Basics**; captured part-wise screenshots and certificates in `2025-12-24/` (images embedded in report). |
| 2025-12-23 | Reviewed **AWS CSO** and **AWS EC2 (with lab)** courses; captured part-wise screenshots and certificates in `2025-12-23/` for evidence and reporting. |
| 2025-12-22 | Watched **~half** of the Amazon EC2 course (through Topic 6 – Launch Template); full course outline and video link added (`https://www.youtube.com/watch?v=4dscVzCaXCU`); no screenshots – planning hands-on labs next; details in `2025-12-22/` |
| 2025-12-19 | AWS architecture course Modules 6–10 completed with detailed part-wise screenshots; certificate of completion saved; evidence in `2025-12-19/` |
| 2025-12-18 | AWS architecture course Modules 2–5 completed with detailed part-wise screenshots; STS course fully completed with certificate; evidence in `2025-12-18/` |
| 2025-12-17 | New AWS architecture course started (parts 1–16) plus STS segment; Rebel Capture – DPL Webcam Prototype repo reviewed and app UI screens captured; evidence in `2025-12-17/` |
| 2025-12-16 | AWS security course completion milestone documented with certificate screenshot; evidence in `2025-12-16/` |
| 2025-12-15 | Deep Dive with Security: AWS IAM course started (46% complete); IAM lab theory + 14-step hands-on completed with certificate; evidence in `2025-12-15/` |
| 2025-12-12 | AWS Cloud Practitioner Essentials completed with certificate; Mastering AWS CDK completed with certificate; modules 10–13 evidence in `2025-12-12/` |
| 2025-12-11 | Video-only learning day: watched two YouTube sessions; skimmed *The Pragmatic Programmer* preface; no screenshots; evidence in `2025-12-11/` |
| 2025-12-10 | AWS Cloud Practitioner Essentials Module 9 completed; Module 10 started; Mastering AWS CDK – Coding Cloud Architectures Modules 6–8 completed; rewatched Kubernetes microservices video; evidence in `2025-12-10/` |
| 2025-12-09 | AWS Cloud Practitioner Essentials Modules 4–8 completed; Mastering AWS CDK Modules 4–5 completed; Kubernetes microservices fundamentals video (deployments, scaling, ingress); evidence in `2025-12-09/` |
| 2025-12-08 | AWS Cloud Practitioner Essentials Modules 1–4 completed; Mastering AWS CDK Modules 1–3 completed; AWS CLI profile configured and CDK installed |
| 2025-12-05 | Advanced TypeScript Types: Optional properties, custom types, literal types and unions, type narrowing, utility types (Partial, Omit), and generics with practical pizza restaurant examples |
| 2025-12-04 | TypeScript basics (handbook), watched practical TS tutorial and built a small TypeScript practice project; images and artifacts added in `2025-12-04/` |
| 2025-12-03 | TypeScript Fundamentals (Basic & Everyday Types), Modern JavaScript Coursera Course (Module 1 completed), Multi-Tenant Chatbot Architecture Research |
| 2025-12-02 | Trunk-Based Development deep dive, Git merge strategies (fast-forward vs --no-ff), rebase vs merge, Git workflows (Gitflow, GitHub Flow, forking), reflog/recovery theory |
| 2025-12-01 | Advanced Git: Internals, Merge/Conflicts, Diff/Stashing, Rebase, GitHub + PRs, plus Gitflow workflow practice (manual checkout alternative) |
| 2025-11-28 | SSH connectivity lab across dual Ubuntu VMs, Git fundamentals kickoff |
| 2025-11-27 | NGINX Complete Tutorial: Static Content, Mime Types, Location Context, Rewrites, Load Balancing with Docker |
| 2025-11-26 | Linux Essentials Chapters 12-14, NGINX installation & setup, 65 commands |
| 2025-11-25 | Linux Essentials Chapters 7-12, Ubuntu VM installation, AL2 CLI practice (70+ commands) |
| 2025-11-24 | AWS Cloud Technical Essentials, Linux CLI practice, AL2 VM attempt |
| 2025-11-21 | Amazon Linux 2 VirtualBox setup, cloud-init seed ISO, study summary |

navigate into the date folder you want to review—for example:

```
cd 2025-11-21
```

You'll find the detailed README plus every artifact referenced.

## 🔗 Latest Live Projects

- `2025-12-4` – Meeting Room Booker (live): https://room-booker-dpl.vercel.app/  
  Source code: https://github.com/Hassan-asim/room-booker-dpl

Visit the `2025-12-4/` folder for the daily report, screenshots, and a short project summary.

## 🔄 Next Steps

- I'll keep uploading new days exactly the same way.
- Feel free to drop evaluations or project briefs inside the relevant date folder; I'll respond in-place.

Let me know if you'd prefer a different naming scheme or extra metadata (e.g., time logs, task checklists) in each folder.
