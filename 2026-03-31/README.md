<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • ECS Troubleshooting Course Progress, CDK Diff Resolution & Automation Planning</h3>

---

## 🎯 Objective Recap
- Continue ECS troubleshooting course and reach 40% completion.
- Resolve CDK diff issues across multiple stacks (AppServiceStack, IdentityStack, MediaCdnStack).
- Complete AWS Cloud Quest Cloud Practitioner assignment #2.
- Discuss static website deployment on EC2 with Izza.
- Finalize automation plan for db-bastion EC2 instance lifecycle management after Hazar's review.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CDK, CloudFormation, Lambda, CloudFront
- **Projects:** Nova Via, Sindh CMS

---

## 📚 Notes & Key Learnings

### 1. ECS Troubleshooting Course Progress
- Continued "Troubleshooting: Amazon Elastic Container Service" course.
- Achieved 40% completion.
- Focused on advanced troubleshooting techniques and CLI commands.

### 2. CDK Diff Resolution and Deployment
- Provided comprehensive update to Hazar regarding CDK diff issues.
- **Summary of Changes:**
  - **dev-AppServiceStack:** Adds s3:PutObject permission (intended change, ready to deploy).
  - **dev-IdentityStack:** Includes Lambda code updates for auth challenge functions (Git version ahead with changes from Jan 2026 not yet deployed).
  - **dev-MediaCdnStack:** Includes CloudFront public key update (Git version ahead with latest commit from Mar 26, 2026 not deployed).

- **Current Issue:** IdentityStack and MediaCdnStack have pending Git changes that were never deployed to AWS. Since AppServiceStack depends on these stacks, deploying the S3 permission fix would also trigger deployment of these pending updates.

- **Approaches Considered:**
  - Deploy all three stacks together to fully sync AWS with Git.
  - Manually add only the s3:PutObject permission via AWS Console (avoid CDK deployment).
  - First deploy IdentityStack and MediaCdnStack separately, then proceed with S3 fix.

- **Resolution Steps Taken:**
  - Pulled required files from Git:
    - `source/cdk/lambda/auth-triggers/define-auth-challenge.ts`
    - `source/cdk/lambda/auth-triggers/create-auth-challenge.ts`
    - `source/cdk/lambda/auth-triggers/verify-auth-challenge.ts`
  - Copied keys.zip folder into CDK folder.
  - Resolved MediaCdnStack diff by updating CloudFront public key.
  - Successfully completed deployment after resolving diffs.

### 3. AWS Cloud Quest Cloud Practitioner
- Started new gamified learning course on AWS Skillbuilder.
- Working on assignment #2, currently in progress.
- Course URL: [AWS Cloud Quest Cloud Practitioner](https://skillbuilder.aws/learn/FU5WCYVGKY/aws-cloud-quest-cloud-practitioner/JF9TKU68GT)

### 4. Static Website Deployment Discussion
- Had technical discussion with Izza regarding deploying a static website on an EC2 instance.
- Explored various approaches and best practices for EC2-based static website hosting.

### 5. EC2 Automation Plan Finalization
- Created comprehensive automation plan for db-bastion EC2 instance stop/start lifecycle management.
- Shared plan with Hazar for review: [automation_plan.md](https://github.com/Hassan-asim/dpl_devops_training/blob/main/2026-03-30/taskplan/automation_plan.md)
- **Feedback from Hazar:** Identified that the start instance runbook is unnecessary.
- Incorporated feedback and refined the automation approach.

---

## 📋 CDK Diff Details

### IdentityStack Changes
```
Stack dev-IdentityStack

Resources

[~] AWS::Lambda::Function DefineAuthChallengeFunction DefineAuthChallengeFunction2CCDC45E

└─ [~] Code

     └─ [~] .S3Key:

         ├─ [-] 007b5e53b267d55ddf0cb118ec64a75503439c4569784f3a572ac8799643abaa.zip

         └─ [+] 1d5e3da233928c1c5423fee5e1890a998826e274f069962105882f7610a757e3.zip

[~] AWS::Lambda::Function CreateAuthChallengeFunction CreateAuthChallengeFunction3E954DBF

└─ [~] Code

     └─ [~] .S3Key:

         ├─ [-] fb2a3b9275d0a3bca89df93df07c2e1efcc40e62ab3f76769f8e0db420231f4f.zip

         └─ [+] 74c21914c2658f37907d88cc5621375d062c9666b2d28aa4be185b99d63e9cea.zip

[~] AWS::Lambda::Function VerifyAuthChallengeFunction VerifyAuthChallengeFunction937C103A

└─ [~] Code

     └─ [~] .S3Key:

         ├─ [-] 352bc3d707e27af466db20a8f54a8da5130ab812336242305795abd66186a373.zip

         └─ [+] 960d293183792a3be7c6ceb88e5b8e25bc5455a2a4beabad217c55a18ecbef91.zip
```

### MediaCdnStack Changes
```
Stack dev-MediaCdnStack

Resources

[~] AWS::CloudFront::PublicKey MediaCdnPublicKey MediaCdnPublicKey470A3B35        

└─ [~] PublicKeyConfig

     └─ [~] .EncodedKey:

         ├─ [-] -----BEGIN PUBLIC KEY-----

MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoHI1LUcT99RNaZDs2bmU

OzX1Mw33yUBZ2Yd4LGsvfLTWCj2nMGufcn13qp+DIYjsyaC+4aLx9fgxmnyS7JOZ

jpv7aZ/oxMlof6bqGS3be7MrGUiVmy3v1PkEyTMvxeNEeZrS8szn6T+qlwf7CNDJ

------------------------------------/B0vZmGa

xISKFNoc/hpUVE1mtxJVPbLRA64c6KrsnhmRgBfUvpr3MLtcAxCDMwY0k4WgmNsF

KdLTLX053BLCol2+QKo3w5SPD2yc7C6You6zz3u4N3q1/YvRsnMT2NLWAgvaDhVX

MwIDAQAB

-----END PUBLIC KEY-----
 
         └─ [+] -----BEGIN PUBLIC KEY-----

MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArkF6QhYuJm4qGhpHQH7m

pW7vyCizJ7/ghjegvSEWbyp+4X4mN+lIKZhrSGfGGLMY4Y0ygbf2lWhwHaKDeI3k

VXjev1Vw9ZPYoYGccR+TqyVs----------------------------------+C1yW

----------------------------jBYiFRAmS5u8tX44XK7lX8dwlisiAVpCOXm

hmeZDw9UV0+K9Y0+ev3rEBj6jo/p46ZPy9VtzunmJjpSmHPMQUrX7xSJQnPbFQn2

M+oBmB0vSvUt6ZAFJivdnqLkH51CUvVeRLbYO9eCiBiepT+GhjmO8lpgJNVpIba1

8QIDAQAB

-----END PUBLIC KEY-----
```

---

## 📝 Files Updated/Pulled
- `source/cdk/lambda/auth-triggers/define-auth-challenge.ts`
- `source/cdk/lambda/auth-triggers/create-auth-challenge.ts`
- `source/cdk/lambda/auth-triggers/verify-auth-challenge.ts`
- `source/cdk/keys/dev-media-cdn-public-key.pem`
- keys.zip folder copied to CDK directory

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Continued ECS troubleshooting course (40% complete).
- ✅ Resolved CDK diff issues and completed deployment.
- ✅ Started AWS Cloud Quest Cloud Practitioner assignment #2.
- ✅ Discussed static website deployment on EC2 with Izza.
- ✅ Created and refined automation plan for db-bastion EC2 instance after Hazar's review.

**Next Steps:**
1. Complete remaining ECS troubleshooting course modules.
2. Finish AWS Cloud Quest Cloud Practitioner assignment #2.
3. Implement refined automation plan for EC2 lifecycle management.
4. Continue monitoring CDK deployments and infrastructure health.
5. Explore static website deployment options on EC2 instances.