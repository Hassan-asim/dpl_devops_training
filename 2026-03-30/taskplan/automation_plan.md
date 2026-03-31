# Automate Stop/Start of `db-bastion` EC2 Instance via CDK + SSM

## Objective

Automate lifecycle management of the `db-bastion` EC2 instance:

- **Stop** the instance daily at midnight (PKT)
- **Start** the instance daily at a defined time (e.g., morning)

---

## Approach

Use **AWS CDK** with:

- **Amazon EventBridge** for scheduling
- **AWS Systems Manager Automation** with AWS-managed runbooks:
  - `AWS-StopEC2Instance`
  - `AWS-StartEC2Instance`

---

## Implementation Plan

### 1. Identify Target Instance

- Retrieve the EC2 **Instance ID** for `db-bastion`

---

### 2. Create CDK Stack

Add a new stack:

```typescript
db-bastion-schedule-stack
```

---

### 3. Configure IAM Role

Create a role for EventBridge to trigger SSM Automation with permissions:

- `ssm:StartAutomationExecution`
- `ec2:StopInstances`
- `ec2:StartInstances`

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

### 5. Create Start Schedule

- **Example start time:** 9 AM PKT → 04:00 UTC

```typescript
cron(0 4 * * ? *)
```

- **Target:**
  - SSM Document: `AWS-StartEC2Instance`
  - Parameter:

```typescript
InstanceId = <db-bastion-instance-id>
```

---

### 6. Link Components

- EventBridge rules use IAM role
- Each rule triggers corresponding SSM Automation document

---

### 7. Deploy

```bash
cdk deploy
```

---

## Architecture Diagram

```
┌─────────────────────┐      ┌──────────────────────┐      ┌─────────────────────┐
│   EventBridge       │      │   SSM Automation     │      │   EC2 Instance      │
│   (Schedule)        │ ───► │   (Runbooks)         │ ───► │   (db-bastion)      │
│                     │      │                      │      │                     │
│ • Stop: 19:00 UTC   │      │ • AWS-StopEC2Instance│      │ • Start/Stop        │
│ • Start: 04:00 UTC  │      │ • AWS-StartEC2Instance│     │ • Instance ID       │
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

| Action | Pakistan Time (PKT) | UTC Time | Cron Expression |
|--------|---------------------|----------|-----------------|
| Stop   | 12:00 AM (Midnight) | 19:00    | `cron(0 19 * * ? *)` |
| Start  | 9:00 AM             | 04:00    | `cron(0 4 * * ? *)` |

