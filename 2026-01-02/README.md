<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Static Website with Custom Domain (S3 + CloudFront + ACM)</h3>

---

## 🎯 Objective Recap
- Implemented a static website with a custom domain using **AWS CloudFormation** (`static-website-with-domain.yaml`).
- Requested an ACM certificate for the domain and prepared DNS validation records; deployed site content (`index.html`, `error.html`), and captured validation screenshots and certificates in `2026-01-02/images/`.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CloudFormation, S3, CloudFront, Route 53, ACM

---

## 📚 Notes & Key Learnings
- **Template file:** `static-website-with-domain.yaml` parameterizes `BucketName`, `IndexDocument`, `ErrorDocument`, `CertificateArn`, and `DomainName` for a domain-backed CloudFront distribution.
- **ACM:** Requested a certificate (must be in us-east-1 for CloudFront). DNS validation is in progress — status is `PENDING_VALIDATION` in ACM until DNS records are propagated and checked.
- **DNS:** `DNS_Configuration.csv` contains the CNAME records required for ACM validation; these were shared with the domain owner for propagation.
- **Notes on credentials:** `creadintials.txt` exists in the folder for local use — **do not commit secrets** or include credentials in public docs; content is not reproduced here.

---

## 🧾 CloudFormation Template (excerpt)
- File: `static-website-with-domain.yaml`

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

  CloudFrontDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        DefaultRootObject: !Ref IndexDocument
        Origins:
          - Id: S3WebsiteOrigin
            DomainName: !GetAtt WebsiteBucket.WebsiteURL
            CustomOriginConfig:
              HTTPPort: 80
              HTTPSPort: 443
              OriginProtocolPolicy: http-only
        ViewerCertificate:
          AcmCertificateArn: !Ref CertificateArn
          SslSupportMethod: sni-only
        Aliases:
          - !Ref DomainName
```

---

## 🖥️ Static Website Files (full content)

### `index.html`

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
            <p>Requested SSL certificate from ACM and DNS validation is pending; waiting for the domain owner to add DNS records.</p>
        </div>
        <div class="card">
            <h3>6. CloudFront Distribution</h3>
            <p>Created CloudFront distribution pointing to S3 with SSL certificate attached for secure global access (once ACM is issued).</p>
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

### `error.html`

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

## 🖼️ Evidence & Screenshots
- ![ACM pending validation](./images/pending%20validation%20of%20the%20ssl%20certificate%20on%20the%20ACM%20consol%20page%20in%20aws%20.png) — ACM certificate pending validation
- ![ACM request ID](./images/ssl%20certificate%20id%20page%20of%20aws%20consol%20showing%20the%20requested%20certificate%20for%20the%20domain%20of%20static%20website.png) — Requested certificate ID in ACM
- ![Static site (HTTPS pending)](./images/static%20website%20hosted%20successfuly%20using%20s3%20and%20cloudfront.png) — Site served via CloudFront (HTTPS when ACM issued)

### Course Certificates
- ![ACM / CloudFront fundamentals certificate](./images/certificate%20for%20ACM%20getting%20started%20.png) — ACM/CloudFront fundamentals
- ![Route 53 getting started certificate](./images/certificate%20for%20route%2053%20getting%20started.png) — Route 53
- ![Linux & SQL certificate](./images/linux%20and%20sql%20course%20compleation%20certificate.png) — Linux & SQL completion

### DNS / Validation
- `DNS_Configuration.csv` — contains DNS records (CNAME) to add to the domain registrar for ACM validation.

---

## ✅ Daily Summary
- Requested and tracked an ACM certificate for the custom domain; validation is pending DNS changes (see pending validation screenshots).
- Added `static-website-with-domain.yaml`, deployed resources, and uploaded site files (`index.html`, `error.html`); static site is ready and will serve over HTTPS once ACM is issued.
- Next steps: confirm DNS entries in the registrar, wait for ACM to change to `ISSUED`, then complete CloudFront distribution steps and test HTTPS with the custom domain.

Made by Sufi Hassan Asim — 2026-01-02
