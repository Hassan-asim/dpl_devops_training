<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Billing Automation Completion & Database Query Updates — 2026-02-03</h3>

---

## 🎯 Objective
Complete the monthly billing report automation system and update critical database queries for the Sindh Ombudsman project.

---

## 💡 Summary
- Finalized automated monthly billing report system with Lambda, SNS, and EventBridge integration.
- Updated and optimized database queries for advisors and escalation reports.
- Successfully tested end-to-end billing automation workflow.

---

## 🚀 Monthly Billing Report Automation — Completion
**Scope:** Finalize automated billing system for finance team with monthly triggers.

**Implementation Steps:**
- **Lambda Code Updates:** Removed HTML table preview, kept clickable links for filtered/full CSV reports
- **SNS Topic Cleanup:** Consolidated to single finance team topic (`arn:aws:sns:us-west-2:353545917793:FinanceMonthlyBilling`)
- **IAM Permissions:** Updated Lambda inline policy for S3 read/write and SNS publish permissions
- **EventBridge Trigger:** Configured monthly schedule (`cron(0 0 1 * ? *)`) for automatic execution

**Testing Results:**
- Manual Lambda invocation successful
- Filtered CSV generation and S3 upload verified
- SNS email delivery to `sindh-ombudsman-ai-cloud-cost@dplit.com` confirmed
- Links functional for both filtered and full CSV reports

**Final Configuration:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:us-west-2:353545917793:FinanceMonthlyBilling"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::dplit-monthly-billing-reports", "arn:aws:s3:::dplit-monthly-billing-reports/*"]
    },
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::dplit-monthly-billing-reports/filtered-monthly-reports/*"
    }
  ]
}
```

---

## 🗄️ Database Query Optimization
**Task:** Update critical database queries for improved performance and accuracy.

**Advisors Report Query:**
- Updated `ADVISORS_REPORT` query in `tbl_report_queries`
- Enhanced to show two rows per advisor: Head office (IO assignments) and Vetting Regions
- Integrated all active statuses from `tbl_complain_status` as JSON objects
- Fixed region assignment logic with proper table joins

**Escalation Report Query:**
- Updated `REGIONAL_ESCALATION_REPORT` query with comprehensive complaint tracking
- Added 11 different escalation categories with proper date calculations
- Implemented business day calculations excluding weekends
- Enhanced filtering logic for complaint types and statuses

**Key Improvements:**
- Optimized JOIN operations for better performance
- Added proper NULL handling and array aggregation
- Implemented business logic for working day calculations
- Enhanced status tracking with JSON object structures

---

## 📈 Monitoring & Next Steps
**Operational Status:**
- Billing automation system fully operational and tested
- Monthly triggers configured for 1st of each month at midnight UTC
- Database queries updated and optimized for production use

**Monitoring Plan:**
- EventBridge invocation tracking on monthly schedule
- CloudWatch logs monitoring for Lambda execution
- SNS delivery confirmation tracking
- Database query performance monitoring

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-02-03