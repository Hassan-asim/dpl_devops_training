```markdown
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

### Immediate Actions
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

### Post-Deployment Validation
1. Monitor connection usage via `pg_stat_activity` after applying changes.
2. Ensure idle connections are properly managed and recycled by the pool.
3. Load test with simulated simultaneous logins to verify the fix.
4. Set up CloudWatch alarms for connection pool utilization.

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
- **STATUS:** 429 error root cause identified; recommendations ready for implementation.
- **NEXT:** 
  - Implement connection pooling in application code.
  - Coordinate credentials with Ali Bhai and deploy updated connection string.
  - Monitor production database connections post-deployment.
  - Begin deep-dive into Sindh Ombudsman project codebase.

---

Made by Sufi Hassan Asim — 2026-01-27

```