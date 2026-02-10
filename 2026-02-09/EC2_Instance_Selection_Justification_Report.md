# EC2 Instance Selection Justification Report

**Project:** Complaint Management System (CMS)\
**Purpose:** Provide technical and cost-based reasoning for optimized
EC2 instance selections and comparison with alternative options

------------------------------------------------------------------------

## 1. Selection Methodology

Instance types were evaluated using the following criteria:

-   Compliance with RFP minimum vCPU and RAM requirements\
-   Workload behavior (burstable vs steady utilization)\
-   Cost comparison across AWS instance families\
-   Performance headroom for scaling and service consolidation\
-   Suitability for production vs non-production environments

Selections prioritize requirement compliance first, then cost
efficiency, and finally performance headroom where beneficial.

------------------------------------------------------------------------

## 2. Production Backend --- prod-backend-app

**RFP Requirement:** 4 vCPU, 8 GB RAM

  Instance Type   vCPU   RAM     1yr Reserved (\$/mo)   Evaluation
  --------------- ------ ------- ---------------------- -------------
  t3a.xlarge      4      16 GB   65                     Selected
  m6i.xlarge      4      16 GB   72                     Alternative

### t3a.xlarge --- Selected

-   Meets CPU requirement exactly\
-   Provides double the required RAM, improving caching and application
    stability\
-   Burstable CPU model fits API workloads with variable demand\
-   AMD-based pricing provides lower cost compared to Intel equivalents\
-   Suitable for merging auxiliary services without resizing

### m6i.xlarge --- Not Selected

-   Meets technical requirements but designed for sustained high CPU
    workloads\
-   Higher cost without proportional performance benefit for this
    application profile\
-   More appropriate for constant compute-heavy processing rather than
    web/API services

------------------------------------------------------------------------

## 3. Production Frontend --- prod-frontend-app

**RFP Requirement:** 4 vCPU, 4 GB RAM

  Instance Type   vCPU   RAM     1yr Reserved (\$/mo)   Evaluation
  --------------- ------ ------- ---------------------- -------------
  t3a.xlarge      4      16 GB   65                     Selected
  m6i.xlarge      4      16 GB   72                     Alternative

### t3a.xlarge --- Selected

-   Meets CPU requirement and provides significant memory headroom\
-   Supports peak traffic bursts without performance degradation\
-   Lower cost compared to Intel family options\
-   Extra memory improves frontend caching and reverse proxy performance

### m6i.xlarge --- Not Selected

-   Provides similar compute profile but at a higher cost\
-   Steady-performance design unnecessary for burst-driven frontend
    workloads

------------------------------------------------------------------------

## 4. UAT Backend --- uat-backend-app

**RFP Requirement:** 2 vCPU, 4 GB RAM

  Instance Type   vCPU   RAM    1yr Reserved (\$/mo)   Evaluation
  --------------- ------ ------ ---------------------- -------------
  t3a.medium      2      4 GB   16                     Selected
  m6i.large       2      8 GB   Higher                 Alternative

### t3a.medium --- Selected

-   Exact match with RFP requirements\
-   Burstable instance reduces cost for intermittent testing workloads\
-   Appropriate for non-production usage patterns

### m6i.large --- Not Selected

-   Provides excess RAM not required for UAT testing\
-   Higher cost with no operational benefit in this environment

------------------------------------------------------------------------

## 5. Development Backend --- dev-backend-app

Same RFP requirements and evaluation logic as UAT backend.

### t3a.medium --- Selected

-   Cost-efficient and requirement-compliant\
-   Matches intermittent development usage

### m6i.large --- Not Selected

-   Over-provisioned for development workload\
-   Higher cost without performance necessity

------------------------------------------------------------------------

## 6. UAT Frontend --- uat-frontend-app

**RFP Requirement:** 2 vCPU, 4 GB RAM

  Instance Type   vCPU   RAM    1yr Reserved (\$/mo)   Evaluation
  --------------- ------ ------ ---------------------- ------------
  t3a.medium      2      4 GB   16                     Selected

### t3a.medium --- Selected

-   Already compliant with RFP\
-   No scaling required\
-   Burstable design aligns with test environment traffic patterns

------------------------------------------------------------------------

## 7. Development Frontend --- dev-frontend-app

### t3a.medium --- Selected

-   Matches RFP requirements\
-   Keeps development environment cost minimal while sufficient for
    testing

------------------------------------------------------------------------

## 8. Database Server

**RFP Requirement:** 4 vCPU, 8 GB RAM

  Instance Type   vCPU   RAM     1yr Reserved (\$/mo)   Evaluation
  --------------- ------ ------- ---------------------- -------------
  db.t3.xlarge    4      16 GB   180                    Selected
  db.m6i.xlarge   4      16 GB   Higher                 Alternative

### db.t3.xlarge --- Selected

-   Meets CPU requirement and doubles RAM requirement for DB caching\
-   Cost-efficient compared to general-purpose DB families\
-   Suitable for moderate transactional workloads typical of CMS
    systems\
-   Aligns with single-AZ deployment scope

### db.m6i.xlarge --- Not Selected

-   Better suited for sustained high-throughput databases\
-   Higher cost without proportional performance gains for this workload

------------------------------------------------------------------------

## 9. Bastion Host --- db-bastion

  Instance Type   Evaluation
  --------------- ------------
  t3.nano         Selected

### t3.nano --- Selected

-   Administrative access workload requires minimal CPU and RAM\
-   No RFP performance requirement specified\
-   Keeps infrastructure management cost low

------------------------------------------------------------------------

## 10. NAT Instance --- nat-instance

  Instance Type   Evaluation
  --------------- ------------
  t3.nano         Selected

### t3.nano --- Selected

-   Handles only outbound routing\
-   Low traffic volume does not justify larger instance\
-   Minimizes operational overhead

------------------------------------------------------------------------

## 11. Overall Strategy Summary

  Environment     Sizing Strategy
  --------------- ------------------------------------------
  Production      Burstable instances with memory headroom
  UAT/DEV         Exact-match requirement sizing
  Database        Balanced cost and performance
  Infra Support   Minimal footprint for auxiliary services

------------------------------------------------------------------------

## 12. Final Outcome

The selected instances:

-   Satisfy or exceed all RFP compute requirements\
-   Reduce long-term infrastructure cost using burstable families where
    suitable\
-   Avoid over-provisioning in non-production environments\
-   Provide scalability headroom for production stability

This ensures a technically compliant and financially optimized
infrastructure design.
