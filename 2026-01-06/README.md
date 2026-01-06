<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • CDK Course Completion & EC2 Website Hosting</h3>

---

## 🎯 Objective Recap
- Finish the **AWS CDK** course lab and deploy the sample CDK project.
- Host a static website on **EC2** with **Nginx** and secure it with **Let’s Encrypt / Certbot**.
- Document the steps, attach screenshots, and provide DNS instructions to finalize SSL.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Services / Tools:** EC2, Elastic IP, ACM (for reference), Certbot (Let’s Encrypt), SSH

---

## 📚 Notes & Key Learnings
- **CDK:** Completed the CDK course and a hands-on lab that deployed a Lambda-backed sample app — the project folder is `hello-cdk/`.
- **EC2 hosting & SSL:** Launched an EC2 (Amazon Linux 2), installed Nginx, deployed static site files (`index.html`, `error.html`), and installed Certbot to obtain TLS. Certificate issuance is pending DNS A record propagation to the Elastic IP.
- **Security:** `ec2-key.pem` is present locally but **ignored by Git** to prevent accidental commits; consider secure storage or rotation for long-term safety.

---

## ✅ Work Summary (detailed)
1. **CDK lab** — completed the course exercises and successfully deployed the CDK sample app (see `hello-cdk/`).
2. **EC2 & Networking** — launched EC2, associated an Elastic IP, and confirmed the instance is running.
3. **Server setup** — installed Nginx, uploaded website files, verified service and content via SSH and `curl`.
4. **SSL** — installed Certbot and prepared to issue a Let’s Encrypt certificate; certificate issuance awaits domain A record pointing at the Elastic IP (instructions in `request-to-add-record.md`).

---

## 📁 Files & Evidence
- Website files: `index.html`, `error.html`
- Nginx config (server block): `nginx server config file content.txt`
- DNS instructions: `request-to-add-record.md` (A record → Elastic IP 3.215.189.47)
- CDK project: `hello-cdk/`
- Screenshots: `images/` (embedded below)
- Local SSH key: `ec2-key.pem` (kept local; not in Git)

---

## 🖼️ Screenshots (embedded)
Below are the screenshots taken during the session. Filenames describe each step — they are embedded so reviewers can inspect the proof directly.

### CDK Course & Lab

**Certificate of completion (CDK):**

![CDK certificate](./images/certificate%20of%20compleation%20for%20the%20CDK%20course%20.png)

**CDK deployment (Lambda function):**

![CDK deployment proof](./images/deployment%20successfull%20for%20my%20cdk%20project%20of%20hallo%20workd%20using%20teh%20lambds%20function.png)

**Practicing CDK CLI (deploy/destroy):**

![CDK practice](./images/practicing%20teh%20CDK%20lab%20to%20define%20and%20deploy%20a%20lambda%20function%20using%20teh%20cdk%20cli%20afterr%20creating%20a%20typescript%20app%20using%20the%20cdk%20aswell.png)


### EC2 / Nginx / Let’s Encrypt

**Instance running:**

![Instance running](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20Instence%20is%20in%20running%20state.png)

**SSH & key pair located on local:**

![SSH access](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20opning%20the%20terminal%20and%20locating%20the%20keypair%20.png)

**Key permission set before SSH:**

![Key permissions](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20setting%20correct%20permission%20to%20the%20key%20pair%20file%20.png)

**Installed & verified Nginx:**

![Nginx install](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20installing%20teh%20ngenx%20and%20activating%20it%20.png)

**Uploaded site and verified locally:**

![Site uploaded](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20hosted%20teh%20static%20webpage%20on%20the%20ec2%20locallyusing%20teh%20ec2%20linux%20and%20uplaoding%20teh%20files%20there%20and%20using%20teh%20nginx%20.png)

**Elastic IP associated:**

![Elastic IP associated](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20associated%20an%20elastic%20ip%20so%20teh%20ip%20remains%20static%20.png)

**Curl test from instance:**

![Curl test](./images/hosting%20a%20static%20website%20and%20using%20lets%20encript%20task%20curl%20teh%20ip%20from%20teh%20ssh%20ec2%20instence%20terminal%20to%20see%20if%20the%20website%20is%20active%20.png)

**Cloud console verification of resources:**

![Stack verification](./images/stack%20created%20in%20the%20aws%20management%20consol%20varification.png)

---

## 🚀 Commands & Repro Steps

**SSH & Nginx setup**

```bash
ssh -i ec2-key.pem ec2-user@<elastic-ip>
sudo yum update -y
sudo yum install -y nginx
sudo systemctl enable --now nginx
sudo chown -R ec2-user:ec2-user /usr/share/nginx/html
scp -i ec2-key.pem index.html error.html ec2-user@<elastic-ip>:/usr/share/nginx/html/
```

**Certbot (Let’s Encrypt)**

```bash
sudo yum install -y certbot python3-certbot-nginx
sudo certbot --nginx -d <your-domain>
# if DNS not ready:
sudo certbot certonly --standalone -d <your-domain>
```

---

## ✅ Status & Next Steps
- STATUS: Website served successfully from the EC2 instance; certificate issuance is pending DNS A record addition and propagation.
- NEXT: Add the A record for your domain to point to the Elastic IP (see `request-to-add-record.md`) and re-run Certbot to complete HTTPS configuration.

---

## Notes & Security
- `ec2-key.pem` is ignored in Git — keep it secure and consider storing/revoking if necessary.
- If you'd like, I can add the `images/` and `hello-cdk/` folders to the repo so images render on GitHub (they are currently uncommitted).

---

Made by Sufi Hassan Asim — 2026-01-06
