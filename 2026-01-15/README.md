<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Task 3: CICD Pipeline with AWS CDK for GitLab</h3>

---

## 🎯 Objective
Implement a **comprehensive CI/CD pipeline using AWS CDK** for a **GitLab repository**. The pipeline automates **builds for frontend and backend projects** using **AWS CodePipeline** and **CodeBuild**, with artifacts stored in **S3** and deployment capabilities for future stages.

---

## 💡 Summary / What I built

**Task 3** creates an **end-to-end CI/CD pipeline** with the following goals:

1. Connect a GitLab repository (`GTO/cdk-ecs-cicd`) to AWS CodePipeline using **CodeStar Connections**
2. Build frontend and backend code with **AWS CodeBuild**
3. Store build artifacts in an **S3 bucket**
4. Enable future deployment stages (ECS, S3, Lambda, etc.) as needed
5. Implement comprehensive logging and monitoring

This is implemented entirely using **AWS CDK (TypeScript)**.

---

## 📋 Table of Contents

* [Overview](#overview)
* [Architecture](#architecture)
* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)
* [Pipeline Details](#pipeline-details)
* [BuildSpec Files](#buildspec-files)
* [Deploying the Pipeline](#deploying-the-pipeline)
* [Testing](#testing)
* [Destroying Resources](#destroying-resources)
* [References](#references)

---

## 🔧 Architecture

```
GitLab Repository (feature/pipeline branch)
         │
         ▼
   CodeStar Connections
         │
         ▼
   AWS CodePipeline
   ┌─────────────────────┐
   │  Source Stage       │
   │  (GitLabSource)     │
   └─────────────────────┘
         │
         ▼
   ┌─────────────────────┐
   │  Build Stage        │
   │  FrontendBuild      │
   │  BackendBuild       │
   └─────────────────────┘
         │
         ▼
    S3 Artifact Bucket
    └─ CloudWatch Logs
    └─ SNS Notifications
```

---

## ✅ Prerequisites

1. **AWS Account** with admin privileges
2. **Node.js** v18+ (LTS recommended)
3. **AWS CDK** installed globally:
```bash
npm install -g aws-cdk
```

4. **AWS CLI** configured:
```bash
aws configure
```

5. **GitLab Repository**:
   - Group: `GTO`
   - Repo: `cdk-ecs-cicd`
   - Branch: `feature/pipeline` (Task 3 branch)

6. **Docker** (optional, for local testing of build processes)

---

## 🚀 Setup Instructions

### Step 1: Clone the repository
```bash
git clone <repo-url>
cd cdk-ecs-cicd/cdk
git checkout feature/pipeline
```

### Step 2: Install dependencies
```bash
npm install
```

### Step 3: Configure AWS credentials
```bash
aws configure
```
Provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-east-1)
- Default output format (json)

### Step 4: Create CodeStar Connection
```bash
aws codestar-connections create-connection \
  --connection-name GTO-GitLab-Connection \
  --provider-type GitLab
```

**Important**: 
- Copy the returned `ConnectionArn`
- Use it in your CDK stack configuration
- Authorize the connection in the AWS Console if prompted

### Step 5: Update CDK Stack with ConnectionArn
Edit `bin/cdk.ts` or your pipeline stack file:
```typescript
const connectionArn = 'arn:aws:codestar-connections:region:account-id:connection/connection-id';

new CicdPipelineStack(app, 'CicdPipelineStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: 'us-east-1' },
  gitLabConnectionArn: connectionArn,
});
```

---

## 📊 Pipeline Details

### Stack Information
- **Stack Name**: `CicdPipelineStack`
- **Pipeline Name**: `Task3Pipeline`
- **Artifact Bucket**: `PipelineArtifactBucket` (auto-created with encryption)
- **Service Role**: `PipelineServiceRole` (auto-created with least privileges)

### Pipeline Stages

#### 1. Source Stage
- **Provider**: GitLab (via CodeStar Connections)
- **Repository**: `GTO/cdk-ecs-cicd`
- **Branch**: `feature/pipeline`
- **Trigger**: Manual or webhook-based
- **Artifact Output**: Source code zipped to S3

#### 2. Build Stage
Runs two build projects in parallel:

##### FrontendBuild
- **Project Name**: `FrontendBuildProject`
- **Runtime**: Node.js 18
- **Buildspec**: `buildspec/frontend/buildspec.yml`
- **Environment Variables**:
  - `ARTIFACT_LOCATION`: S3 frontend artifacts path
- **Output**: Frontend build artifacts (dist/)

##### BackendBuild
- **Project Name**: `BackendBuildProject`
- **Runtime**: Node.js 18
- **Buildspec**: `buildspec/backend/buildspec.yml`
- **Environment Variables**:
  - `ARTIFACT_LOCATION`: S3 backend artifacts path
- **Output**: Backend build artifacts

#### 3. Deploy Stage (Optional - Future)
Placeholder for ECS, Lambda, S3, or other deployment targets.

---

## 🔨 BuildSpec Files

### Frontend BuildSpec
**File**: `buildspec/frontend/buildspec.yml`

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - echo "Installing frontend dependencies..."
      - npm install

  pre_build:
    commands:
      - echo "Running linting and tests..."
      - npm run lint
      - npm run test -- --coverage

  build:
    commands:
      - echo "Building frontend..."
      - npm run build
      - echo "Build completed at $(date)"

  post_build:
    commands:
      - echo "Frontend build successful"

artifacts:
  files:
    - '**/*'
  base-directory: dist
  name: frontend-build-$(date +%Y%m%d-%H%M%S).zip

cache:
  paths:
    - 'node_modules/**/*'
```

### Backend BuildSpec
**File**: `buildspec/backend/buildspec.yml`

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - echo "Installing backend dependencies..."
      - npm install

  pre_build:
    commands:
      - echo "Running linting and tests..."
      - npm run lint
      - npm run test

  build:
    commands:
      - echo "Building backend..."
      - npm run build
      - echo "Build completed at $(date)"

  post_build:
    commands:
      - echo "Backend build successful"
      - npm run bundle

artifacts:
  files:
    - 'dist/**/*'
    - 'package*.json'
  name: backend-build-$(date +%Y%m%d-%H%M%S).zip

cache:
  paths:
    - 'node_modules/**/*'
```

---

## 🎯 Deploying the Pipeline

### Step 1: Synthesize CloudFormation template
```bash
cdk synth
```
This generates the CloudFormation template in `cdk.out/` directory.

### Step 2: Bootstrap CDK (first-time only)
```bash
cdk bootstrap aws://<ACCOUNT_ID>/us-east-1
```
This creates the necessary S3 bucket and IAM roles for CDK deployments.

### Step 3: Deploy the stack
```bash
cdk deploy CicdPipelineStack \
  --app "ts-node bin/cdk.ts" \
  --require-approval never
```

**Options**:
- `--profile <profile-name>`: Use specific AWS CLI profile
- `--region <region>`: Deploy to specific region
- `--require-approval always`: Require approval before deployment
- `--hotswap`: Faster deployment for development

### Step 4: Verify deployment
```bash
# Check CloudFormation stack status
aws cloudformation describe-stacks --stack-name CicdPipelineStack

# View pipeline in AWS Console
# Navigate to CodePipeline → Pipelines → Task3Pipeline
```

---

## 🧪 Testing the Pipeline

### Test 1: Manual Pipeline Execution
1. Go to AWS Console → CodePipeline
2. Select **Task3Pipeline**
3. Click **Release change**
4. Monitor execution through each stage

### Test 2: GitLab Push Trigger
1. Make changes to a feature branch in the GitLab repository
2. Create a merge request to `feature/pipeline`
3. Pipeline should trigger automatically (if webhook is configured)
4. Check CodeBuild logs for build progress

### Test 3: Verify Build Artifacts
```bash
# List artifacts in S3
aws s3 ls s3://PipelineArtifactBucket/

# Download specific artifact
aws s3 cp s3://PipelineArtifactBucket/<artifact-path> ./
```

### Test 4: Check CloudWatch Logs
```bash
# List build project logs
aws logs describe-log-groups --query 'logGroups[?contains(logGroupName, `CodeBuild`)]'

# View specific build logs
aws logs tail /aws/codebuild/FrontendBuildProject --follow
```

---

## 🧹 Destroying Resources

To clean up all resources created by this task:

```bash
cdk destroy CicdPipelineStack \
  --app "ts-node bin/cdk.ts" \
  --force
```

This removes:
- **CodePipeline**: `Task3Pipeline`
- **CodeBuild Projects**: `FrontendBuildProject`, `BackendBuildProject`
- **S3 Bucket**: `PipelineArtifactBucket` (with all contents)
- **IAM Roles & Policies**: Service roles and build role
- **CloudWatch Log Groups**: Build logs

### Optional: Delete CodeStar Connection
```bash
aws codestar-connections delete-connection \
  --connection-arn <ConnectionArn>
```

> **Warning**: Destroying the stack will delete the S3 artifact bucket and all stored artifacts. Download any important artifacts before proceeding.

---

## 📚 References

* [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
* [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
* [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
* [AWS CodeStar Connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html)
* [GitLab Integration with AWS](https://docs.gitlab.com/ee/integration/aws/)
* [CDK Best Practices](https://docs.aws.amazon.com/cdk/latest/guide/best_practices.html)

---

## 🔭 Next Steps / Improvements

1. **Add Testing Stage**: Integrate automated testing (Jest, SonarQube)
2. **Deploy Stage**: Add ECS service deployment or S3 static site hosting
3. **Approval Gates**: Implement manual approval for production deployments
4. **Notifications**: Configure SNS notifications for pipeline events
5. **Security Scanning**: Integrate SAST tools (Snyk, WhiteSource)
6. **Performance Optimization**: Cache dependencies in CodeBuild
7. **Multi-region Deployment**: Cross-region artifact replication

---

## 📞 Contact

- Email: hassan.u@dplit.com

> Task 3 provides a production-ready CI/CD pipeline framework using infrastructure-as-code best practices. This pipeline serves as the foundation for automated deployment workflows on AWS.
