# CodeCommit to GitLab Migration Plan and Guide

## Overview
We will migrate all repositories from AWS CodeCommit to GitLab. Pipelines will remain in AWS CodePipeline for now and will be updated after code migration is complete.

## Responsibilities

### My Responsibilities
- Create all repositories in GitLab. Repository names: mm-backend, mm-enterprise, mm-cms, mm-event, mm-checkout. Created.

### Your Responsibilities
- Perform the repository migration from CodeCommit to GitLab.
- We will execute the migration when you are available.

## Important Notes
- GitLab repository names may differ from CodeCommit names.
- This does not affect migration or pipeline integration.
- CodePipeline will work with GitLab as long as it is configured with the correct repository URL and branch.

## Migration Strategy
- Start with one repository first.
- Validate migration (branches, commits, tags).
- Proceed with remaining repositories.

## Standard Repository Migration Steps

Example values used below:
- CodeCommit repo: complaint-service
- GitLab repo: complaint-service-v2
- Region: us-east-1
- GitLab group: my-group

### Step 1: Clone Repository from CodeCommit Using Mirror Mode
```
git clone --mirror https://git-codecommit.us-east-1.amazonaws.com/v1/repos/complaint-service
cd complaint-service.git
```

### Step 2: Add GitLab as Remote
```
git remote add gitlab https://gitlab.com/my-group/complaint-service-v2.git
```

### Step 3: Push All Data to GitLab
```
git push --mirror gitlab
```

### Step 4: Verify in GitLab
- All branches are present.
- Commit history is intact.
- Tags are available.

## Special Case: Repository with .env in Commit History

This repository must not be mirrored.

Example values:
- CodeCommit repo: user-service
- GitLab repo: user-service-clean

### Step 1: Clone Repository Normally
```
git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/user-service
cd user-service
```

### Step 2: Remove Existing Git History
```
rm -rf .git
```

### Step 3: Initialize Fresh Repository
```
git init
git add .
git commit -m "Initial clean commit"
```

### Step 4: Push to GitLab
```
git remote add gitlab https://gitlab.com/my-group/user-service-clean.git
git push -u gitlab main
```

## Post Migration (Next Phase)
- Update CodePipeline to use GitLab as the source.
- Likely using CodeStar connection or webhook integration.
- Pipeline trigger on push to main branch will be configured after migration.

## Timeline
- GitLab repository creation: completed.
- Migration: when you are available.
- Pipeline integration: after successful migration.
