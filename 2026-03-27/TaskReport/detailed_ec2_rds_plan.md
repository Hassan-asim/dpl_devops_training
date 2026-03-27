# EC2 & RDS Reserved Instance Strategy Plan

## DPL Infrastructure – Cost Optimization Plan

| Document Property | Value |
|-------------------|-------|
| **Date** | 27 March 2026 |
| **Service Period** | 1 December 2025 → 30 November 2027 (24 months) |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [What Are AWS Reserved Instances?](#2-what-are-aws-reserved-instances)
3. [AWS Reserved Instance Rules Explained](#3-aws-reserved-instance-rules-explained)
4. [Current Infrastructure Overview](#4-current-infrastructure-overview)
5. [Service Timeline & Cost Analysis](#5-service-timeline--cost-analysis)
6. [Complete Instance Cost Breakdown](#6-complete-instance-cost-breakdown)
7. [Multiple Strategy Options](#7-multiple-strategy-options)
8. [Recommendations](#8-recommendations)
9. [Implementation Timeline](#9-implementation-timeline)

---

## 1. Executive Summary

### 1.1 Purpose

This document outlines a strategic plan to **reduce infrastructure costs** for our AWS cloud services while ensuring **uninterrupted operation** of all systems through November 2027.

### 1.2 What We Are Optimizing

| Resource Type | Description | Quantity |
|---------------|-------------|----------|
| **EC2 Instances** | Virtual servers that run our applications (frontend, backend, APIs) | 9 instances |
| **RDS Instances** | Managed database servers (PostgreSQL) | 2 instances |
| **Total** | | **11 instances** |

### 1.3 The Challenge

Our service contract runs for **24 months** (December 2025 – November 2027), but AWS does **not offer 2-year Reserved Instance contracts**. AWS only provides:

| Term Length | Availability |
|-------------|--------------|
| 1-year Reserved Instances | Available |
| 2-year Reserved Instances | **Not Available** |
| 3-year Reserved Instances | Available |

### 1.4 The Solution

This plan presents **multiple purchasing strategies** to cover our 24-month service period in the most cost-effective way possible, with clear recommendations based on budget availability and business needs.

### 1.5 Key Financial Insight

By switching from On-Demand pricing to Reserved Instances, we can achieve **significant cost savings** (up to 40-60% discount) on our AWS infrastructure costs.

---

## 2. What Are AWS Reserved Instances?

### 2.1 For Non-Technical Stakeholders

Think of Reserved Instances (RIs) like a **mobile phone contract**:

| Payment Type | How It Works | Best For |
|--------------|--------------|----------|
| **On-Demand** | Pay-as-you-go, like prepaid mobile credit. Higher per-hour cost, but no commitment. | Short-term, unpredictable workloads |
| **Reserved Instance** | Commit to 1 or 3 years for a much lower hourly rate. Like a postpaid contract with better rates. | Long-term, stable workloads |

### 2.2 For Technical Stakeholders

Reserved Instances provide a **capacity reservation** and **billing discount** applied to instance usage in your AWS account. Key characteristics:

- **Billing Discount**: Significant reduction (up to 72%) compared to On-Demand pricing
- **Capacity Reservation**: Guaranteed EC2 capacity in a specific Availability Zone (when AZ-scoped)
- **Scope**: Can be Regional (flexible across AZs) or Zonal (specific AZ)

---

## 3. AWS Reserved Instance Rules Explained

### 3.1 Term Length Options

| Term | Duration | Availability |
|------|----------|--------------|
| 1-Year | 12 months | Available |
| 2-Year | 24 months | **Not Available** |
| 3-Year | 36 months | Available |

> **Important:** AWS does **not** offer 2-year Reserved Instances. This is why we need a strategic approach to cover our 24-month service period.

### 3.2 Payment Options

| Payment Type | Upfront Cost | Monthly Cost | Total Savings |
|--------------|--------------|--------------|---------------|
| **All Upfront** | 100% at purchase | $0 | Maximum discount |
| **Partial Upfront** | ~50% at purchase | Reduced monthly rate | Moderate discount |
| **No Upfront** | $0 at purchase | Higher monthly rate | Lower discount |

> **Recommendation:** **All Upfront** provides the best overall savings if budget allows.

### 3.3 Reserved Instance Types

| Type | Flexibility | Discount Level | Use Case |
|------|-------------|----------------|----------|
| **Standard RI** | Cannot change instance type or family | Higher discount (up to 72%) | Stable, predictable workloads |
| **Convertible RI** | Can exchange for different instance type/family | Lower discount (up to 54%) | Workloads that may need changes |

### 3.4 Important Rules to Understand

#### 3.4.1 No Retroactive Pricing

Reserved Instances **cannot be applied to past usage**. Any costs incurred before purchasing an RI remain billed at On-Demand rates.

**Example:**

| Period | Status | Billing |
|--------|--------|---------|
| December 2025 – March 2026 | Past | Already billed at On-Demand rates |
| March 2026 onward | Future | Can apply RI pricing |

> **Note:** Cannot "go back" and apply RI pricing to months already billed.

#### 3.4.2 Regional vs. Zonal Scope

| Scope | Description | Use Case |
|-------|-------------|----------|
| **Regional RI** | Applies to any instance of that type in the entire AWS region | Flexible workloads across Availability Zones |
| **Zonal RI** | Applies only to a specific Availability Zone | Workloads requiring guaranteed capacity |

---

## 4. Current Infrastructure Overview

### 4.1 Infrastructure Summary

Our infrastructure consists of **11 instances** across three categories:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DPL INFRASTRUCTURE                           │
│                      (11 Total Instances)                       │
├─────────────────────┬─────────────────────┬─────────────────────┤
│   Database (RDS)    │   Application (EC2) │   Support (EC2)     │
│      2 instances    │      6 instances    │      3 instances    │
└─────────────────────┴─────────────────────┴─────────────────────┘
```

### 4.2 Database Servers (RDS - PostgreSQL)

| Instance Name | Purpose | Size |
|---------------|---------|------|
| `postgres-instance` | Development/Testing database | Small (micro) |
| `prod-postgres-instance` | Production database | Large (xlarge) |

### 4.3 Application Servers (EC2)

| Instance Name | Purpose | Size |
|---------------|---------|------|
| `prod-backend-app` | Production backend API | Large (xlarge) |
| `prod-frontend-app` | Production frontend web server | Large (xlarge) |
| `dev-backend-app` | Development backend | Medium |
| `dev-frontend-app` | Development frontend | Medium |
| `uat-backend-app` | User Acceptance Testing backend | Medium |
| `uat-frontend-app` | User Acceptance Testing frontend | Medium |

### 4.4 Support Infrastructure (EC2)

| Instance Name | Purpose | Size |
|---------------|---------|------|
| `db-bastion` | Secure database access gateway | Very Small (micro) |
| `Nat-instance` | Network address translation for outbound traffic | Very Small (nano) |
| `FileScanApiInstance` | File scanning service API | Small (medium) |

---

## 5. Service Timeline & Cost Analysis

### 5.1 Timeline Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SERVICE PERIOD: 24 MONTHS                             │
│                     December 2025 → November 2027                           │
├──────────────────────┬──────────────────────────┬───────────────────────────┤
│   Dec 2025           │   Mar 2026               │   Mar 2027     │  Nov 2027│
│   (Contract Start)   │   (Today)                │                │  (End)   │
├──────────────────────┼──────────────────────────┼────────────────┼──────────┤
│  ON-DEMAND           │   1st RI PERIOD          │  2nd RI PERIOD │          │
│  (Past - Paid)       │   (12 months)            │  (8 months)    │          │
│  4 months            │                          │                │          │
└──────────────────────┴──────────────────────────┴────────────────┴──────────┘
```

### 5.2 Detailed Timeline Breakdown

| Period | Duration | Status | Cost Type | Explanation |
|--------|----------|--------|-----------|-------------|
| **Dec 2025 – Mar 2026** | 4 months | Past | On-Demand | Already incurred and billed. Cannot apply RI pricing retroactively. |
| **Mar 2026 – Mar 2027** | 12 months | Current | Reserved Instance | First RI purchase covers this period. |
| **Mar 2027 – Nov 2027** | 8 months | Future | Reserved Instance or On-Demand | Second RI or On-Demand, depending on strategy chosen. |
| **Dec 2027 onward** | N/A | Beyond Service | N/A | Not required for current contract. |

---

## 6. Complete Instance Cost Breakdown

### 6.1 Cost Comparison Table

All costs in **USD ($)**.

| # | Instance Name | Type | Instance Family | Monthly On-Demand | 1-Year RI (All Upfront) | 3-Year RI (All Upfront) |
|---|---------------|------|-----------------|-------------------|-------------------------|-------------------------|
| 1 | `db-bastion` | EC2 | t4g.micro | $6.13 | $43.00 | $83.00 |
| 2 | `FileScanApiInstance` | EC2 | t3.medium | $30.37 | $213.00 | $411.00 |
| 3 | `Nat-instance` | EC2 | t3.nano | $3.80 | $27.00 | $51.00 |
| 4 | `dev-backend-app` | EC2 | t4g.medium | $24.53 | $172.00 | $332.00 |
| 5 | `prod-backend-app` | EC2 | t4g.xlarge | $98.11 | $689.00 | $1,327.00 |
| 6 | `uat-backend-app` | EC2 | t4g.medium | $24.53 | $172.00 | $332.00 |
| 7 | `dev-frontend-app` | EC2 | t4g.medium | $24.53 | $172.00 | $332.00 |
| 8 | `uat-frontend-app` | EC2 | t4g.medium | $24.53 | $172.00 | $332.00 |
| 9 | `prod-frontend-app` | EC2 | t4g.xlarge | $98.11 | $689.00 | $1,327.00 |
| 10 | `postgres-instance` | RDS | db.t4g.micro | $13.98 | $122.60 | $226.60 |
| 11 | `prod-postgres-instance` | RDS | db.t4g.xlarge | $190.64 | $1,544.60 | $3,219.60 |

### 6.2 Total Cost Summary

| Pricing Model | Total Annual Cost | 2-Year Equivalent | Savings vs On-Demand |
|---------------|-------------------|-------------------|----------------------|
| **On-Demand** (baseline) | $6,138.28 | $14,731.87 | — |
| **1-Year RI** (All Upfront) | $3,839.20 | $7,678.40 (×2) | ~48% savings |
| **3-Year RI** (All Upfront) | $7,643.20 | $5,095.47 (prorated) | ~48% savings |

> **Note:** The 3-Year RI total is shown as a 3-year commitment. When prorated for 2 years, the cost is approximately: $7,643.20 ÷ 3 × 2 = **$5,095.47** (but it's not possible to just pay for 2 years in a 3-year plan )

### 6.3 Key Observation

Buying **two consecutive 1-year RIs** provides nearly the same cost efficiency as a **3-year RI**

---

## 7. Multiple Strategy Options

### 7.1 Option A – Two Consecutive 1-Year RIs (Recommended)

#### How It Works

1. **First RI Purchase (March 2026):** Buy 1-year Reserved Instances for all instances
2. **Second RI Purchase (March 2027):** Buy another 1-year RI to cover remaining 8 months (March – November 2027)

#### Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OPTION A: TWO CONSECUTIVE 1-YEAR RIs                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Mar 2026                    Mar 2027              Nov 2027                │
│      │                           │                     │                    │
│      │◄──── 1st RI (12 mo) ────►│◄─ 2nd RI (8 mo) ───►│                    │
│      │                           │                     │                    │
│      └─────────────────────────────────────────────────┘                    │
│                    Total Coverage: 20 months                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Financial Breakdown

| Cost Component | Amount |
|----------------|--------|
| First 1-Year RI (All Upfront) | $3,839.20 |
| Second 1-Year RI (All Upfront) | $3,839.20 |
| **Total RI Cost** | **$7,678.40** |
| Less: Unused months (Nov 2027 – Mar 2028) | -$1,279.73 |
| **Effective Cost for 20 Months** | **~$6,398.67** |

#### Pros and Cons

| Pros | Cons |
|------|------|
| Maximum cost savings for the 24-month period | Requires two separate purchase transactions |
| Continuous coverage with no gaps | Need to remember to purchase second RI before first expires |
| Flexibility to adjust instance types after first year if needed | Past 4 months (Dec 2025 – Mar 2026) remain On-Demand |
| No commitment beyond service period | |

#### Best For

Organizations with **adequate budget** seeking **maximum savings** without long-term commitment.

---

### 7.2 Option B – 1-Year RI + Remaining Months On-Demand

#### How It Works

1. **First RI Purchase (March 2026):** Buy 1-year Reserved Instances
2. **Remaining Period (March 2027 – November 2027):** Pay On-Demand rates for 8 months

#### Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              OPTION B: 1-YEAR RI + REMAINING ON-DEMAND                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Mar 2026                    Mar 2027              Nov 2027                │
│      │                           │                     │                    │
│      │◄──── 1st RI (12 mo) ────►│◄─ On-Demand (8 mo) ─►│                    │
│      │                           │                     │                    │
│      └─────────────────────────────────────────────────┘                    │
│                    Total Coverage: 20 months                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Financial Breakdown

| Cost Component | Amount |
|----------------|--------|
| First 1-Year RI (All Upfront) | $3,839.20 |
| Remaining 8 Months On-Demand | $4,092.19 |
| **Total Cost** | **$7,931.39** |

#### Pros and Cons

| Pros | Cons |
|------|------|
| Lower upfront payment (only one RI purchase) | Higher total cost compared to Option A |
| No need to manage second RI purchase | No RI discount for final 8 months |
| Flexibility to scale down or change infrastructure in final 8 months | |

#### Best For

Organizations with **budget constraints** or those anticipating **infrastructure changes** in the final year.

---

### 7.3 Option C – 3-Year RI Starting Now

#### How It Works

Purchase 3-year Reserved Instances starting March 2026, covering through March 2029.

#### Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OPTION C: 3-YEAR RI STARTING NOW                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Mar 2026                                          Mar 2029                │
│      │                                                 │                     │
│      │◄──────────── 3-Year RI (36 mo) ───────────────►│                     │
│      │                                                 │                     │
│      ├───────────────────────────────────────┤                                │
│      │   Our Service Period (20 months)      │                                │
│      └───────────────────────────────────────┘                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Financial Breakdown

| Cost Component | Amount |
|----------------|--------|
| 3-Year RI (All Upfront) | $7,643.20 |
| Prorated for 24 months | $5,095.47 |
| Unused value (Nov 2027 – Mar 2029) | ~$2,547.73 |

#### Pros and Cons

| Pros | Cons |
|------|------|
| Lowest effective monthly rate | Highest upfront payment |
| Single purchase transaction | Overpayment for ~16 months beyond service period |
| Coverage extends beyond service period (can be sold on RI Marketplace if needed) | Long-term commitment beyond contract end date |

#### Best For

Organizations planning to **extend services beyond November 2027** or those with **excess capital** seeking maximum long-term savings.

---

### 7.4 Option D – Hybrid Approach (Standard + Convertible RIs)

#### How It Works

| Instance Category | RI Type | Purpose |
|-------------------|---------|---------|
| **Production instances** (prod-backend, prod-frontend, prod-postgres) | Standard RI | Maximum discount |
| **Development/Test instances** (dev, uat, bastion, nat, filescan) | Convertible RI | Flexibility |

#### Financial Breakdown (Estimated)

| Instance Category | RI Type | Cost (1-Year) |
|-------------------|---------|---------------|
| Production (3 instances) | Standard | $2,922.60 |
| Dev/Test (8 instances) | Convertible | ~$1,150.00 |
| **Total First Year** | | **~$4,072.60** |

#### Pros and Cons

| Pros | Cons |
|------|------|
| Maximum discount on stable production workloads | Slightly higher cost than Option A (Convertible RIs have lower discounts) |
| Flexibility to change instance types for dev/test environments | More complex to manage and track |
| Balances cost savings with operational flexibility | |

#### Best For

Organizations expecting **architecture changes** in development environments or those wanting to **future-proof** their infrastructure decisions.

---

## 8. Recommendations

### 8.1 Primary Recommendation: Option A – Two Consecutive 1-Year RIs

#### Why Option A?

| Factor | Rating | Explanation |
|--------|--------|-------------|
| **Cost Efficiency** | 5/5 | Maximum savings for the 24-month period |
| **Budget Management** | 4/5 | Two payments spread over time |
| **Flexibility** | 4/5 | Can adjust after first year if needed |
| **Simplicity** | 4/5 | Easy to understand and execute |
| **Risk** | 5/5 | No long-term commitment beyond contract |

#### Implementation Steps

**Step 1: Immediate Action (March 2026)**

| Action | Details |
|--------|---------|
| Purchase | 1-year All-Upfront RIs for all 11 instances |
| Total upfront cost | **$3,839.20** |

**Step 2: Reminder Setup**

| Action | Details |
|--------|---------|
| Set calendar reminder | **February 2027** (1 month before expiry) |
| Review | Instance utilization and adjust if needed |

**Step 3: Second Purchase (March 2027)**

| Action | Details |
|--------|---------|
| Purchase | Second 1-year All-Upfront RIs |
| Total upfront cost | **$3,839.20** |
| Note | Final 4 months (Nov 2027 – Mar 2028) will be unused |

---

### 8.2 Alternative Recommendations

| Scenario | Recommended Option | Reason |
|----------|-------------------|--------|
| Limited budget now | Option B | Lower immediate cash outlay |
| Planning extension beyond 2027 | Option C | Long-term commitment makes sense |
| Expecting architecture changes | Option D | Convertible RIs provide flexibility |

---

## 9. Implementation Timeline

### 9.1 Phase 1: Immediate Actions (March 2026)

| Week | Action | Responsible Party |
|------|--------|-------------------|
| Week 1 | Review and approve this plan | Hazar / Management |
| Week 2 | Verify instance details in AWS Console | Technical Team |
| Week 3 | Process payment for first RI purchase | Finance Team |
| Week 4 | Purchase 1-year All-Upfront RIs | Technical Team |

### 9.2 Phase 2: Monitoring (April 2026 – February 2027)

| Frequency | Action |
|-----------|--------|
| Monthly | Review RI utilization reports in AWS Cost Explorer |
| Quarterly | Verify all instances are covered by RIs |
| February 2027 | Receive alert for upcoming RI expiration |

### 9.3 Phase 3: Second RI Purchase (March 2027)

| Week | Action |
|------|--------|
| Week 1 | Review current infrastructure (any changes?) |
| Week 2 | Process payment for second RI purchase |
| Week 3 | Purchase second 1-year All-Upfront RIs |
| Week 4 | Confirm RI coverage is active |

### 9.4 Phase 4: Service Completion (November 2027)

| Item | Details |
|------|---------|
| **Contract End Date** | 30 November 2027 |
| **RI Status** | Second RI still active (until March 2028) |
| **Options** | Continue service, sell unused RI on Marketplace, or let expire |
