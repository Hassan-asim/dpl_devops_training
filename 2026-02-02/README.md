<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • AWS Billing Automation & Access Management — 2026-02-02</h3>

---

## 🎯 Objective
Implement automated monthly billing reports for the finance team and configure AWS access permissions for team members.

---

## 💡 Summary
- Created automated monthly Cost & Usage Report system with Lambda processing and SNS notifications for the finance team.
- Configured Bedrock access for Izza with full permissions.
- Set up S3 bucket and Athena access for Izza via AWS Identity Center (SSO).

---

## 📊 Billing Report & Alert System
**Scope:** Automate monthly AWS billing reports with filtered data for finance team.

**Implementation:**
- Created monthly Cost & Usage Report (MonthlyServiceReport) in Workload account
- Configured S3 export to `dplit-monthly-billing-reports` bucket with monthly granularity
- Developed Lambda function `FilterMonthlyBillingReport` to process reports and send notifications
- Set up SNS topic for email notifications to `sindh-ombudsman-ai-cloud-cost@dplit.com`

**Status:**
- Infrastructure deployed successfully
- SNS subscription requires email confirmation before Lambda testing

---

## 🔐 Access Management & Permissions
**Task:** Configure AWS service access for team members.

**Bedrock Access for Izza:**
- Required permission: `bedrock:PutModelInvocationLoggingConfiguration`
- Granted `AmazonBedrockFullAccess` policy for comprehensive access

**S3 & Athena Access for Izza:**
- Created dedicated S3 bucket `s3bucketforizza` in Workload account
- Configured permission set in Sindh account via AWS Identity Center (SSO)
- Granted read/write access to S3 bucket and full Athena access
- Removed redundant manually created IAM role in Workload account

---

## 📋 Next Steps
**Pending Actions:**
1. **SNS Subscription Confirmation** - Hazar to confirm subscription via email
2. **Lambda Function Testing** - Test with sample billing report data
3. **SNS Delivery Verification** - Confirm email delivery to finance team
4. **EventBridge Scheduling** - Set up monthly trigger (`cron(0 0 1 * ? *)`)
5. **Monitoring Setup** - Configure CloudWatch logs and alerts for automated runs

**Test Event JSON:**
```json
{
  "reportBucket": "dplit-monthly-billing-reports",
  "reportPrefix": "monthly-reports/MonthlyServiceReport/date-range/"
}
```

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-02-02