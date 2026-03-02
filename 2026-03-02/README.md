```markdown
<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • AWS Training, Dev Troubleshooting & Environment Setup — 2026-03-02</h3>

---

## 🎯 Objective
Continue AWS training, investigate and resolve development environment gateway errors, consult on production database security and backup strategy, and configure AWS Lambda environment variables for the backend services.

---

## 💡 Summary
Continued the KodeKloud AWS for Beginners training course. Investigated and resolved a 502 Bad Gateway error on the DEV Admin website by identifying root causes and sharing findings with Hazar, who successfully applied the fixes. Consulted with Salman regarding production database backup and security measures against DDoS threats; verified that the Production RDS instance has robust security configurations in place. Attended the Career Growth - Onboarding Session. Completed environment variable setup for three AWS Lambda functions in the DEV backend, adding new configuration variables to the ASP.NET Core application for AI operations.

---

## 🚀 Development & Infrastructure Operations

**1. DEV Environment Troubleshooting:**
- Investigated 502 Bad Gateway error affecting the DEV Admin website.
- Identified root causes and documented findings.
- Shared detailed analysis with Hazar, who applied the solution successfully.
- Error resolved and environment restored to operational state.

**2. Production Security & Backup Strategy:**
- Reviewed production database security configuration for Prod RDS (prod-postgres-instance).
- Verified SSL encryption is enabled (sslmode=verify-full) with encrypted connections.
- Confirmed storage encryption is active and security groups restrict access appropriately.
- Confirmed database is not publicly accessible.
- Consulted with Salman regarding DDoS protection and backup requirements.
- Provided recommendations for database snapshot backup implementation.

**3. Lambda Function Environment Variables Setup (DEV Completed):**
- Added 3 new AWS Lambda function name environment variables to ASP.NET Core backend.
- Modified `start_server.sh` to pass Lambda function names as environment variables.
- Connected to DEV backend EC2 via AWS Console Instance Connect.
- Added 3 variables to `/etc/environment`:
  - `AI_EXAMINATION_FUNCTION_NAME=AIFunction-dev`
  - `TEXT_REFINE_FUNCTION_NAME=TextRefineFunction-dev`
  - `DRAFT_GENERATION_FUNCTION_NAME=DraftGenerationFunction-dev`
- Verified variables were properly configured and ready for use.
- Documented variable access methods (IConfiguration injection and Environment.GetEnvironmentVariable).

**Existing Environment Variables in Place:**
- ASPNETCORE_ENVIRONMENT, COGNITO_USER_POOL_ID, AWS_REGION
- DB_SECRET_NAME, COGNITO_CLIENT_ID, FILE_UPLOAD_BUCKET_NAME, NOTIFICATION_QUEUE_URL

---

## 📚 Training & Professional Development

**1. AWS for Beginners (KodeKloud):**
- Continued the "AWS for Beginners with Hands-on Labs" course provided by Hazar.
- Completed course modules focused on AWS fundamentals and hands-on exercises.
- Link: [Module Lesson](https://learn.kodekloud.com/user/courses/aws-for-beginners-with-hands-on-labs/module/d28d64dd-cbb1-45ed-83c4-e8d4b0b0d08b/lesson/191587ad-e9a2-4892-acb5-528a6d38034c)

**2. Onboarding & Professional Growth:**
- Attended the Career Growth - Onboarding Session by Muhammad Muneeb.
- Focused on professional development and organizational alignment.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Continued KodeKloud AWS training.
- ✅ Investigated and resolved DEV Admin website gateway error.
- ✅ Reviewed and documented production database security configuration.
- ✅ Provided backup and DDoS protection recommendations to Salman.
- ✅ Configured Lambda function environment variables in DEV backend.
- ✅ Verified environment variable setup and documented access methods.
- ✅ Attended Career Growth onboarding session.

**Next Steps:**
- Implement UAT backend environment variables setup (following DEV pattern).
- Implement PROD backend environment variables setup (following DEV pattern).
- Monitor DEV backend operations post configuration changes.
- Execute database snapshot backup strategy as recommended.
- Continue KodeKloud AWS training progress.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-03-02

```