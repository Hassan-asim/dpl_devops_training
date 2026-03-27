<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • EC2 Reserved Instance Strategy Planning & Infrastructure Cost Analysis</h3>

---

## 🎯 Objective Recap
- Complete ECS troubleshooting course progression.
- Create comprehensive EC2 & RDS instance pricing table with On-Demand and Reserved Instance options.
- Research and develop strategic Reserved Instance purchasing plan aligned with DPL service delivery timeline (Dec 2025 - Nov 2027).
- Assist with Nova Via environment variable configuration inquiry.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** EC2, RDS, Reserved Instances, Cost Explorer
- **Documentation:** AWS Reserved Instances User Guide

---

## 📚 Notes & Key Learnings

### 1. ECS Troubleshooting Course Continuation
- Continued "Troubleshooting: Amazon Elastic Container Service" course enrollment.
- Building upon previous day's progress.
- Focusing on ECS service diagnostics and container health monitoring.

### 2. EC2 & RDS Instance Pricing Table Creation
- Created comprehensive pricing table for all infrastructure instances.
- Included EC2 and RDS instances across dev, uat, and prod environments.
- Provided cost comparison: On-Demand vs 1-Year Reserved vs 3-Year Reserved.

**Instance Table Created:**

| Name | Type | Family | Current Monthly On-Demand ($) | 1-Year Reserved ($, All Upfront) | 3-Year Reserved ($, All Upfront) |
|------|------|--------|-------------------------------|----------------------------------|----------------------------------|
| db-bastion | t4g.micro | t4g | 6.13 | 43 | 83 |
| FileScanApiInstance | t3.medium | t3 | 30.37 | 213 | 411 |
| Nat-instance | t3.nano | t3 | 3.8 | 27 | 51 |
| dev-backend-app | t4g.medium | t4g | 24.53 | 172 | 332 |
| prod-backend-app | t4g.xlarge | t4g | 98.11 | 689 | 1327 |
| uat-backend-app | t4g.medium | t4g | 24.53 | 172 | 332 |
| dev-frontend-app | t4g.medium | t4g | 24.53 | 172 | 332 |
| uat-frontend-app | t4g.medium | t4g | 24.53 | 172 | 332 |
| prod-frontend-app | t4g.xlarge | t4g | 98.11 | 689 | 1327 |
| postgres-instance | db.t4g.micro | t4g | 13.98 | 122.6 | 226.6 |
| prod-postgres-instance | db.t4g.xlarge | t4g | 190.64 | 1544.6 | 3219.6 |

### 3. Nova Via Environment Variable Inquiry
- Afifa requested setting `MEDIA_CDN_DOMAIN` to `video-cdn-dev.novalifeapp.com`.
- Consulted with Hazar regarding implementation approach.
- Finding: Value already set in CloudFront distribution; code already configured.
- Communicated findings to Afifa; she will verify from her end.

---

## 📋 Reserved Instance Strategy Research

### AWS Reserved Instance Rules & Notes

| Feature | Detail |
|---------|--------|
| Term length | 1-year or 3-year only. **2-year RIs do not exist**. |
| Payment options | All Upfront, Partial Upfront, No Upfront. All Upfront provides maximum discount. |
| Standard vs Convertible | Standard: higher discount, cannot change instance type/family. Convertible: can change type/family, smaller discount. |
| Retroactive pricing | RI savings **cannot be applied retroactively**; On-Demand costs already incurred remain billed. |
| Scope | Regional or AZ-specific; regional allows automatic instance size flexibility. |

### Service Timeline & Gap Analysis

| Period | Status | Cost Type | Notes |
|--------|--------|-----------|-------|
| Dec 2025 – Mar 2026 | Past | On-Demand | Retroactive coverage: cannot buy RIs for past months; already billed at On-Demand rates |
| Mar 2026 – Nov 2026 | Current | Option-dependent | RI purchases can start now; first RI covers until Mar/Nov 2027 depending on plan |
| Dec 2026 – Nov 2027 | Future | Option-dependent | Second RI or On-Demand covers remaining months |
| Dec 2027 onward | Beyond service period | N/A | Not needed |

---

## 🧪 Multiple RI Strategy Options

### Option A – Two Consecutive 1-Year RIs (Recommended)
- **Strategy:** Buy first 1-year RI now (Mar 2026 → Mar 2027), second 1-year RI before expiry (Mar 2027 → Nov 2027).
- **Pros:** Maximizes discount; ensures continuous coverage; flexible for architecture changes.
- **Cons:** Retroactive coverage (Dec 2025 → Mar 2026) still billed On-Demand.
- **Implementation:** All-Upfront payment for both 1-year periods.

**Cost Example (prod-postgres-instance):**
- 1-year upfront: $1544.6 → total for 2 sequential RIs: $1544.6 × 2 = $3089.2

---

### Option B – 1-Year RI + Remaining Months On-Demand
- **Strategy:** Buy first 1-year RI now; pay On-Demand for remaining months to match timeline.
- **Pros:** Lower immediate cash outlay; partial cost saving.
- **Cons:** Less cost-effective than consecutive 1-year RIs; monthly billing for remaining months.
- **Use Case:** If budget constraints prevent buying two upfront RIs.

---

### Option C – 3-Year RI Starting Now
- **Strategy:** Buy 3-year RI starting Mar 2026 → Mar 2029.
- **Pros:** Maximum discount on AWS RIs; covers service period and beyond.
- **Cons:** Overpays for months beyond Nov 2027 (extra ~16 months); large upfront payment required.
- **Use Case:** If long-term planning beyond 2027 is desired and cash flow allows.

---

### Option D – Mix of Convertible & Standard RIs
- **Strategy:** Use Standard RIs for predictable instances (prod) and Convertible RIs for flexible/dev instances.
- **Pros:** Balances cost savings with flexibility in instance family/type.
- **Cons:** Convertible RIs offer slightly smaller discount than Standard.

---

## 📝 Recommendations Summary

| Priority | Recommendation | Rationale |
|----------|----------------|-----------|
| 1 | **Option A – Two consecutive 1-year All-Upfront RIs** | Covers entire required service period with maximum cost efficiency |
| 2 | **Option B** | Alternative if cash-limited; buy 1-year RI, pay On-Demand for remainder |
| 3 | **Option C** | Consider only if extending services beyond Nov 2027 |
| 4 | **Convertibles for dev/test** | Use for instances where instance families may change |

---

## 📚 Training & Professional Development

**1. ECS Troubleshooting Course:**
- Course: "Troubleshooting: Amazon Elastic Container Service"
- Progress: Continued advancement through course modules.
- Focus: ECS service diagnostics, task failures, and container health monitoring.

**2. AWS Reserved Instances Documentation Study:**
- Document: [EC2 Reserved Instances Overview](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)
- Key Learning: 2-year RIs do not exist; only 1-year and 3-year terms available.
- Applied learning to develop comprehensive cost optimization strategy.

---

## 🖼️ Evidence & Screenshots

### Instance Pricing Table
- ![EC2 RDS Pricing Table](./images/ec2_rds_pricing_table.png) — Comprehensive pricing comparison for all instances

### Reserved Instance Strategy Document
- ![RI Strategy Options](./images/ri_strategy_options.png) — Multiple option comparison chart
- ![Timeline Chart](./images/timeline_chart.png) — RI purchase timeline visualization

---

## ✅ Daily Summary
- Continued ECS troubleshooting course progression, advancing through diagnostic modules.
- Created comprehensive EC2 & RDS instance pricing table with On-Demand and Reserved Instance comparisons.
- Researched AWS Reserved Instance rules and developed strategic purchasing plan for DPL infrastructure.
- Analyzed four RI strategy options; recommended two consecutive 1-year All-Upfront RIs for cost efficiency.
- Assisted Afifa with Nova Via environment variable inquiry; coordinated with Hazar for clarification.
- Delivered comprehensive RI strategy plan document aligned with service delivery timeline (Dec 2025 - Nov 2027).
- Next steps: Await feedback on RI strategy; continue ECS troubleshooting course completion; support infrastructure cost optimization implementation.

Made by Sufi Hassan Asim — 2026-03-27
