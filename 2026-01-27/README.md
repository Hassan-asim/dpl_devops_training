<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • 429 Error Investigation & Sindh Ombudsman Onboarding</h3>

---

## 🎯 Objective
Investigate and identify the root cause of 429 "too many requests" errors occurring in production when multiple users log in simultaneously, and complete onboarding for the Sindh Ombudsman project.

---

## 💡 Summary / What I Investigated
- **Production Issue:** Discovered that simultaneous user logins trigger 429 errors indicating connection pool exhaustion.
- **Root Cause:** Application lacks connection pooling implementation; each request creates a fresh database connection instead of reusing pooled connections.
- **Database Status:** Confirmed PostgreSQL RDS instance is healthy with available connections (max_connections = 838), but the idle connection pile-up from the application exhausts this limit.
- **New Project Onboarding:** Met with UmSir to get introduced to the Sindh Ombudsman project and understand requirements.

---

## 🛠️ Work Environment
- **Host OS:** Windows
- **Tools:** AWS SSM port forwarding, psql, Visual Studio Code
- **Database:** PostgreSQL on AWS RDS
- **Application Stack:** .NET Web API with NpgsqlConnection (no pooling)

---

## 📚 Investigation Steps & Key Findings

### 1. Reviewed Application Code
- Inspected repository classes responsible for database access.
- Observed that each request opens a fresh `NpgsqlConnection` instance instead of reusing connections.
- Verified that the base repository fetches the connection string from configuration but does not implement connection pooling.
- Confirmed that some repositories instantiate `NpgsqlConnection` directly without pooling parameters.

### 2. Checked Connection Handling
- Base repository does not use connection pooling mechanisms.
- Connection string in code lacks pooling configuration.
- Each HTTP request spawns a new connection lifecycle.

### 3. Examined Production Configuration
- Checked `appsettings.Production.json` in the WebApi folder.
- **Critical Finding:** The `DefaultConnection` string is **empty** and does not define pooling or maximum connection limits.
- No connection pool size limits are specified in the production configuration.

### 4. Connected to Production Database
- Used **AWS Systems Manager (SSM)** port forwarding to establish a secure tunnel to the RDS instance.
- Verified database connectivity using `psql` command-line client.
- Queried PostgreSQL server parameters and connection state.

### 5. Analyzed Connection State
Checked PostgreSQL server parameters:
- `max_connections = 838`
- Queried `pg_stat_activity` to inspect active and idle connections.
- **Key Observation:** Found multiple connections in idle state, predominantly from the same application user (`prod_app_user`).
- Confirmed that connection count grows with each simultaneous login, eventually hitting the server limit of 838.

### 6. Rate-Limiting Policy Research (Briefing from Khurrun Bhai)
Khurrun Bhai mentioned that there is a rate-limiting policy applied in the codebase to restrict API calls in the **Dev and UAT environments**. Key findings:
- **Current Issue:** The policy is currently too restrictive, preventing legitimate requests from being processed (Oski mentioned the issue is occurring).
- **Action Required:** Increase the rate-limiting policy threshold to allow more API calls per time window.
- **Primary Endpoints to Review:** The complaint submission endpoints are explicitly rate-limited in `Program.cs`, as these are high-traffic endpoints that need careful throttling.
- **Strategy:** Need to adjust rate-limiting parameters (requests per minute/second, time window) to balance security with functionality.

### 7. Codebase Understanding & Rate-Limiting Implementation
- Reviewed `Program.cs` to understand middleware and policy configuration.
- Identified that rate-limiting is implemented using middleware (likely using a library like AspNetCoreRateLimit or similar).
- Complaint submission endpoints are specifically configured with rate-limiting decorators/policies.
- Policy enforcement appears to be applied at multiple levels: global middleware and endpoint-specific configurations.
- Gained foundational understanding of how the codebase structures API protection and throttling mechanisms.

---

## 🔍 Root Cause Analysis

**Why 429 Errors Occur:**
1. Multiple users log in simultaneously → each login generates a new HTTP request.
2. Each request creates a new database connection (no pooling).
3. Connections remain in an idle state after the query completes (not returned to a pool).
4. Idle connections accumulate on the server.
5. The server reaches `max_connections = 838` and rejects new connection attempts.
6. Application returns **429 "too many requests"** error to the user.

**Why It's Happening Now:**
- Production deployment lacks connection pooling configuration.
- The application design does not reuse connections, treating each connection as disposable.
- Even though RDS allows 838 connections, poor connection management exhausts this limit prematurely.

---

## ✅ Recommendations

### For 429 Connection Pooling Issue

#### Immediate Actions
1. **Enable Connection Pooling in Repositories:**
   - Modify repository classes to use connection pooling (e.g., NpgsqlConnectionStringBuilder with Pooling=true).
   - Ensure connections are properly disposed or returned to the pool after use.

2. **Update Production Connection String:**
   - Add pooling parameters to the `DefaultConnection` in `appsettings.Production.json`:
   ```
   Server=<rds-endpoint>;Database=<db-name>;User Id=<user>;Password=<password>;Pooling=true;Max Pool Size=50;Min Pool Size=5;
   ```

3. **Coordinate with Ali Bhai:**
   - Request secure delivery of actual PROD credentials.
   - Update the connection string securely (use AWS Secrets Manager or similar).

#### Post-Deployment Validation
1. Monitor connection usage via `pg_stat_activity` after applying changes.
2. Ensure idle connections are properly managed and recycled by the pool.
3. Load test with simulated simultaneous logins to verify the fix.
4. Set up CloudWatch alarms for connection pool utilization.

### For Rate-Limiting Policy Issue

#### Actions Required
1. **Increase Rate-Limiting Policy Threshold:**
   - Review current rate-limiting configuration in `Program.cs` middleware setup.
   - Adjust requests-per-minute/second limits for complaint submission endpoints.
   - Balance between security (preventing abuse) and functionality (allowing legitimate users).

2. **Endpoints to Reconfigure:**
   - Focus on complaint submission endpoints that are explicitly rate-limited.
   - Consider environment-specific configurations (Dev/UAT vs Prod).
   - Ensure rate-limiting is more lenient in Dev/UAT but remains strict in production.

3. **Testing:**
   - Load test with concurrent requests to verify the new policy allows legitimate traffic.
   - Monitor rate-limiting logs to ensure false positives are eliminated.

---

## 📁 Files & References
- **Application Code:** WebApi folder (repository classes)
- **Configuration:** `appsettings.Production.json` (currently has empty DefaultConnection)
- **Database:** AWS RDS PostgreSQL instance
- **Investigation Tool:** AWS SSM Session Manager, psql

---

## 🚀 New Project: The Breath Source

### Onboarding Summary
- **Met with:** UmSir (Project Lead/Manager)
- **Project Name:** The Breath Source
- **Status:** Onboarding phase
- **Next Steps:** Understand project requirements, codebase, and assigned responsibilities.

---

## ✅ Status & Next Steps
- **STATUS:** 
  - 429 error root cause identified; recommendations ready for implementation.
  - Rate-limiting policy issue identified; codebase understanding initiated.
- **NEXT:** 
  - Implement connection pooling in application code.
  - Coordinate credentials with Ali Bhai and deploy updated connection string.
  - Monitor production database connections post-deployment.
  - Work with Khurrun Bhai to adjust rate-limiting policy thresholds in Dev/UAT.
  - Review and reconfigure complaint submission endpoint rate-limiting.
  - Continue deep-dive into The Breath Source project codebase.

---

Made by Sufi Hassan Asim — 2026-01-27
