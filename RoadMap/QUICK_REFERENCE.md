# Quick Reference Guide - Essential Commands & Concepts

## Table of Contents
1. [Linux Essential Commands](#linux-essential-commands)
2. [Git Commands](#git-commands)
3. [AWS CLI Quick Commands](#aws-cli-quick-commands)
4. [Docker & Container Commands](#docker--container-commands)
5. [Nginx Configuration](#nginx-configuration)
6. [TypeScript Basics](#typescript-basics)
7. [AWS CDK Snippets](#aws-cdk-snippets)
8. [Troubleshooting Guide](#troubleshooting-guide)

---

## Linux Essential Commands

### File & Directory Operations
```bash
pwd                           # Print working directory
cd /path                      # Change directory
ls -la                        # List files (detailed)
mkdir folder_name             # Create directory
rmdir folder_name             # Remove empty directory
rm -rf folder_name            # Remove directory with contents
cp source destination         # Copy file
mv source destination         # Move/rename file
find . -name "*.txt"          # Find files by pattern
```

### File Content & Text Processing
```bash
cat filename                  # Display file content
head -n 10 filename           # Show first 10 lines
tail -n 10 filename           # Show last 10 lines
less filename                 # View file page by page
grep "pattern" filename       # Search for pattern
grep -r "pattern" .           # Recursive search
sed 's/old/new/g' filename    # Replace text
awk '{print $1}' filename     # Extract fields
cut -d',' -f1,2 filename      # Extract columns
sort filename                 # Sort lines
uniq filename                 # Show unique lines
wc -l filename                # Count lines
```

### Permissions & Ownership
```bash
chmod 755 filename            # Change permissions (rwxr-xr-x)
chmod +x script.sh            # Make executable
chown user:group filename     # Change owner
chown -R user:group folder    # Change owner recursively
sudo command                  # Execute as root
```

### User & Group Management
```bash
whoami                        # Current user
id                            # User and group IDs
sudo useradd username         # Create user
sudo userdel username         # Delete user
sudo passwd username          # Change password
groups username               # List user groups
```

### Network & SSH
```bash
ifconfig                      # View network config
ip addr show                  # Show IP addresses
ping hostname                 # Test connectivity
ssh user@host                 # SSH login
ssh -i key.pem user@host      # SSH with key
scp file user@host:/path      # Secure copy
ssh-keygen -t rsa -b 4096     # Generate SSH key
ssh-copy-id -i key user@host  # Copy public key to host
```

### System Management
```bash
uname -a                      # System information
df -h                         # Disk space usage
du -sh folder                 # Folder size
top                           # Process monitor
ps aux                        # List processes
kill -9 PID                   # Kill process
systemctl status service      # Service status
systemctl start service       # Start service
systemctl enable service      # Enable at boot
journalctl -xe                # View system logs
```

---

## Git Commands

### Basic Setup
```bash
git config --global user.name "Name"
git config --global user.email "email@example.com"
git init                      # Initialize repository
git clone url                 # Clone repository
```

### Branching
```bash
git branch                    # List branches
git branch feature-name       # Create branch
git checkout feature-name     # Switch branch
git checkout -b feature-name  # Create and switch
git branch -d feature-name    # Delete branch
git branch -m old new         # Rename branch
```

### Staging & Commits
```bash
git status                    # View changes
git add filename              # Stage file
git add .                     # Stage all changes
git commit -m "message"       # Create commit
git commit -am "message"      # Stage and commit
git log --oneline             # View commit history
git diff                      # View unstaged changes
git diff --staged             # View staged changes
```

### Undoing Changes
```bash
git restore filename          # Discard changes
git restore --staged filename # Unstage file
git reset HEAD~1              # Undo last commit (keep changes)
git reset --hard HEAD~1       # Undo last commit (discard changes)
git revert HEAD               # Create revert commit
git reflog                    # View all HEAD positions
```

### Merging & Rebasing
```bash
git merge branch-name         # Merge branch
git merge --no-ff branch      # Merge with merge commit
git rebase main               # Rebase on main
git rebase -i HEAD~3          # Interactive rebase (last 3 commits)
```

### Stashing
```bash
git stash                     # Stash changes
git stash list                # View stashed changes
git stash pop                 # Apply and remove stash
git stash apply               # Apply without removing
git stash drop                # Delete stash
```

### Remote Operations
```bash
git remote -v                 # List remotes
git remote add origin url     # Add remote
git push origin main          # Push to remote
git pull origin main          # Pull from remote
git fetch origin              # Fetch without merge
git branch -u origin/main     # Track remote branch
```

---

## AWS CLI Quick Commands

### EC2 Operations
```bash
# List EC2 instances
aws ec2 describe-instances

# Launch EC2 instance
aws ec2 run-instances \
  --image-id ami-xxxxxxxx \
  --instance-type t3.micro \
  --key-name my-key

# Stop instance
aws ec2 stop-instances --instance-ids i-xxxxxxxx

# Start instance
aws ec2 start-instances --instance-ids i-xxxxxxxx

# Terminate instance
aws ec2 terminate-instances --instance-ids i-xxxxxxxx
```

### S3 Operations
```bash
# List buckets
aws s3 ls

# Create bucket
aws s3 mb s3://bucket-name

# Upload file
aws s3 cp file.txt s3://bucket-name/

# Download file
aws s3 cp s3://bucket-name/file.txt .

# Sync directory
aws s3 sync ./local s3://bucket-name/

# List bucket contents
aws s3 ls s3://bucket-name/ --recursive
```

### IAM Operations
```bash
# List users
aws iam list-users

# Create user
aws iam create-user --user-name username

# Create access key
aws iam create-access-key --user-name username

# Attach policy
aws iam attach-user-policy \
  --user-name username \
  --policy-arn arn:aws:iam::aws:policy/PolicyName

# List roles
aws iam list-roles
```

### CloudFormation
```bash
# List stacks
aws cloudformation list-stacks

# Create stack
aws cloudformation create-stack \
  --stack-name my-stack \
  --template-body file://template.yaml

# Update stack
aws cloudformation update-stack \
  --stack-name my-stack \
  --template-body file://template.yaml

# Delete stack
aws cloudformation delete-stack --stack-name my-stack

# Describe stack
aws cloudformation describe-stacks --stack-name my-stack
```

### RDS Operations
```bash
# List RDS instances
aws rds describe-db-instances

# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t3.micro \
  --engine postgres

# Delete RDS instance
aws rds delete-db-instance \
  --db-instance-identifier mydb \
  --skip-final-snapshot
```

---

## Docker & Container Commands

### Docker Basics
```bash
# Build image
docker build -t image-name:tag .

# List images
docker images

# Run container
docker run -d --name container-name image-name

# Run with port mapping
docker run -d -p 8080:8080 --name container-name image-name

# List running containers
docker ps

# List all containers
docker ps -a

# Stop container
docker stop container-name

# Start container
docker start container-name

# Remove container
docker rm container-name

# View logs
docker logs container-name

# Execute command in container
docker exec -it container-name bash
```

### Docker Registry (ECR)
```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag image-name:tag <account>.dkr.ecr.us-east-1.amazonaws.com/repo-name:tag

# Push to ECR
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/repo-name:tag

# Create ECR repository
aws ecr create-repository --repository-name repo-name
```

---

## Nginx Configuration

### Basic Configuration Structure
```nginx
# /etc/nginx/nginx.conf

user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 768;
}

http {
    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    gzip on;

    include /etc/nginx/sites-enabled/*;
}
```

### Virtual Host Configuration
```nginx
# /etc/nginx/sites-available/example.com

server {
    listen 80;
    server_name example.com www.example.com;

    root /var/www/html;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php-fpm.sock;
    }
}
```

### HTTPS with SSL
```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    root /var/www/html;

    location / {
        try_files $uri $uri/ =404;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
```

### Reverse Proxy
```nginx
upstream backend {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
}

server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Common Commands
```bash
# Test configuration
sudo nginx -t

# Reload configuration
sudo systemctl reload nginx

# Restart Nginx
sudo systemctl restart nginx

# Check status
sudo systemctl status nginx

# View error logs
sudo tail -f /var/log/nginx/error.log

# View access logs
sudo tail -f /var/log/nginx/access.log
```

---

## TypeScript Basics

### Type Annotations
```typescript
// Primitive types
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;

// Arrays
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];

// Any and Unknown
let data: any = "anything goes";
let unknown: unknown = "be careful";

// Union types
let id: string | number;
id = "123";    // OK
id = 123;      // OK
```

### Interfaces
```typescript
interface User {
    name: string;
    age: number;
    email?: string;  // Optional property
    readonly id: number;  // Read-only
}

const user: User = {
    name: "John",
    age: 30,
    id: 1
};
```

### Classes
```typescript
class Animal {
    constructor(public name: string) {}

    speak(): void {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    speak(): void {
        console.log(`${this.name} barks`);
    }
}

const dog = new Dog("Buddy");
dog.speak();  // "Buddy barks"
```

### Generics
```typescript
// Generic function
function identity<T>(arg: T): T {
    return arg;
}

// Generic class
class Container<T> {
    constructor(private value: T) {}

    getValue(): T {
        return this.value;
    }
}

const container = new Container<string>("Hello");
```

### Enums
```typescript
enum Color {
    Red = 0,
    Green = 1,
    Blue = 2
}

let myColor: Color = Color.Green;
```

---

## AWS CDK Snippets

### Basic Stack Setup
```typescript
import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';

export class MyStack extends cdk.Stack {
    constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Define resources here
    }
}

const app = new cdk.App();
new MyStack(app, 'MyStack');
app.synth();
```

### VPC Creation
```typescript
const vpc = new ec2.Vpc(this, 'MyVpc', {
    ipAddresses: ec2.IpAddresses.cidr('10.0.0.0/16'),
    maxAzs: 2,
    natGateways: 1,
    subnetConfiguration: [
        {
            name: 'Public',
            subnetType: ec2.SubnetType.PUBLIC,
            cidrMask: 24,
        },
        {
            name: 'Private',
            subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
            cidrMask: 24,
        },
    ],
});
```

### Security Group
```typescript
const securityGroup = new ec2.SecurityGroup(this, 'WebSG', {
    vpc: vpc,
    allowAllOutbound: true,
    description: 'Allow web traffic',
});

securityGroup.addIngressRule(
    ec2.Peer.anyIpv4(),
    ec2.Port.tcp(80),
    'Allow HTTP'
);

securityGroup.addIngressRule(
    ec2.Peer.anyIpv4(),
    ec2.Port.tcp(443),
    'Allow HTTPS'
);
```

### EC2 Instance
```typescript
const instance = new ec2.Instance(this, 'MyInstance', {
    vpc: vpc,
    instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
    machineImage: ec2.MachineImage.latestAmazonLinux2(),
    keyName: 'my-key',
    securityGroup: securityGroup,
});
```

### RDS Database
```typescript
import * as rds from 'aws-cdk-lib/aws-rds';

const database = new rds.DatabaseInstance(this, 'MyDatabase', {
    engine: rds.DatabaseInstanceEngine.postgres({
        version: rds.PostgresEngineVersion.VER_13,
    }),
    instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
    credentials: rds.Credentials.fromGeneratedSecret('admin'),
    vpc: vpc,
    vpcSubnets: {
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
    },
    multiAz: true,
    storageEncrypted: true,
    removalPolicy: cdk.RemovalPolicy.SNAPSHOT,
});
```

### S3 Bucket
```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = new s3.Bucket(this, 'MyBucket', {
    versioned: true,
    encryption: s3.BucketEncryption.S3_MANAGED,
    blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    removalPolicy: cdk.RemovalPolicy.RETAIN,
});
```

### Outputs
```typescript
new cdk.CfnOutput(this, 'VpcId', {
    value: vpc.vpcId,
    description: 'VPC ID',
    exportName: 'MyVpcId',
});

new cdk.CfnOutput(this, 'DatabaseEndpoint', {
    value: database.dbInstanceEndpointAddress,
    description: 'Database endpoint',
});
```

---

## Troubleshooting Guide

### SSH Connection Issues

**Problem:** Permission denied (publickey)
```bash
# Solution 1: Check key permissions
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh

# Solution 2: Specify correct key
ssh -i /path/to/key.pem user@host

# Solution 3: Debug SSH connection
ssh -vvv user@host  # Verbose output

# Solution 4: Check SSH service
systemctl status ssh
sudo systemctl restart ssh
```

**Problem:** Connection timeout
```bash
# Solution: Check security group rules
aws ec2 describe-security-groups

# Check if host is reachable
ping hostname
traceroute hostname

# Check if SSH port is listening
netstat -tuln | grep 22
```

### Git Issues

**Problem:** Cannot push to repository
```bash
# Solution 1: Check remote URL
git remote -v

# Solution 2: Update remote
git remote set-url origin new-url

# Solution 3: Check credentials
git config --global user.name
git config --global user.email
```

**Problem:** Merge conflicts
```bash
# View conflicts
git diff

# Resolve manually, then:
git add resolved-file
git commit -m "Resolve merge conflict"

# Or abort merge
git merge --abort
```

### AWS Issues

**Problem:** Access Denied errors
```bash
# Check IAM permissions
aws iam get-user

# Check role/policy
aws iam list-attached-user-policies --user-name username

# Verify credentials
aws sts get-caller-identity
```

**Problem:** CloudFormation stack creation failed
```bash
# View stack events
aws cloudformation describe-stack-events --stack-name stack-name

# View stack status
aws cloudformation describe-stacks --stack-name stack-name

# Debug template
aws cloudformation validate-template --template-body file://template.yaml
```

### Docker Issues

**Problem:** Cannot build image
```bash
# Check Docker daemon
systemctl status docker

# Check Docker logs
journalctl -u docker -n 50

# Rebuild with no cache
docker build --no-cache -t image-name:tag .

# Check Dockerfile syntax
docker build --progress=plain -t image-name:tag .
```

**Problem:** Container won't start
```bash
# Check logs
docker logs container-name

# Run interactive
docker run -it image-name bash

# Inspect image
docker inspect image-name
```

---

**Last Updated:** January 20, 2026  
**Quick Reference for:** DPL DevOps Training Program
