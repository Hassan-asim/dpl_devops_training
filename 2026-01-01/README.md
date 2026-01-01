<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Static Website Deployment (S3 + CloudFront via CloudFormation)</h3>

---

## 🎯 Objective Recap
- Implemented a static website deployment using **AWS CloudFormation** to provision an S3 bucket and a CloudFront distribution (no custom domain).
- Prepared and uploaded site content (`index.html`, `error.html`) and collected screenshots and course certificates as evidence in `2026-01-01/images/`.

---

## 🛠️ Study / Work Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell
- **AWS Console:** CloudFormation, S3, CloudFront

---

## 📚 Notes & Key Learnings
- **CloudFormation template:** `static-website-cloudformation.yaml` is parameterized: `BucketName`, `IndexDocument`, `ErrorDocument`.
- **S3 Bucket:** Configured with `WebsiteConfiguration` and a bucket policy granting public read access to objects.
- **CloudFront distribution:** Uses the S3 website endpoint as a custom origin with an HTTP-only origin protocol policy and `redirect-to-https` viewer policy; defaults to the `IndexDocument`.
- **Outputs:** Template exposes `S3WebsiteURL` and `CloudFrontURL` for quick verification.
- **Files deployed:** `index.html` (responsive landing page summarizing the deployment steps) and `error.html` (simple 404 page).

---

## 🧾 Template (excerpt)
- File: `static-website-cloudformation.yaml`

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Dynamic Static Website using S3 + CloudFront without a custom domain.
  All names and files are configurable via parameters.

Parameters:
  BucketName:
    Type: String
    Description: "Name of the S3 bucket to create for the website"

  IndexDocument:
    Type: String
    Default: index.html
    Description: "Default index document for S3 website"

  ErrorDocument:
    Type: String
    Default: error.html
    Description: "Error document for S3 website"

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
            DomainName: !Select
              - 2
              - !Split
                - "/"
                - !GetAtt WebsiteBucket.WebsiteURL
            CustomOriginConfig:
              HTTPPort: 80
              HTTPSPort: 443
              OriginProtocolPolicy: http-only

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
          CloudFrontDefaultCertificate: true

Outputs:
  S3WebsiteURL:
    Description: "S3 static website URL"
    Value: !GetAtt WebsiteBucket.WebsiteURL

  CloudFrontURL:
    Description: "CloudFront HTTPS URL"
    Value: !Sub "https://${CloudFrontDistribution.DomainName}"
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
    <title>Static Website Deployment Completed</title>
    <style>
        /* General Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f4f7fa;
            color: #333;
        }

        /* Banner */
        .banner {
            background: linear-gradient(90deg, #0f4c81, #00b4d8);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }

        .banner h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .banner p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* Section */
        section {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }

        h2 {
            text-align: center;
            color: #0f4c81;
            margin-bottom: 30px;
        }

        /* Cards */
        .card-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            padding: 20px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }

        .card h3 {
            color: #0077b6;
            margin-bottom: 10px;
        }

        .card p {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #555;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
            color: #888;
        }

        /* Responsive */
        @media(max-width: 600px) {
            .banner h1 {
                font-size: 2rem;
            }

            .banner p {
                font-size: 1rem;
            }
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
        <h2>Steps We Completed</h2>
        <div class="card-container">
            <div class="card">
                <h3>1. Create HTML Files</h3>
                <p>Prepared <strong>index.html</strong> and <strong>error.html</strong> as the content of our static website.</p>
            </div>
            <div class="card">
                <h3>2. Write CloudFormation Template</h3>
                <p>Created a dynamic CloudFormation YAML template to provision the S3 bucket and CloudFront distribution automatically.</p>
            </div>
            <div class="card">
                <h3>3. Deploy CloudFormation Stack</h3>
                <p>Used AWS CloudFormation console to deploy the stack and create the required infrastructure resources.</p>
            </div>
            <div class="card">
                <h3>4. Upload Files to S3</h3>
                <p>Uploaded the HTML files to the root of the S3 bucket created by CloudFormation.</p>
            </div>
            <div class="card">
                <h3>5. Test URLs</h3>
                <p>Accessed the website via both S3 endpoint (HTTP) and CloudFront endpoint (HTTPS) to ensure everything works.</p>
            </div>
        </div>
    </section>

    <!-- Technologies Used -->
    <section>
        <h2>Technologies & Tools</h2>
        <div class="card-container">
            <div class="card">
                <h3>Amazon S3</h3>
                <p>Simple Storage Service (S3) stores static files and serves them as a website.</p>
            </div>
            <div class="card">
                <h3>Amazon CloudFront</h3>
                <p>Content Delivery Network (CDN) that delivers content globally over HTTPS with caching.</p>
            </div>
            <div class="card">
                <h3>CloudFormation</h3>
                <p>Infrastructure as Code (IaC) service to automate the creation of AWS resources like S3 buckets and CloudFront distributions.</p>
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
<html>
<head>
    <title>Error</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Error</h1>
    <p>The page you requested does not exist.</p>
</body>
</html>
```

---

## 🖼️ Evidence & Screenshots
- ![CloudFormation stack info page](./images/cloudformation%20stack%20info%20page%20of%20the%20static%20website.png) — CloudFormation stack details and events
- ![S3 bucket created](./images/s3%20bucket%20created%20using%20teh%20cloudformation%20template%20for%20teh%20static%20website%20hosting.png) — S3 bucket created by template
- ![Static website working](./images/static%20website%20hosted%20successfuly%20using%20s3%20and%20cloudfront.png) — Website served via CloudFront (HTTPS)

### Course Certificates
- ![CloudFront fundamentals certificate](./images/certificate%20of%20aws%20course%20cloudfront%20fundamentals.png) — CloudFront fundamentals
- ![EC2 Auto Scaling fundamentals certificate](./images/certificate%20of%20aws%20course%20EC2%20auto%20scalling%20fundamentals.png) — EC2 Auto Scaling fundamentals
- ![Managing Amazon S3 certificate](./images/certificate%20of%20aws%20course%20managing%20amazon%20S3%20.png) — Managing Amazon S3

---

## ✅ Daily Summary
- Successfully created and deployed a CloudFormation template to provision an S3-hosted static website with a CloudFront distribution.
- Uploaded `index.html` and `error.html`, verified S3 and CloudFront endpoints, and collected screenshots and certificates as evidence.
- Next steps: parameterize more template options (logging, cache behaviors), add CI/CD automation for deployments, and test invalid requests to verify error page behavior.

Made by Sufi Hassan Asim — 2026-01-01
