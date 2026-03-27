<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • ECS Troubleshooting Course Continuation & SAM CLI Experiments</h3>

---

## 🎯 Objective Recap
- Continue ECS troubleshooting course progression.
- Practice and experiment with AWS SAM CLI to validate console-based findings.
- Await task assignments from team lead.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** SAM, CloudFormation, IAM, Lambda
- **AWS CLI:** SAM CLI for local experimentation

---

## 📚 Notes & Key Learnings

### 1. ECS Troubleshooting Course Continuation
- Continued "Troubleshooting: Amazon Elastic Container Service" course enrollment.
- Building upon previous day's progress (Module 3).
- Focusing on ECS diagnostic techniques and common failure patterns.

### 2. SAM CLI Practice & Experimentation
- Practiced with AWS SAM CLI to validate console-based experiment findings.
- Compared CLI results with console-based deployment behaviors.
- Verified consistency between CLI and console deployment patterns.

---

## 🧪 Experiment Log

### Experiment 4: SAM CLI vs Console Behavior Validation

**Objective:**
- Validate if SAM CLI produces same results as console-based deployments.
- Confirm template-driven behavior consistency across interfaces.

**Steps:**
1. Used SAM CLI to deploy IAM role with inline policy.
2. Made manual modifications via console.
3. Redeployed using SAM CLI with template changes.
4. Compared results with previous console-based experiments.

**Result:**
- CLI and console produced identical behavior.
- Template-driven deployments overwrite manual changes regardless of interface.
- No discrepancies found between CLI and console methods.

**Conclusion:**
- SAM behavior is consistent across CLI and console interfaces.
- Template-driven infrastructure management is reliable regardless of deployment method.

---

## 📋 Key Takeaways

| Observation | Finding |
|-------------|---------|
| CLI vs Console | Same behavior, no differences |
| Template-driven deployments | Consistent overwrite behavior |
| Manual changes | Temporary regardless of interface |
| Best practice | Use CLI for reproducible, scriptable deployments |

### Best Practices Reinforced:
1. SAM CLI provides reproducible, automatable deployments.
2. Console is useful for quick experiments but not for production.
3. Template changes always override manual modifications.
4. CLI workflows are preferred for CI/CD integration.

---

## 📝 Task Coordination

- Reached out to Hazar for task assignments.
- Awaiting response and further instructions.
- Utilized available time for skill development and experimentation.

---

## 📚 Training & Professional Development

**1. ECS Troubleshooting Course:**
- Course: "Troubleshooting: Amazon Elastic Container Service"
- Progress: Continued from Module 3, advancing through course content.
- Focus: ECS service diagnostics, task failures, and container health monitoring.

**2. SAM CLI Hands-on Practice:**
- Practiced SAM CLI commands for stack deployment and management.
- Validated console experiment findings using CLI interface.
- Reinforced understanding of template-driven infrastructure behavior.

---

## ✅ Daily Summary
- Continued ECS troubleshooting course progression, building expertise in container service diagnostics.
- Conducted SAM CLI experiments to validate console-based findings from previous day.
- Confirmed consistent behavior between CLI and console deployment methods.
- Reinforced best practices for template-driven infrastructure management.
- Reached out to Hazar for task assignments; awaiting response.
- Next steps: Complete ECS troubleshooting course; await task assignments; apply SAM CLI learnings to production workflows.

Made by Sufi Hassan Asim — 2026-03-26
