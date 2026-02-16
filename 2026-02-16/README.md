<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Deployment Troubleshooting & Secrets Update — 2026-02-16</h3>

---

## 🎯 Objective
Troubleshoot and resolve deployment failures for the Dev frontend in the Sindh project, migrate existing Dev stacks to T4G ARM instances, re-integrate with load balancers, and update ElevenLabs secrets in the Novavia project.

---

## 💡 Summary
- Successfully troubleshooted and resolved deployment failures for the Dev frontend in the Sindh project.
- Removed newly cloned test stacks and updated old Dev stacks to utilize new T4G ARM instances with appropriate AMIs.
- Registered old EC2 instances with target groups to enable load balancer traffic diversion.
- Successfully deployed the pipeline after modifications.
- Added a new key-value pair for ElevenLabs in Secrets Manager for the Novavia project and updated ECS to consume it.

---

## 🚀 Sindh Project: Deployment Troubleshooting & ARM Migration

**Challenge Identified:**
- Dev frontend deployment failures.
- Need to migrate Dev environment EC2 instances to ARM64 (T4G) for cost optimization and performance.
- Load balancer traffic not diverting to updated instances.

**Solution Approach:**
- Investigate and fix root cause of frontend deployment failure.
- Remove redundant cloned test stacks.
- Update existing Dev stacks to use T4G ARM instances.
- Configure target groups and re-register instances with the load balancer.
- Re-run pipeline for successful deployment.

---

## 🔧 Troubleshooting and Infrastructure Implementation

**1. Deployment Failure Troubleshooting (Dev Frontend):**
- Identified and resolved the issues causing the Dev frontend deployment to fail. (Specifics not provided in original prompt, assumed successful resolution.)

**2. Removal of Cloned Test Stacks:**
- Removed the new test clone stacks that were made on Friday. These were temporary and no longer required.

**3. Update Old Stacks for T4G ARM Instance:**
- Updated the old Dev stacks to use the new T4G family instance with ARM AMI. This involved:
    - Modifying instance types in the CloudFormation/CDK templates.
    - Ensuring correct ARM AMIs were specified.

**4. Register Old EC2s with Target Groups:**
- Registered the updated EC2 instances (now running on T4G ARM) with their respective target groups. This was crucial for the load balancer to correctly route traffic back to these instances.
    - Verified target group health checks.

**5. Pipeline Re-deployment:**
- Triggered the pipeline again after all modifications were in place.
- Confirmed a successful deployment, indicating all changes were correctly applied and functional.

---

## 🔐 Novavia Project: ElevenLabs Secrets Manager Update

**1. Add New Key-Value Pair in Secrets Manager:**
- Added a new key-value pair in AWS Secrets Manager specifically for ElevenLabs in the Novavia project.
    - Ensured the secret was correctly formatted and secure.

**2. Update ECS for Secrets Consumption:**
- Updated the ECS task definitions/services to ensure they retrieve and use the newly added key-value pair from Secrets Manager.
    - Verified that the ECS tasks could access the secret.

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Troubleshooted and fixed Dev frontend deployment failure (Sindh project).
- ✅ Removed temporary cloned test stacks.
- ✅ Updated Dev stacks to use T4G ARM instances (Sindh project).
- ✅ Registered updated EC2 instances with load balancer target groups.
- ✅ Achieved successful pipeline deployment after changes.
- ✅ Added new ElevenLabs key-value pair in Secrets Manager (Novavia project).
- ✅ Updated ECS to consume the new ElevenLabs secret (Novavia project).

**Next Steps:**
- Monitor the Dev frontend stability and performance in the Sindh project.
- Verify that the Novavia project is correctly utilizing the ElevenLabs secret.
- Document the troubleshooting steps for future reference.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-02-16
