<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Static Website Deployment & DNS Fix</h3>

---

## 🎯 Objective Recap
- Deploy a domain-backed static website using **AWS CloudFormation** (`static-website-with-domain.yaml`) and verify access globally.
- Troubleshoot and resolve a DNS resolution issue affecting access while connected to corporate VPN so the site works both on and off VPN.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CloudFormation, S3, CloudFront, Route 53, ACM

---

## 📚 Notes & Key Learnings
- **Template file:** `static-website-with-domain.yaml` parameterizes `BucketName`, `IndexDocument`, `ErrorDocument`, `CertificateArn`, and `DomainName` for a CloudFront distribution backed by S3.
- **ACM:** SSL certificates used by CloudFront must be issued in **us-east-1**; DNS validation must propagate before ACM transitions to `ISSUED`.
- **DNS & VPN:** Corporate VPN DNS can return internal or stale records. If the site fails while on VPN, check the client DNS resolver and flush the local DNS cache.
- **Security note:** `creadintials.txt` is stored locally — avoid committing secrets to the repository.

---

## 🧾 CloudFormation Template — Full Content
- File: `static-website-with-domain.yaml` (full content reproduced below for reference)

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Dynamic Static Website using S3 + CloudFront with custom domain and ACM certificate.

Parameters:

  BucketName:
    Type: String
    Description: "Name of the S3 bucket for the website"

  IndexDocument:
    Type: String
    Default: index.html
    Description: "Default index document"

  ErrorDocument:
    Type: String
    Default: error.html
    Description: "Error document"

  CertificateArn:
    Type: String
    Description: "ACM certificate ARN (must be issued in us-east-1)"

  DomainName:
    Type: String
    Description: "Custom domain name for CloudFront"

Resources:

  WebsiteBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName
      WebsiteConfiguration:
        IndexDocument: !Ref IndexDocument
        ErrorDocument: !Ref ErrorDocument
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy: false
        IgnorePublicAcls: false
        RestrictPublicBuckets: false

  WebsiteBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref WebsiteBucket
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal: "*"
            Action: s3:GetObject
            Resource: !Sub "${WebsiteBucket.Arn}/*"

  CloudFrontDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        DefaultRootObject: !Ref IndexDocument
        Origins:
          - Id: S3WebsiteOrigin
            DomainName: !GetAtt WebsiteBucket.RegionalDomainName
            S3OriginConfig: {}
        DefaultCacheBehavior:
          TargetOriginId: S3WebsiteOrigin
          ViewerProtocolPolicy: redirect-to-https
          AllowedMethods:
            - GET
            - HEAD
          CachedMethods:
            - GET
            - HEAD
          ForwardedValues:
            QueryString: false
        ViewerCertificate:
          AcmCertificateArn: !Ref CertificateArn
          SslSupportMethod: sni-only
        Aliases:
          - !Ref DomainName

Outputs:

  S3WebsiteURL:
    Description: "S3 static website URL"
    Value: !GetAtt WebsiteBucket.WebsiteURL

  CloudFrontURL:
    Description: "CloudFront HTTPS URL"
    Value: !Sub "https://${CloudFrontDistribution.DomainName}"
```

---

## 🖥️ Static Website Files — Full Content

### `static-website/index.html` (full)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Static Website Deployment Complete</title>
<style>
    /* Reset & Font */
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    body { background-color:#0a0f1b; color:#f0f0f0; }

    /* Banner */
    .banner {
        background: linear-gradient(90deg,#0077b6,#00bcd4);
        padding:50px 20px;
        text-align:center;
        color:white;
    }
    .banner h1 { font-size:2.8rem; margin-bottom:10px; }
    .banner p { font-size:1.2rem; opacity:0.9; }

    /* Section */
    section { max-width:1200px; margin:40px auto; padding:0 20px; }
    h2 { text-align:center; color:#00bcd4; margin-bottom:30px; }

    /* Cards */
    .card-container { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:20px; }
    .card {
        background:#111827;
        border-radius:12px;
        box-shadow:0 6px 15px rgba(0,0,0,0.4);
        padding:25px;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover { transform:translateY(-5px); box-shadow:0 10px 25px rgba(0,0,0,0.5); }
    .card h3 { color:#00bcd4; margin-bottom:10px; }
    .card p { font-size:0.95rem; line-height:1.5; color:#ccc; }

    /* Footer */
    footer { text-align:center; padding:20px; font-size:0.9rem; color:#888; }

    /* Responsive */
    @media(max-width:600px) {
        .banner h1 { font-size:2rem; }
        .banner p { font-size:1rem; }
    }
</style>
</head>
<body>

<!-- Banner -->
<div class="banner">
    <h1>Static Website Hosted Successfully!</h1>
    <p>Using AWS S3, CloudFront, and CloudFormation</p>
</div>

<!-- Steps Completed -->
<section>
    <h2>Steps Completed</h2>
    <div class="card-container">
        <div class="card">
            <h3>1. HTML Files Created</h3>
            <p>Prepared <strong>index.html</strong> and <strong>error.html</strong> as the static website content.</p>
        </div>
        <div class="card">
            <h3>2. CloudFormation Template</h3>
            <p>Created a dynamic CloudFormation YAML template to provision the S3 bucket and CloudFront distribution automatically.</p>
        </div>
        <div class="card">
            <h3>3. Deploy Stack</h3>
            <p>Used CloudFormation console to deploy the stack and create the required infrastructure resources.</p>
        </div>
        <div class="card">
            <h3>4. Upload Files to S3</h3>
            <p>Uploaded the HTML files to the root of the S3 bucket created by CloudFormation.</p>
        </div>
        <div class="card">
            <h3>5. ACM Validation</h3>
            <p>Requested SSL certificate from ACM and DNS validation was completed by the domain owner. HTTPS will be active once issued.</p>
        </div>
        <div class="card">
            <h3>6. CloudFront Distribution</h3>
            <p>Created CloudFront distribution pointing to S3 with SSL certificate attached for secure global access.</p>
        </div>
    </div>
</section>

<!-- Technologies Used -->
<section>
    <h2>Technologies & Tools</h2>
    <div class="card-container">
        <div class="card">
            <h3>Amazon S3</h3>
            <p>Simple Storage Service stores static files and serves them publicly via HTTP.</p>
        </div>
        <div class="card">
            <h3>Amazon CloudFront</h3>
            <p>Content Delivery Network (CDN) that delivers content securely over HTTPS with caching and global performance.</p>
        </div>
        <div class="card">
            <h3>AWS CloudFormation</h3>
            <p>Infrastructure as Code (IaC) service to automate creation of S3 buckets, CloudFront distributions, and other resources.</p>
        </div>
        <div class="card">
            <h3>AWS Certificate Manager (ACM)</h3>
            <p>Manages SSL/TLS certificates for secure HTTPS connections without manually configuring certificates.</p>
        </div>
    </div>
</section>

<footer>
    &copy; 2026 Static Website Deployment Example | Built with AWS
</footer>

</body>
</html>
```

---

### `static-website/error.html` (full)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page Not Found</title>
<style>
    body {
        background-color:#0a0f1b;
        color:#f0f0f0;
        font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align:center;
        padding:50px;
    }
    h1 { font-size:3rem; color:#00bcd4; margin-bottom:20px; }
    p { font-size:1.2rem; }
    a { color:#0077b6; text-decoration:none; }
    a:hover { text-decoration:underline; }
</style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Oops! The page you are looking for does not exist.</p>
    <p><a href="index.html">Go back to Home</a></p>
</body>
</html>
```

---

## 🖼️ Screenshots (attached in `images/`)

Below are all screenshots taken during the deployment and validation steps. Click an image to view the full-size file.

- **Certificate — Bash scripting for DevOps**  
  ![certificate bash scripting](./images/certificate%20of%20compleation%20bash%20scripting%20for%20DevOps%20.png)

- **Certificate — IO redirection for DevOps**  
  ![certificate IO redirection](./images/certificate%20of%20compleation%20io%20redirection%20for%20DevOps.png)

- **ACM validation pending (earlier)**  
  ![ACM validation pending](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20and%20waiting%20for%20the%20DNS%20validation%20for%20the%20certificate%20issuing%20.png)

- **ACM certificate issued**  
  ![ACM issued](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20certificatehas%20been%20issued.png)

- **CloudFront URL screenshot**  
  ![CloudFront URL](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20cloudfront%20url%20screen.png)

- **Custom domain URL screenshot**  
  ![Custom domain](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20custom%20domain%20url%20screen.png)

- **Stack parameters (prompt)**  
  ![Stack parameters prompt](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20custom%20parameters%20are%20being%20asked%20to%20add%20when%20creating%20stack.png)

- **Stack parameter values**  
  ![Stack parameter values](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20parameters%20of%20the%20stack%20.png)

- **Resource creation confirmation**  
  ![Resource creation confirmation](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20resourced%20creation%20conformation%20in%20the%20stack%20.png)

- **Stack creation (using CloudFormation)**  
  ![Stack creating](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20stack%20is%20being%20created%20using%20cloud%20formation.png)

- **Stack creation complete**  
  ![Stack complete](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20stack%20is%20create%20compleate.png)

- **Stack creation in progress**  
  ![Stack in progress](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20stack%20is%20create%20in%20progress.png)

- **S3 upload confirmation (static website files)**  
  ![S3 upload confirmation](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20static%20website%20files%20uploaded%20in%20the%20s3%20bucket%20that%20was%20created%20using%20teh%20cloud%20formation%20stack%20.png)

- **Stack outputs: S3 & CloudFront URLs (console output)**  
  ![Stack outputs S3 CloudFront](./images/Static%20website%20hostiong%20using%20a%20custom%20domain%20the%20urls%20s3%20and%20cloudfront%20in%20the%20coutput%20of%20the%20stack.png)

---

## Deployment steps (detailed)
1. Prepare `static-website-with-domain.yaml` and validate parameters (BucketName, DomainName, CertificateArn).
2. Deploy the CloudFormation stack (console or `aws cloudformation deploy --template-file static-website-with-domain.yaml --stack-name <stack-name> --parameter-overrides BucketName=<bucket> DomainName=<domain> CertificateArn=<arn>`).
3. Upload `index.html` and `error.html` to the S3 bucket created by the stack (console or `aws s3 cp static-website/* s3://<bucket>/ --acl public-read`).
4. Request ACM certificate in **us-east-1**, copy the DNS CNAME entries into `DNS_Configuration.csv`, and share/add them to DNS.
5. Wait for ACM to reach `ISSUED`, then confirm CloudFront distribution has the certificate attached and is deployed (can take several minutes).
6. Validate by opening the CloudFront URL and the custom domain in a browser.

---

## ✅ Verification / How to test (expanded)
- Browser check: Open `https://<custom-domain>` and `https://<cloudfront-domain>`; confirm page loads, validate TLS certificate.
- DNS check (Windows): `nslookup <custom-domain>` to confirm it resolves to the CloudFront or expected record.
- TLS check: `curl -I https://<custom-domain>` (or use an online SSL checker) and verify `200 OK` and certificate chain.
- Local DNS troubleshooting (Windows): `ipconfig /flushdns`, then `nslookup <custom-domain>` to ensure correct resolver returns the right records.

---

## 📝 Notes & Recommendations
- Keep `creadintials.txt` out of version control and rotate any sensitive items it contains.
- For production, enable cache policies and consider invalidating CloudFront cache after content updates (`aws cloudfront create-invalidation --distribution-id <id> --paths "/*"`).
- Monitor CloudFront distribution and ACM status in Console for propagation delays.

---

## 🐞 Troubleshooting — DNS / VPN issue (root cause & fix)
- **Symptom:** Site accessible from external networks but failed to resolve on my machine when connected to corporate VPN.
- **Root cause:** VPN client was using a cached internal DNS resolver that returned stale/internal records for the domain.
- **Fix implemented:** IT changed the system DNS to a public resolver (1.1.1.1) and performed a DNS cache flush. I ran the local DNS flush command and verified resolution.

Windows flush command (client side):
```
ipconfig /flushdns
```

**Recommendation:** If access fails while on VPN, switch to a public DNS resolver (e.g., 1.1.1.1 or 8.8.8.8), run `ipconfig /flushdns`, and re-test. If problems persist, ask IT to clear or update the VPN DNS cache.

---

## ✅ Verification / How to test
1. Open the site domain in a browser and confirm `index.html` loads and the HTTPS certificate is valid.
2. Test access while connected to corporate VPN and while disconnected.
3. Confirm ACM certificate status in **us-east-1** is `ISSUED`.
4. Refer to `images/` for screenshots that demonstrate site pages and DNS validation.

---

## Artifacts
- `static-website/` — website source files (`index.html`, `error.html`) and static assets.
- `images/` — screenshots showing the site, CloudFront, and DNS/ACM validation proofs.
- `static-website-with-domain.yaml` — CloudFormation template used to deploy the site and CloudFront distribution.
- `DNS_Configuration.csv` — DNS records used for ACM validation.
- `creadintials.txt` — local credentials notes (handle securely — consider removing sensitive data).

---

Made by Sufi Hassan Asim — 2026-01-05
