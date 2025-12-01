<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Advanced Git Concepts • GitHub Integration</h3>

---

## 🎯 Objective Recap
- Deep dive into Git's internal workings and configuration management.
- Master branch operations, merge strategies, and conflict resolution techniques.
- Explore Git diff, stashing mechanisms, and advanced workflow patterns.
- Understand Git rebase as an alternative to merging for cleaner history.
- Learn GitHub remote repository operations and SSH authentication.
- Practice creating Pull Requests and contributing to open source projects.
- Capture comprehensive proof for all advanced Git concepts learned.

---

## 🛠️ Lab Environment
- **Host:** Windows 11 with WSL/Terminal.
- **Git Version:** Latest Git for Windows with Git Bash integration.
- **Editor:** VS Code configured as Git's default editor.
- **Remote:** GitHub account with SSH key authentication.
- **Practice Repository:** Local `git_exercise` directory with multiple subdirectories.

![Getting started with Git](images/getting%20started%20with%20git%20using%20the%20wasp%20terminal.png)

---

## 📚 Git Learning Journey (YouTube Series)
**Source:** [Complete Git Tutorial Series](https://www.youtube.com/watch?v=zTjRZNkhiEU)

| Timestamp | Chapter | Deep Dive Notes |
|-----------|---------|-----------------|
| ⌨️ 0:40:02 | Git Internal Working and Configs | Explored Git's object model (blobs, trees, commits), internal file structure within `.git/`, configuration hierarchies (local vs global), and how Git tracks changes at the filesystem level. |
| ⌨️ 1:07:47 | Git Merge and Git Conflicts | Mastered branch creation, switching strategies, merge workflows (fast-forward vs three-way), conflict identification, resolution techniques, and branch lifecycle management. |
| ⌨️ 1:47:21 | Git Diff and Stashing | Deep dive into change visualization, diff algorithms, staging/unstaging workflows, stash stack management, and applying stashes across branches. |
| ⌨️ 2:15:42 | Git Rebase is Not That Scary | Learned interactive rebase, rewriting history safely, rebase vs merge trade-offs, and maintaining linear project history for cleaner collaboration. |
| ⌨️ 2:37:24 | Insight of Pushing Code to GitHub | Explored remote repository setup, SSH key generation and authentication, remote URL configuration, push/pull workflows, and understanding remote tracking branches. |
| ⌨️ 3:18:18 | How to Make Pull Request and Open Source Contribution | Mastered fork workflow, creating feature branches, submitting Pull Requests, code review processes, and contributing to open source projects following best practices. |

---

## 🔧 Chapter 1: Git Internal Working and Configs (⌨️ 0:40:02)

### 1.1 Repository Initialization and Structure
- Created a dedicated practice directory structure to experiment with Git commands in isolation.
- Initialized Git repositories in subdirectories to understand how `.git/` folders work independently.

![Creating practice directory](images/making%20a%20directory%20to%20practice%20the%20git%20commands%20on%20and%20naming%20it%20git_exersice.png)

![Setting up subdirectories](images/making%203%20different%20directory%20inside%20teh%20git_exercise%20dir%20so%20we%20can%20apply%20git%20commpnds%20and%20the%20main%20dir%20is%20not%20empty%20.png)

![Initializing Git in subdirectory](images/initilising%20and%20cheacking%20the%20status%20of%201%20sub%20dir%20named%20git1%20in%20teh%20git_exercise%20dir%20.png)

### 1.2 Exploring `.git/` Directory Structure
- Examined the hidden `.git/` folder to understand how Git stores metadata, objects, and references.
- Explored key directories: `objects/`, `refs/`, `config`, `HEAD`, and `index` to see Git's internal tracking mechanism.

![Accessing hidden .git folder](images/getting%20the%20access%20of%20the%20hidden%20folder%20git%20which%20keeps%20tracks%20of%20the%20fildes%20we%20uploades%20and%20everythimng%20.png)

![Exploring Git folder contents](images/getting%20the%20access%20of%20the%20git%20folder%20and%20its%20contents%20to%20see%20what%20kind%20of%20info%20is%20being%20saved%20in%20the%20git%20folder.png)

### 1.3 Git Configuration Management
- Configured global Git settings including user identity (name and email) that will be attached to all commits.
- Reviewed how configuration cascades from system → global → local, and where each config file resides.

![Viewing Git config](images/getting%20teh%20git%20logs%20and%20ststus%20to%20see%20teh%20config%20files%20contents%20.png)

![Setting global config](images/adding%20my%20name%20and%20email%20in%20teh%20git%20config%20file%20using%20teh%20config%20global%20command%20.png)

### 1.4 Editor Configuration
- Changed Git's default editor from vim to VS Code for more comfortable commit message editing.
- Verified the configuration takes effect immediately for interactive Git operations.

![Configuring VS Code as editor](images/made%20the%20vs%20code%20my%20default%20editor%20fot%20teh%20message%20writing%20insted%20of%20it%20beinmg%20vim%20.png)

### 1.5 `.gitignore` Best Practices
- Created `.gitignore` files to exclude sensitive data (`.env` files) and editor-specific directories (`.vscode/`).
- Validated that ignored files no longer appear in `git status`, preventing accidental commits of unwanted files.

![Creating gitignore](images/using%20teh%20git%20ignore%20to%20make%20sure%20thta%20teh%20sensitive%20or%20unwanted%20fils%20are%20not%20being%20added%20to%20git%20.png)

![Verifying gitignore effect](images/before%20and%20after%20teh%20gitignote%20and%20seeing%20the%20status%20to%20varify%20that%20the%20.env%20and%20vscode%20folder%20are%20not%20being%20shown%20in%20the%20stasus%20.png)

### 1.6 Staging and Committing Workflow
- Practiced the complete workflow: creating files, staging with `git add`, and committing with meaningful messages.
- Observed how files transition from untracked → staged → committed states.

![Files before staging](images/making%202%20txt%20files%20in%20teh%20git1%20dir%20befor%20git%20add%20command%20.png)

![Files after staging](images/making%202%20txt%20files%20in%20teh%20git1%20dir%20after%20git%20add%20command%20.png)

![Making first commit](images/cometing%20the%20changes%20like%20teh%20two%20files%20in%20the%20git%20using%20add%20command%20with%20a%20message%20using%20m%20command%20.png)

---

## 🌳 Chapter 2: Git Merge and Git Conflicts (⌨️ 1:07:47)

### 2.1 Branch Fundamentals
- Introduced the concept of branches as independent development lines within the same repository.
- Understood how branches enable parallel work without interfering with main codebase.

![Starting with branches](images/getting%20started%20with%20branch.png)

### 2.2 Creating and Switching Branches
- Created a new branch called `nav-bar` for feature development.
- Practiced switching between branches using `git checkout` and observed how the working directory updates.

![Creating nav-bar branch](images/creating%20and%20changing%20a%20new%20branch%20called%20nav%20bar%20.png)

### 2.3 Working Across Multiple Branches
- Made isolated changes in both `master` and `nav-bar` branches to simulate real-world feature development.
- Tracked how each branch maintains its own commit history independently.

![Working in master branch](images/working%20in%20master%20branch%20.png)

![Working in nav-bar branch](images/working%20in%20the%20nav-bar%20branch%20.png)

### 2.4 HEAD Reference Tracking
- Verified that `HEAD` points to the current branch, and how Git tracks which branch is active.
- Explored how branch pointers move forward with each new commit.

![Checking HEAD position](images/cheaching%20that%20teh%20git%20logs%20have%20teh%20head%20pointing%20the%20head%20to%20the%20nav-bar%20breamnch%20.png)

### 2.5 Merging Branches
- Merged the `nav-bar` feature branch back into `master` to integrate completed work.
- Observed how Git combines changes from two branches into a unified history.

![Merging nav-bar into master](images/mearged%20the%20navbar%20breanch%20into%20master%20.png)

### 2.6 Branch Lifecycle Management
- Practiced the complete branch lifecycle: creation, development, merging, and deletion.
- Learned when and how to safely delete merged branches to keep repository clean.

![Branch lifecycle practice](images/preactice%20the%20deletion%20creation%20and%20meargingof%20a%20branch%20.png)

![Deleting merged branch](images/deleted%20the%20nav%20bar%20branch.png)

### 2.7 Merge Conflict Resolution
- Intentionally created conflicting changes to understand how merge conflicts occur.
- Practiced conflict resolution workflow: identifying conflicts, editing files manually, and completing the merge.
- Learned that conflicts happen when Git cannot automatically reconcile changes to the same lines.

![Merge conflict encountered](images/getting%20a%20mearged%20conflicts%20and%20fixing%20it%20.png)

### 2.8 Visualizing Branch History
- Used Git's graph visualization to see how branches diverge and converge.
- Understood the difference between linear and branching commit histories.

![Branch graph visualization](images/teh%20git%20graph%20showing%20teh%20branch%20mearged%20and%20different%20branch%20works%20.png)

---

## 📊 Chapter 3: Git Diff and Stashing (⌨️ 1:47:21)

### 3.1 Understanding Git Diff
- Explored the `git diff` command to see unstaged changes in the working directory.
- Learned how diff output shows additions (green/+) and deletions (red/-) with context lines.

![Starting with git diff](images/getting%20started%20with%20teh%20git%20diff%20command%20.png)

### 3.2 Advanced Diff Operations
- Compared changes across multiple files to see comprehensive modifications.
- Used diff to review changes before staging them, ensuring quality before committing.

![Multi-file diff](images/updateing%20multipal%20hile%20and%20using%20teh%20git%20diff%20commands%20to%20see%20the%20changes%20made%20in%20the%20timeline.png)

### 3.3 Branch Comparison with Diff
- Used branch references with diff to compare entire branches, not just working directory changes.
- Understood how to see what differs between feature branches and main branch.

![Branch comparison](images/using%20teh%20branch%20id%20to%20see%20the%20diff%20in%20the%20whole%20branch%20by%20compairing%20.png)

### 3.4 Stashing Fundamentals
- Encountered a scenario where uncommitted changes prevented branch switching.
- Learned that `git stash` temporarily saves work-in-progress without committing.

![Branch switch error](images/getting%20the%20error%20msg%20that%20i%20cant%20switch%20the%20branch%20woithout%20the%20commiting%20the%20changes%20of%20the%20current%20branch.png)

### 3.5 Applying Stashes Across Branches
- Used `git stash pop` to retrieve stashed changes in a different branch.
- Understood how stashes are stored separately from commits and can be applied anywhere.

![Popping stash in another branch](images/using%20teh%20git%20stash%20pop%20to%20get%20teh%20stash%20in%20an%20other%20branch%20.png)

---

## 🔄 Chapter 4: Git Rebase is Not That Scary (⌨️ 2:15:42)

### 4.1 Understanding Rebase
- Learned that rebase rewrites commit history by replaying commits from one branch onto another.
- Understood the key difference: merge creates a merge commit, rebase creates a linear history.

### 4.2 Interactive Rebase Practice
- Performed an interactive rebase on the `bugfix` branch to clean up merge commits.
- Used rebase to remove unnecessary commits and create a cleaner, more readable history.

![Using rebase command](images/used%20the%20rebase%20command%20in%20the%20bugfix%20branch%20to%20delete%20the%20extra%20meagred%20commiets%20.png)

### 4.3 Rebase vs Merge Trade-offs
- Explored when to use rebase (clean history, feature branches) vs merge (shared branches, preserving context).
- Learned best practices: rebase local commits, never rebase shared/public branches.

---

## 🚀 Chapter 5: Insight of Pushing Code to GitHub (⌨️ 2:37:24)

### 5.1 SSH Key Generation
- Generated SSH keys using Git Bash to establish secure authentication with GitHub.
- Created public/private key pair for passwordless remote access.

![Creating SSH key](images/using%20git%20bash%20to%20create%20the%20ssg%20key%20.png)

### 5.2 SSH Agent Configuration
- Researched GitHub documentation to properly configure SSH agent for key management.
- Added SSH keys to GitHub account secrets and verified authentication flow.

![GitHub SSH documentation](images/searching%20the%20github%20docs%20to%20find%20all%20the%20info%20on%20ssh%20agent%20and%20how%20to%20connect%20it%20in%20the%20secriats.png)

### 5.3 Remote Repository Operations
- Configured remote repository URLs using SSH protocol (`git@github.com:user/repo.git`).
- Practiced pushing local commits to remote and pulling remote changes.
- Understood how remote tracking branches (`origin/master`) sync with local branches.

### 5.4 Understanding Push Workflow
- Learned that `git push` sends local commits to remote repository.
- Explored how Git tracks which local branch maps to which remote branch.
- Understood the concept of "upstream" branches and setting them with `-u` flag.

### 5.5 Authentication and Security
- Verified SSH key authentication eliminates need for username/password prompts.
- Explored how SSH keys provide secure, encrypted communication with GitHub servers.

---

## 🔀 Chapter 6: How to Make Pull Request and Open Source Contribution (⌨️ 3:18:18)

### 6.1 Fork Workflow Fundamentals
- Learned the standard open source contribution workflow: fork → clone → branch → commit → push → PR.
- Understood that forking creates a personal copy of someone else's repository.

### 6.2 Creating Feature Branches
- Practiced creating dedicated branches for each feature or bug fix.
- Followed naming conventions like `feature/add-navbar` or `fix/login-bug` for clarity.

### 6.3 Pull Request Lifecycle
- Explored how Pull Requests enable code review before merging changes.
- Understood PR descriptions, linking issues, and responding to review feedback.
- Learned that PRs provide discussion context and maintain project history.

### 6.4 Open Source Best Practices
- Studied how to contribute effectively: finding issues, reading contribution guidelines, writing good commit messages.
- Learned to keep PRs focused on single changes, write descriptive PR titles, and update documentation.

### 6.5 Code Review Process
- Understood the collaborative nature of open source: maintainers review, suggest changes, and approve contributions.
- Learned to iterate based on feedback and maintain respectful communication.

![Learning completion](images/compleated%20the%20part%20of%20learning%20the%20github%20.png)

---

## 🎓 Key Learnings Summary

### Git Internals
- Git stores everything in `.git/` directory: objects (blobs/trees/commits), references (branches/tags), and configuration.
- Configuration cascades: system → global → local, allowing fine-grained control.
- `.gitignore` prevents tracking unwanted files while maintaining clean repository state.

### Branching and Merging
- Branches enable parallel development without code interference.
- Merge combines branch histories, creating merge commits in the process.
- Conflicts occur when Git cannot automatically reconcile changes; resolution requires manual intervention.

### Advanced Workflows
- `git diff` provides powerful change visualization at multiple levels (working directory, staged, branches).
- `git stash` enables context switching without committing incomplete work.
- Rebase rewrites history for cleaner linear progression, but should only be used on local branches.

### GitHub Integration
- SSH keys provide secure, passwordless authentication for remote operations.
- Remote repositories enable collaboration and backup of local work.
- Understanding remote tracking branches is crucial for effective push/pull workflows.

### Open Source Collaboration
- Pull Requests enable code review and discussion before merging.
- Fork workflow allows contributing to projects without direct access.
- Good practices: clear commit messages, focused PRs, responsive to feedback.

---

## ✅ Evidence Checklist
- All 34 screenshots documenting Git learning journey are stored in `2025-12-1/images/` directory.
- Images are properly categorized and referenced within their respective sections above.
- Final two chapters (GitHub and Pull Requests) were learned in extreme detail through hands-on practice, even without screenshots.
- Every concept covered in the YouTube series has been thoroughly practiced and documented.
- Repository structure maintains consistency with previous daily reports.

---

## 🔄 Practice Repository Structure
```
git_exercise/
├── git1/          # First practice repository
├── [other dirs]/  # Additional practice directories
└── .git/          # Git internal tracking (hidden)
```

---

**Next Review Window:** Ready to apply advanced Git concepts in real-world projects. Continue practicing rebase workflows, conflict resolution, and GitHub collaboration patterns. Consider contributing to open source projects to solidify Pull Request workflow.

---

**Learning Progress:** Advanced Git concepts mastered. Ready for production-level version control workflows. 🚀

---

## 🧭 New Topic: Gitflow Workflow (Legacy Branching Strategy)

- Studied Atlassian’s Gitflow guide in depth to understand why the model relies on parallel `main` and `develop` branches, how release/hotfix branches isolate stabilization work, and why the workflow fits scheduled releases despite falling out of favor for modern trunk-based CI/CD.
- Practiced the entire lifecycle (feature → develop, release → main+develop, hotfix → main+develop) using pure `git checkout` and `git merge` sequences because installing the `git-flow` extension was blocked by admin controls; documented the exact command pairs as a drop-in alternative to `git flow feature|release|hotfix start/finish`.
- Highlighted operational guardrails learned from the article—never merge feature branches directly into `main`, always merge hotfixes back to `develop`, and tag production releases off `main` for traceability.
- Reflected on practical trade-offs: Gitflow’s clarity for regulated releases versus the overhead of long-lived branches, and noted scenarios where I would still reach for it (multi-sprint QA cycles, staggered release trains).

Reference: [Atlassian – Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)