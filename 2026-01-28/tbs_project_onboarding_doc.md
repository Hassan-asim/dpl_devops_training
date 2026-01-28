Project Onboarding & Responsibilities – Sufi Hassan Asim

---

**1. Introduction**

**Purpose:**
This document serves as a personal onboarding guide for Sufi Hassan Asim, detailing responsibilities, key services, operational procedures, and access rights for the assigned project.

**Scope:**
Covers AWS ECS services management, monitoring, GitLab repository access, and associated operational duties.

---

**2. Project Overview**

**High-Level Architecture:**
- AWS ECS Fargate-based microservices
- Separate clusters for Development (DevCluster) and Production (ProdCluster)
- CI/CD pipeline connected to GitLab repositories

**Clusters:**
- Dev Cluster: DevCluster
- Prod Cluster: ProdCluster

**ECS Services:**

*Dev Cluster Services:*
| Service Name | Task Definition | Container Image | Desired Count | Running Count | Responsibility |
|--------------|-----------------|-----------------|---------------|---------------|----------------|
| DevSubscriptionServiceStack-FargateServiceAC2B3B85-YOgZKtWp3907 | DevSubscriptionServiceStackFargateTaskDef90DE7581:151 | 477205183357.dkr.ecr.us-east-2.amazonaws.com/devsubscriptionservicestack-subscriptionservicerepo8a425aad-1bxo3j64sdmk:fccd382 | 1 | 1 | Monitoring, Scaling, Error Handling |
| DevUserServiceStack-FargateServiceAC2B3B85-eueObu0LJBCF | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| DevNotificationServiceStack-FargateServiceAC2B3B85-nnUKandrgwvA | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| DevAuthServiceStack-FargateServiceAC2B3B85-1MHUNTyVI9g3 | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| DevQdrantServiceStack-DevQdrantFargateService8B6C4258-JfYo29uG3j9Z | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| DevLiveClassesServiceStack-FargateServiceAC2B3B85-D3FuiUjTM4GS | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| DevSearchServiceStack-FargateServiceAC2B3B85-rIOpcHBk0Yeg | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| DevWebServiceStack-FargateServiceAC2B3B85-Gsu1zePaiiwi | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |

*Prod Cluster Services:*
| Service Name | Task Definition | Container Image | Desired Count | Running Count | Responsibility |
|--------------|-----------------|-----------------|---------------|---------------|----------------|
| ProdAuthServiceStack-FargateServiceAC2B3B85-xN0VkeRowaP2 | ProdAuthServiceStackFargateTaskDefD9D24E65:24 | 477205183357.dkr.ecr.us-east-2.amazonaws.com/prodauthservicestack-authservicerepo50124346-yitjpoecwkv8:dfcf37f | 1 | 1 | Monitoring, Scaling, Error Handling |
| ProdLiveClassesServiceStack-FargateServiceAC2B3B85-pVM8NINAvnbC | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| ProdNotificationServiceStack-FargateServiceAC2B3B85-ronGdupKwvQc | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| ProdSearchServiceStack-FargateServiceAC2B3B85-p5TC8HI3uc1a | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| ProdWebServiceStack-FargateServiceAC2B3B85-K8ds8xcEOL2W | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| ProdSubscriptionServiceStack-FargateServiceAC2B3B85-dqHC18e7XhL2 | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| ProdUserServiceStack-FargateServiceAC2B3B85-shMK3Ff1e2uQ | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |
| ProdQdrantServiceStack-QdrantFargateService5C2F8C90-z9u4Rp8n5qdB | (Add TaskDef) | (Add Image) | 1 | 1 | Monitoring |

---

**3. GitLab Repository Responsibilities**
- Access granted by Ali Imran
- Responsibilities include:
  - Code review and approvals
  - Monitoring CI/CD pipelines for build or deployment failures
  - Branch management (feature, staging, release)
  - Coordination with Dev and Prod teams for deployments

---

**4. Operational Procedures**

**ECS Monitoring Commands:**
- List clusters: `aws ecs list-clusters --region us-east-2`
- List services: `aws ecs list-services --cluster <ClusterName> --region us-east-2`
- Describe service: `aws ecs describe-services --cluster <ClusterName> --services <ServiceARN> --region us-east-2 --output table`
- Describe task definition: `aws ecs describe-task-definition --task-definition <TaskDefARN> --region us-east-2 --output table`

**Error Handling:**
- Monitor CloudWatch logs for service errors
- Restart failing services if necessary using Fargate CLI or AWS console
- Notify relevant developers for persistent failures

---

**5. Known Risks & Notes**
- Interdependencies between services (e.g., AuthService with UserService)
- Production services require extra caution during deployments
- Always validate task definitions and container images before updating

---

**6. References & Resources**
- AWS ECS Documentation: https://docs.aws.amazon.com/ecs/
- Internal dashboards for Dev/Prod monitoring
- GitLab repository documentation for CI/CD pipelines

---

**Access Details**
- AWS Admin Account: Provided by Umair Khan
- GitLab Repo Group Access: Provided by Ali Imran

---

**Prepared by:** Sufi Hassan Asim

