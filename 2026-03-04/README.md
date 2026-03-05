
<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • CloudFront Media CDN Cookies & Disk Space Troubleshooting — 2026-03-04</h3>

---

## 🎯 Objective
Resolve Afifa's CloudFront media CDN private key access and signed cookies issues in the Novavia project; verify and validate the signed cookie solution; learn from Hazar's approach to disk space error resolution in the Sindh project.

---

## 💡 Summary
Investigated and resolved a CloudFront signed cookies rejection issue for Afifa in the Novavia Media CDN project. The root cause was that the private key was stored as a binary secret in AWS Secrets Manager but was being fetched as a plain string. After identifying the issue, provided guidance to decode the private key using base64 and regenerate the signed cookies. Verified the solution end-to-end using AWS CloudShell, executing bash commands to fetch, decode, and validate the private key, then generating valid CloudFront signed cookies and successfully testing them via curl. Reviewed Hazar's GitLab changes to understand how disk space extension was handled for a deployment stage error in the Sindh project.

---

## 🚀 Development & Infrastructure Operations

**1. Novavia Media CDN Signed Cookies Troubleshooting:**
- Received report from Afifa regarding issues with CloudFront media CDN private key access.
- Updated the webhook in AWS Secrets Manager to resolve initial access issue.
- Verified the private key was functional but further investigation revealed the root cause.
- **Root Cause Identified:** The private key was stored as a binary secret but was being fetched as a plain string, causing signed cookie generation to fail.
- Advised Afifa to fetch the private key as a binary secret, decode it using base64, and then regenerate the signed cookies.

**2. CloudFront Signed Cookies Validation & Testing:**
- Replicated and validated the solution end-to-end using AWS CloudShell.
- Executed bash command to fetch and decode the binary secret:
  ```bash
  aws secretsmanager get-secret-value --secret-id dev-media-cdn-private-key --query SecretBinary --output text | base64 --decode > /tmp/private_key.pem
  ```
- Verified private key integrity with OpenSSL:
  ```bash
  openssl rsa -in /tmp/private_key.pem -check -noout
  ```
- Generated CloudFront signed cookies using Python cryptography library with custom policy and 10-minute expiration.
- Successfully tested signed cookies via curl against the CloudFront distribution.
- **Result:** ✅ CloudFront accepted signed cookies, signature validated, key pair matched trusted key group, policy not expired, resource path matched.
- Confirmed solution to Afifa for implementation.

**3. Sindh Project Disk Space Error Investigation:**
- Asked Hazar about his approach to resolving the deploy stage error.
- Reviewed Hazar's GitLab changes to understand the disk space extension solution.
- Learned how the issue (full disk space causing deployment failures) was resolved through infrastructure adjustments.

---

## 📚 Training & Professional Development

**AWS for Beginners (KodeKloud):**
- Continued watching AWS for Beginners course modules provided by Hazar.

**CloudFront & AWS Secrets Manager:**
- Deepened knowledge of CloudFront signed cookies and binary secret handling in AWS Secrets Manager.
- Learned practical debugging and validation techniques using AWS CloudShell.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Updated CloudFront webhook in Secrets Manager.
- ✅ Diagnosed root cause of signed cookies rejection (binary vs string secret).
- ✅ Validated solution end-to-end with AWS CloudShell testing.
- ✅ Generated and tested valid CloudFront signed cookies via curl.
- ✅ Provided solution guidance to Afifa for implementation.
- ✅ Reviewed and learned from Hazar's disk space error resolution approach.

**Next Steps:**
1. Follow up with Afifa to confirm successful implementation of signed cookies in Novavia project.
2. Continue AWS for Beginners training modules.
3. Apply disk space extension knowledge to Sindh infrastructure monitoring and maintenance.
4. Monitor Novavia media CDN for any recurrence of signed cookie issues.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-03-04
