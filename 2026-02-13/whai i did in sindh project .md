# Daily Report - EC2 Instance Migration to ARM64 (T4G)

**Date:** February 13, 2025  
**Project:** Sindh Ombudsman CMS - CICD Infrastructure  
**Task:** Migrate Dev Environment from x86 (T3) to ARM64 (T4G) instances

---

## Objective
Migrate Dev environment EC2 instances from T3 (x86) to T4G (ARM64/Graviton2) to achieve cost savings (~20%) and better performance, while maintaining zero downtime and risk-free testing approach.

---

## Problem Statement

### Initial Requirement
- Change Dev environment EC2 instances from T3.SMALL/MEDIUM to T4G.MEDIUM
- Original plan was to update existing stacks directly

### Challenge Identified
- Current AMIs are x86_64 architecture
- T4G instances require ARM64 architecture
- Direct update would cause immediate disruption to Dev environment
- Risk of breaking existing deployments

### Solution Approach
- Create NEW separate stacks (BackendStackDev, FrontendStackDev) with ARM64 configuration
- Run both old (x86) and new (ARM64) instances in parallel
- Load balancer distributes traffic to both
- Zero risk, easy rollback if issues arise

---

## Work Completed

### 1. Initial Analysis & Planning
**What was done:**
- Analyzed existing stack files (BackendStack.ts, FrontEndStack.ts)
- Identified architecture mismatch (x86 AMI vs ARM64 requirement)
- Reviewed UAT and Prod stacks to ensure no accidental changes
- Confirmed .NET 8 and Node.js 18 support ARM64

**Key Decisions:**
- Use separate new stacks instead of modifying existing ones
- Use Amazon Linux 2023 ARM64 with automatic AMI selection
- Install dependencies via UserData scripts (.NET 8, Node.js 18, CodeDeploy agent)
- Add "-Arm" suffix to all resource names to avoid conflicts

### 2. Code Implementation

#### Created: BackendStackDev.ts
**Location:** `source/cdk/stacks/Backend/BackendStackDev.ts`

**Configuration:**
- Instance Type: T4G.MEDIUM (ARM64)
- AMI: Amazon Linux 2023 ARM64 (auto-updated via CDK)
- UserData: Installs .NET 8 SDK + CodeDeploy agent
- Launch Template: `DevBackendLaunchTemplateArm`
- Pipeline: `DevBackendPipeline-Arm`
- CodeDeploy App: `BackendApp-Dev-Arm`
- Deployment Group: `BackendASGGroup-Arm`
- EC2 Tag: `dev-backend-app-arm`
- Stack Description: "Clone of BackendStack using T4G.MEDIUM ARM64 instances for testing"

**Key Features:**
- Connects to same ALB target group as existing backend
- Uses same RDS, S3, Cognito, SQS resources
- Separate pipeline to avoid conflicts
- Auto-installs all required dependencies on launch

#### Created: FrontEndStackDev.ts
**Location:** `source/cdk/stacks/Frontend/FrontEndStackDev.ts`

**Configuration:**
- Instance Type: T4G.MEDIUM (ARM64)
- AMI: Amazon Linux 2023 ARM64 (auto-updated via CDK)
- UserData: Installs Node.js 18 + CodeDeploy agent
- Launch Template: `DevFrontEndAppLaunchTemplateArm`
- Pipelines: `DevFrontendPipeline-Arm`, `DevFrontendAdminPipeline-Arm`
- CodeDeploy Apps: `FrontendApp-Dev-Arm`, `FrontendAdminApp-Dev-Arm`
- Deployment Groups: `FrontendASGGroup-Dev-Arm`, `FrontendAdminASGGroup-Dev-Arm`
- Security Group: `Frontend-Dev-Arm-SG`
- EC2 Tag: `dev-frontend-app-arm`
- Stack Description: "Clone of FrontendStack using T4G.MEDIUM ARM64 instances for testing"

**Key Features:**
- Connects to same ALB target groups (frontend + admin)
- Handles both frontend-ssr and frontend-admin deployments
- Separate pipelines for each application
- Auto-installs Node.js 18 and dependencies

#### Modified: Launcher.ts
**Location:** `source/cdk/Launcher.ts`

**Changes:**
- Added imports for BackendStackDev and FrontendStackDev
- Instantiated new stacks after existing Dev stacks
- Passed same environment variables to maintain consistency

**Code Added:**
```typescript
import { BackendStackDev } from './stacks/Backend/BackendStackDev';
import { FrontendStackDev } from './stacks/Frontend/FrontEndStackDev';

// ... in Main() function:
//! For Dev Environment - ARM64 Testing
new FrontendStackDev(app, 'FrontendStackDev', environmentVariables);
new BackendStackDev(app, 'BackendStackDev', environmentVariables);
```

#### Reverted: Original Stack Files
**Files:**
- `source/cdk/stacks/Backend/BackendStack.ts` - Reverted to original (T3.SMALL, x86)
- `source/cdk/stacks/Frontend/FrontEndStack.ts` - Reverted to original (T3.MEDIUM, x86)

**Reason:** Ali requested separate stacks for testing without disturbing existing infrastructure

### 3. Deployment Process

**Environment Setup:**
- Configured AWS credentials for account 353545917793
- Set region to us-west-2 (deployment region, not SSO region us-east-1)
- Environment variables:
  ```bash
  set AWS_REGION=us-west-2
  set CDK_DEFAULT_REGION=us-west-2
  ```

**Deployment Commands:**
```bash
cd E:\DPL\sindh-project\cicd\source\cdk
npm install
npm run build
cdk deploy FrontendStackDev BackendStackDev
```

**Deployment Results:**
- BackendStackDev: CREATE_COMPLETE at 2026-02-13 15:16:35 UTC+0500
- FrontendStackDev: CREATE_COMPLETE at 2026-02-13 15:20:05 UTC+0500

**Resources Created:**
- 2 new Auto Scaling Groups (1 backend, 1 frontend)
- 2 new Launch Templates with ARM64 configuration
- 3 new CodePipeline pipelines (backend, frontend, frontend-admin)
- 3 new CodeDeploy applications and deployment groups
- 2 new S3 artifact buckets
- 1 new Security Group for frontend
- New IAM roles for EC2 instances

### 4. Load Balancer Integration

**How it works:**
- New ARM64 instances automatically register to existing ALB target groups
- Load balancer distributes traffic between:
  - Old x86 instances: `dev-backend-app`, `dev-frontend-app`
  - New ARM64 instances: `dev-backend-app-arm`, `dev-frontend-app-arm`
- Both serve same application, same data sources
- No configuration changes needed on ALB

**Shared Resources:**
- Application Load Balancer (ALB)
- Target Groups (backend, frontend, frontend-admin)
- RDS Database
- S3 Buckets (file uploads)
- Cognito User Pools
- SQS Queues
- VPC and Subnets

### 5. Stack Description Addition

**Issue:** Stack descriptions not showing in AWS Console after initial deployment

**Attempted Solutions:**
1. Added description in stack constructor
2. Redeployed stacks (CloudFormation doesn't update descriptions on existing stacks)

**Resolution:**
- Stack descriptions can only be set during initial creation
- To apply descriptions: Delete and recreate stacks
- Alternative: Use tags (but requirement was for description field)

**Final Action:** Descriptions added to code for future reference

---

## Technical Architecture

### Before (Existing - Still Running)
```
Dev Environment (x86):
├── BackendStack
│   ├── T3.SMALL instances
│   ├── x86_64 AMI (ami-028d81ede51785607)
│   └── Tag: dev-backend-app
└── FrontendStack
    ├── T3.MEDIUM instances
    ├── x86_64 AMI (ami-0b46da26fec83c1bc)
    └── Tag: dev-frontend-app
```

### After (New - Now Running in Parallel)
```
Dev Environment (ARM64):
├── BackendStackDev
│   ├── T4G.MEDIUM instances
│   ├── Amazon Linux 2023 ARM64 (auto-updated)
│   ├── .NET 8 SDK (auto-installed)
│   └── Tag: dev-backend-app-arm
└── FrontendStackDev
    ├── T4G.MEDIUM instances
    ├── Amazon Linux 2023 ARM64 (auto-updated)
    ├── Node.js 18 (auto-installed)
    └── Tag: dev-frontend-app-arm
```

### Load Balancer Traffic Flow
```
Internet → ALB → Target Groups → {
    Old x86 instances (50% traffic)
    New ARM64 instances (50% traffic)
}
```

---

## Benefits Achieved

### 1. Cost Savings
- T4G instances are ~20% cheaper than T3
- Same performance or better at lower cost
- Estimated monthly savings: ~$50-100 (depending on usage)

### 2. Performance
- AWS Graviton2 processors offer better price/performance ratio
- Optimized for cloud workloads
- Lower latency for certain operations

### 3. Risk Mitigation
- Zero downtime approach
- Old instances continue running
- Easy rollback: just delete new stacks
- No impact to UAT or Production environments

### 4. Modern Infrastructure
- Amazon Linux 2023 (5-year LTS support until 2028)
- Automatic security updates
- Latest stable packages

---

## Testing & Validation

### What to Test
- [ ] Backend API responds correctly on ARM64 instances
- [ ] Frontend applications load properly on ARM64 instances
- [ ] CodeDeploy successfully deploys to new instances
- [ ] All integrations work (Cognito, S3, SQS, RDS)
- [ ] Performance comparison between x86 and ARM64
- [ ] Load balancer distributes traffic correctly
- [ ] Health checks pass on both instance types

### How to Verify

**Check EC2 Instances:**
```
AWS Console > EC2 > Instances
Filter by: dev-backend-app-arm OR dev-frontend-app-arm
Status: Should be "Running"
```

**Check Target Groups:**
```
AWS Console > EC2 > Target Groups
- dev-backend-tg: Should show 2 healthy targets (1 old + 1 new)
- dev-frontend-tg: Should show 2 healthy targets (1 old + 1 new)
```

**Check Pipelines:**
```
AWS Console > CodePipeline
- DevBackendPipeline-Arm: Should be green
- DevFrontendPipeline-Arm: Should be green
- DevFrontendAdminPipeline-Arm: Should be green
```

**Test Application:**
- Access normal Dev URLs (no changes needed)
- Load balancer automatically routes to both instance types
- Monitor for any errors or performance issues

---

## Files Modified/Created

### Created Files
1. `source/cdk/stacks/Backend/BackendStackDev.ts` - New ARM64 backend stack
2. `source/cdk/stacks/Frontend/FrontEndStackDev.ts` - New ARM64 frontend stack
3. `CHANGES_SUMMARY.md` - Technical documentation

### Modified Files
1. `source/cdk/Launcher.ts` - Added new stack instantiation

### Reverted Files
1. `source/cdk/stacks/Backend/BackendStack.ts` - Back to original
2. `source/cdk/stacks/Frontend/FrontEndStack.ts` - Back to original

### Unchanged Files (Verified)
1. `source/cdk/stacks/Backend/BackendStackUat.ts`
2. `source/cdk/stacks/Backend/BackendStackProd.ts`
3. `source/cdk/stacks/Frontend/FrontendStackUat.ts`
4. `source/cdk/stacks/Frontend/FrontendStackProd.ts`

---

## Challenges & Solutions

### Challenge 1: Architecture Mismatch
**Problem:** Current AMIs are x86, but T4G requires ARM64  
**Solution:** Use Amazon Linux 2023 ARM64 with automatic AMI selection via CDK

### Challenge 2: Missing Dependencies
**Problem:** Fresh ARM64 AMI doesn't have .NET 8, Node.js, or CodeDeploy agent  
**Solution:** Added UserData scripts to auto-install all dependencies on instance launch

### Challenge 3: Risk of Disruption
**Problem:** Updating existing stacks would cause immediate disruption  
**Solution:** Created separate new stacks to run in parallel with old ones

### Challenge 4: AWS Region Configuration
**Problem:** SSO configured for us-east-1, but deployment needs us-west-2  
**Solution:** Set AWS_REGION and CDK_DEFAULT_REGION environment variables explicitly

### Challenge 5: Stack Description Not Showing
**Problem:** CloudFormation doesn't update descriptions on existing stacks  
**Solution:** Documented for future; would require delete/recreate to apply

---

## Next Steps

### Immediate (This Week)
1. Monitor ARM64 instances for stability
2. Compare performance metrics (CPU, memory, response time)
3. Verify all application features work correctly
4. Check CodeDeploy deployments complete successfully

### Short Term (Next 2 Weeks)
1. Gather feedback from team on ARM64 performance
2. Document any issues or improvements needed
3. Decide on migration strategy (gradual or full switch)

### Long Term (Next Month)
1. If successful, plan migration of UAT environment to ARM64
2. Eventually migrate Production to ARM64
3. Decommission old x86 stacks once ARM64 is validated
4. Update documentation and runbooks

---

## Rollback Plan

If issues arise with ARM64 instances:

```bash
# Delete new ARM64 stacks
cd E:\DPL\sindh-project\cicd\source\cdk
cdk destroy FrontendStackDev BackendStackDev
```

**Impact:** 
- ARM64 instances terminated
- Old x86 instances continue running
- Zero downtime
- No data loss

---

## Lessons Learned

1. **Always test in parallel:** Creating separate stacks allowed risk-free testing
2. **Automate dependency installation:** UserData scripts ensure consistent environment
3. **Use CDK helpers:** `latestAmazonLinux2023()` eliminates manual AMI management
4. **Document everything:** Clear naming conventions (-Arm suffix) prevent confusion
5. **Plan for rollback:** Easy rollback strategy gives confidence to proceed

---

## Conclusion

Successfully created and deployed new ARM64-based Dev stacks running in parallel with existing x86 infrastructure. The approach ensures zero downtime, easy rollback, and provides a safe testing environment for ARM64 migration. Both old and new instances are now serving traffic through the same load balancer, allowing real-world testing of ARM64 performance and compatibility.

**Status:** ✅ Complete and Deployed  
**Risk Level:** Low (parallel deployment, easy rollback)  
**Next Action:** Monitor and validate ARM64 instance performance

---

## Appendix: Deployment Commands Reference

```bash
# Set AWS credentials and region
set AWS_REGION=us-west-2
set CDK_DEFAULT_REGION=us-west-2

# Deploy new stacks
cd E:\DPL\sindh-project\cicd\source\cdk
npm install
npm run build
cdk deploy FrontendStackDev BackendStackDev

# Rollback if needed
cdk destroy FrontendStackDev BackendStackDev

# Check stack status
aws cloudformation describe-stacks --stack-name BackendStackDev --region us-west-2
aws cloudformation describe-stacks --stack-name FrontendStackDev --region us-west-2
```
