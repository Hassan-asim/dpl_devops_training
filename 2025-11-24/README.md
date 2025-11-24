<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#00a86b;">Daily DevOps Practice • AWS Essentials • Linux CLI</h3>

---

## 🎧 Study Log – Linux Essentials Video (Continuation)

I picked up the same **Linux Essentials** walkthrough on YouTube: https://www.youtube.com/watch?v=sWbUDq4S6Y8 and focused on the next chapters to reinforce workstation usage before diving back into AWS services.

- ⌨️ 1:34:29 – Chapter 5: System Configuration from the Graphical Interface  
- ⌨️ 2:04:27 – Chapter 6: Common Applications  
- ⌨️ 2:12:57 – Chapter 7: Command Line Operations  

Chapter 5 refreshed desktop-driven administration, Chapter 6 surveyed the most common Linux applications, and Chapter 7 dove into the CLI tools I will rely on when managing Amazon Linux 2 without a GUI.

---

## 🌩️ AWS Cloud Technical Essentials – Course Work

I completed the **AWS Cloud Technical Essentials** learning path on Coursera (verification link: https://www.coursera.org/learn/aws-cloud-technical-essentials?utm_source=mobile&utm_source=link&utm_medium=page_share&utm_content=lih&utm_campaign=card_button). The shareable certificate will be placed inside `images/` as soon as I download it from Coursera Plus.

### Key takeaways

- Practiced spinning up an EC2 instance from the AWS Console and reviewed how key pairs, security groups, and IAM roles drive access control.
- Revisited storage differences: Amazon EC2 for compute, Amazon S3 for object storage, and Amazon EBS for block-level volumes that can be attached/detached per instance.
- Compared database families: when to pick Amazon RDS engines for relational workloads versus Amazon DynamoDB for fully-managed NoSQL, and how each scales.
- Walked through foundational monitoring (CloudWatch metrics/alarms) and cost-optimization tips that the course pairs with the shared responsibility model.
- Used the Coursera-provided AWS training console to complete the guided labs; without a paid AWS account I cannot extend experiments beyond the sandbox yet.

---

## 🧪 Hands-on Practice – Amazon Linux 2 VM Attempt

- Tried to boot the Amazon Linux 2 VirtualBox image again, this time without attaching a desktop environment. The VM launched, but because AL2 is CLI-only by default, I struggled to navigate beyond the login prompt.
- Ran through the Coursera lab instructions and attempted `sudo yum update` plus `sudo yum install nodejs`, yet both commands failed (screenshot attached) and I could not diagnose the repo/connection issue before time ran out.
- Tested copy/paste and file sharing settings in VirtualBox so I can move command snippets from Windows into the VM more easily; clipboard sharing still behaves inconsistently.
- Followed along with the course material to run basic commands (package updates, service checks), but I still need more comfort operating purely from the terminal.
- Watched “How to run Amazon Linux 2 on premises (locally) as a VM” (https://www.youtube.com/watch?v=oYo1LHbEKyI&t=26s) as an additional helper, but despite the walkthrough I still couldn’t get the CLI commands to succeed on my own VM.
- Next step: map each CLI task from Chapter 7 to equivalent AL2 commands so I can manage the instance confidently even without a GUI, and retry the package installs once I sort out the networking/yum errors.

---

## 📸 Assets & To-Dos

![AWS console dashboard](images/dashboard%20of%20aws%20consol%20.png)

![Coursera certificate placeholder](images/Screenshot%202025-11-24%20143837.png)

![Amazon Linux 2 boot sequence](images/start%20of%20vm%20amazon%20linux%202.png)

![Failed yum/node attempt](images/tried%20installing%20the%20nodejs%20and%20updating%20the%20system%20using%20sudo%20yam%20install%20update%20but%20resulted%20if%20falier%20dont%20knoiw%20why%20.png)

![VirtualBox sharing settings](images/updating%20teh%20setting%20so%20i%20can%20shaer%20the%20files%20and%20clipboard%20from%20and%20to%20my%20vm%20to%20th%20elocal%20mechine%20.png)

- `images/` – holds the day’s screenshots above (including the failed yum attempt to document today’s blockers) and will store the official Coursera certificate once downloaded.  
- I will also capture the Amazon Linux 2 console output once I have a cleaner workflow.

---

## 📚 References

- Linux Essentials video (timestamps above).  
- AWS Cloud Technical Essentials – Coursera verification link listed earlier.  
- How to run Amazon Linux 2 on premises (locally) as a VM – https://www.youtube.com/watch?v=oYo1LHbEKyI&t=26s  
