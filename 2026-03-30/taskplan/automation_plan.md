# Automate Stop of `db-bastion` EC2 Instance via CDK + SSM

## Objective

Automate lifecycle management of the `db-bastion` EC2 instance:

- **Stop** the instance daily at midnight (PKT) if it is running

---

## Approach

Use **AWS CDK** with:

- **Amazon EventBridge** for scheduling
- **AWS Systems Manager Automation** with AWS-managed runbook:
  - `AWS-StopEC2Instance`

---

## Implementation Plan

### 1. Identify Target Instance

- Retrieve the EC2 **Instance ID** for `db-bastion`

---

### 2. Create CDK Stack

Add a new stack:

```typescript
db-bastion-stop-stack
```

---

### 3. Configure IAM Role

Create a role for EventBridge to trigger SSM Automation with permissions:

- `ssm:StartAutomationExecution`
- `ec2:StopInstances`

---

### 4. Create Stop Schedule

- **EventBridge cron** (PKT midnight → UTC):

```typescript
cron(0 19 * * ? *)
```

- **Target:**
  - SSM Document: `AWS-StopEC2Instance`
  - Parameter:

```typescript
InstanceId = <db-bastion-instance-id>
```

---

### 5. Link Components

- EventBridge rule uses IAM role
- Rule triggers SSM Automation document

---

### 6. Deploy

```bash
cdk deploy
```

---

## Architecture Diagram

```
┌─────────────────────┐      ┌──────────────────────┐      ┌─────────────────────┐
│   EventBridge       │      │   SSM Automation     │      │   EC2 Instance      │
│   (Schedule)        │ ───► │   (Runbook)          │ ───► │   (db-bastion)      │
│                     │      │                      │      │                     │
│ • Stop: 19:00 UTC   │      │ • AWS-StopEC2Instance│      │ • Stop if running   │
└─────────────────────┘      └──────────────────────┘      └─────────────────────┘
         │                           │
         │                           │
         ▼                           ▼
┌─────────────────────┐      ┌──────────────────────┐
│   IAM Role          │      │   CloudWatch Logs    │
│   (Permissions)     │      │   (Execution Logs)   │
└─────────────────────┘      └──────────────────────┘
```

---

## Time Zone Conversion Table

| Action | Pakistan Time (PKT) | UTC Time | Cron Expression      |
| ------ | ------------------- | -------- | -------------------- |
| Stop   | 12:00 AM (Midnight) | 19:00    | `cron(0 19 * * ? *)` |

