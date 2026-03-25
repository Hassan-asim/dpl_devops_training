<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • AWS SAM & IAM Policy Behavior Experiment Log</h3>

---

## 🎯 Objective Recap
- Understand how AWS SAM/CloudFormation behaves when policies are modified manually in the console, templates are redeployed, and resources already exist.
- Complete AWS course and obtain certificate of completion.
- Create MR for Sindh project template.yaml changes to add DynamoDB tables for Lambda function.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** SAM, IAM, Lambda, DynamoDB, CloudFormation

---

## 📚 Notes & Key Learnings

### 1. Initial Issue
- Lambda function was failing due to missing DynamoDB permissions.
- Required DynamoDB tables were not included in IAM role policy.

### 2. Temporary Fix (Console)
- Manually updated inline IAM policies in console for dev, uat, and prod roles.
- Added required DynamoDB table ARNs in policy.
- Function started working successfully.

**Observation:** Fix worked but was done manually in console (not persistent).

### 3. Permanent Fix (Template Update)
- Updated SAM template.yaml to include required DynamoDB table ARNs in IAM policy.
- Created MR for proper deployment to ensure changes persist after deployment.

---

## 🧪 Experiment Log

### Experiment 1: Inline Policy Overwrite

**Steps:**
1. Created IAM role using SAM with inline policy (s3:GetObject).
2. Manually edited policy in console and added:
   - s3:PutObject
   - s3:GetAccessPoint
3. Modified SAM template to include:
   - s3:GetObject
   - s3:PutObject
   - s3:ListBucket
4. Redeployed SAM template.

**Result:**
- Inline policy was overwritten.
- Console change (s3:GetAccessPoint) was removed.
- Policy matched template exactly.

**Conclusion:** Inline policies managed by SAM are overwritten on deployment if template changes.

---

### Experiment 2: No Change Deployment

**Steps:**
1. Manually edited inline policy in console.
2. Redeployed SAM template without any changes.

**Result:**
- Deployment returned: "No changes to deploy"
- Manual changes remained intact.

**Conclusion:** SAM does NOT overwrite unless template changes.

---

### Experiment 3: Existing Role Conflict

**Steps:**
1. Created IAM role manually in console.
2. Tried creating same role via SAM (same RoleName).

**Result:**
- Deployment failed with: "Role already exists"
- Stack rolled back.

**Conclusion:** SAM cannot overwrite or create existing manual roles. Must use resource import to manage them.

---

## 📋 Final Understanding

| Scenario | Behavior |
|----------|----------|
| Console changes to inline policies | TEMPORARY |
| SAM template redeployed with changes | Policies are overwritten |
| Template unchanged | No overwrite occurs |
| Existing manually created roles | Cannot be overwritten by SAM |

### Best Practices:
1. Always update template.yaml for permanent changes.
2. Avoid relying on console edits for production infrastructure.
3. Use resource import for managing existing manual resources.

---

## 📝 MR Created for Sindh Project

- Created MR for template.yaml changes to add DynamoDB tables for Lambda function in Sindh project.
- Sent to Hazar for review.
- Hazar requested above tests and experiments to validate understanding.
- Experiments completed and findings documented.

---

## 📚 Training & Professional Development

**1. AWS Course Completion:**
- Completed AWS course started earlier in the week.
- Certificate of completion saved in `images/` folder.

**2. New Course Started - ECS Troubleshooting:**
- Started new course: "Troubleshooting: Amazon Elastic Container Service"
- Progress: Completed up to Module 3.
- Building expertise in ECS diagnostic and troubleshooting techniques.

---

## 🖼️ Evidence & Screenshots

### Course Completion Certificate
- ![AWS Course Completion Certificate](./images/course_completion_certificate.png) — Certificate of completion for AWS course started earlier.

---

## ✅ Daily Summary
- Conducted comprehensive AWS SAM & IAM policy behavior experiments to understand deployment overwrite patterns.
- Documented three key experiments: inline policy overwrite, no-change deployment, and existing role conflict.
- Established best practices for managing IAM policies via SAM templates.
- Completed AWS course and obtained certificate of completion.
- Created MR for Sindh project template.yaml changes (DynamoDB table permissions for Lambda function).
- Next steps: Await MR review from Hazar; apply learnings to production infrastructure management.

Made by Sufi Hassan Asim — 2026-03-25
