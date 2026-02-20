
<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Lambda CDK Deployment to Sindh CMS — 2026-02-17</h3>

---

## 🎯 Objective
Deploy changes made in the Lambda CDK sub-repo to DEV and UAT environments in the Sindh CMS Project.

---

## 💡 Summary
Successfully deployed Lambda CDK changes to the DEV and UAT environments within the Sindh CMS Project. This involved using `cdk diff` to preview changes and `cdk deploy` to apply updates for both SQS and Lambda stacks in each respective environment.

---

## 🚀 Sindh CMS Project: Lambda CDK Deployment

**Deployment Process:**

**1. Deployment to DEV Environment:**
- Set `TARGET_ENV` to `DEV`.
- Previewed changes using `npx cdk diff --profile sindh-project`.
- Deployed changes using `npx cdk deploy DEV-SqsStack DEV-LambdaStack --profile sindh-project`.

**Commands Used for DEV:**
```bash
# Set environment variable for DEV
export TARGET_ENV=DEV

# Preview changes
npx cdk diff --profile sindh-project

# Deploy
npx cdk deploy DEV-SqsStack DEV-LambdaStack --profile sindh-project
```

**2. Deployment to UAT Environment:**
- Set `TARGET_ENV` to `UAT`.
- Previewed changes using `npx cdk diff --profile sindh-project`.
- Deployed changes using `npx cdk deploy UAT-SqsStack UAT-LambdaStack --profile sindh-project`.

**Commands Used for UAT:**
```bash
# Set environment variable for UAT
export TARGET_ENV=UAT

# Preview changes
npx cdk diff --profile sindh-project

# Deploy
npx cdk deploy UAT-SqsStack UAT-LambdaStack --profile sindh-project
```

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Deployed Lambda CDK changes to DEV environment (Sindh CMS Project).
- ✅ Deployed Lambda CDK changes to UAT environment (Sindh CMS Project).

**Next Steps:**
- Monitor the stability and functionality of the deployed changes in both DEV and UAT environments.
- Verify that SQS and Lambda stacks are operating as expected.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-02-17
