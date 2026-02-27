<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily Report • Production Deployments & Database Operations — 2026-02-27</h3>

---

## 🎯 Objective
Execute production database updates, deploy notification system infrastructure, consult on RDS configuration risks, and advance AWS technical training.

---

## 💡 Summary
Updated critical records in the Production RDS database following approved requests from Khurrum and Salman. Deployed notification service updates to the production environment by successfully deploying Lambda and SQS stacks. Consulted with Hazar regarding RDS MultiAZ configuration to mitigate replacement risks during scaling operations. Continued progress on the KodeKloud AWS course.

---

## 🚀 Infrastructure & Database Operations

**1. PROD RDS Data Updates:**
- Executed record updates on the Production database as requested by Khurrum and approved by Salman.

**2. Production Stack Deployment:**
- Deployed updated notification logic to PROD environment.
- Successfully deployed Lambda and SQS stacks to ensure production systems are up to date.

**3. RDS Configuration Strategy:**
- Discussed the impact of transitioning from MultiAZ to Single AZ with Hazar.
- Analyzed the CDK warning regarding potential DB instance replacement (`may cause replacement`) when adjusting `MultiAZ` settings alongside the `DBInstanceClass` upgrade to `db.t4g.xlarge`.

---

## 📚 Training & Professional Development

**1. AWS for Beginners (KodeKloud):**
- Continued the "AWS for Beginners with Hands-on Labs" course provided by Hazar.
- Completed training modules focused on AWS fundamentals and resource management.
- Link: [Module Lesson](https://learn.kodekloud.com/user/courses/aws-for-beginners-with-hands-on-labs/module/d28d64dd-cbb1-45ed-83c4-e8d4b0b0d08b/lesson/191587ad-e9a2-4892-acb5-528a6d38034c)

---

## 📈 Operational Summary & Next Steps

**Completed Tasks:**
- ✅ Updated Production RDS records.
- ✅ Deployed Lambda and SQS notification stacks to PROD.
- ✅ Consulted on RDS MultiAZ risk mitigation.
- ✅ Continued KodeKloud AWS training.

**Next Steps:**
- Monitor PROD Lambda and SQS health post-deployment.
- Finalize the RDS configuration approach based on the MultiAZ discussion.
- Complete the next section of the KodeKloud training.

---

**Author:** Sufi Hassan Asim  
**Date:** 2026-02-27
