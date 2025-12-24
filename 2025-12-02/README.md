<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • Trunk‑Based Development • Git Merge & Workflows</h3>

---

## 🎯 Objective Recap
- **Understand modern branching strategies**: Trunk‑Based Development, GitHub Flow, Gitflow, release branches, environment branches, and forking workflows.
- **Deep dive into Git merge behavior**: fast‑forward vs non‑fast‑forward merges, when to use `--no-ff`, and how merge commits shape history.
- **Compare merge vs rebase**: trade‑offs for history clarity, collaboration safety, and how to recover using `git reflog` and `git reset`.
- **Connect theory to CI/CD reality**: how branching models impact continuous integration, release cadence, and team structure.

> Today was **reading/theory‑heavy**: I focused on high‑quality articles, official docs, and videos instead of hands‑on terminal practice. Proof of learning is via screenshots of the resources inside `images/`.

---

## 🛠️ Study Environment
- **Host OS:** Windows 11
- **Browser:** Chrome (used to read Git / workflow docs and watch videos)
- **Focus Area:** Git branching models, merge strategies, and modern collaboration flows (no local repo experimentation today)
- **Evidence:** Screenshots of learning resources stored in `2025-12-2/images/`

---

## 📚 Study Sources Overview

| Category | Resource | What I Focused On |
|---------|----------|-------------------|
| Trunk‑Based Development | [Trunk‑Based Development – main site](https://trunkbaseddevelopment.com/) | Core ideas of committing frequently to a single trunk, short‑lived branches, feature flags, and how this supports CI/CD. |
| Deciding Factors | [Deciding factors](https://trunkbaseddevelopment.com/deciding-factors/) | How iteration length, story size, build times, repo size, Conway’s law, DB migrations, and shared code policies affect whether trunk‑based is a good fit. |
| Git Merge Internals | [git‑merge examples](https://git-scm.com/docs/git-merge#_examples) | How fast‑forward vs true merge works, options like `--no-ff`, and what Git actually does during a merge. |
| FF vs no‑FF | [Stack Overflow – fast forward vs no fast forward](https://stackoverflow.com/questions/6701292/git-fast-forward-vs-no-fast-forward-merge) | When to keep a linear history vs when to force a merge commit to preserve feature branch boundaries. |
| Merge vs `--no-ff` | [Hackr – Difference between git merge and git merge --no-ff](https://hackr.io/blog/difference-between-git-merge-and-git-merge-no-ff) | Practical examples of `git merge` vs `git merge --no-ff` and how each affects `git log`. |
| Gitflow | [Atlassian – Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) | Roles of `main`, `develop`, feature, release, and hotfix branches; pros/cons in modern teams. |
| GitHub Flow | [GitHub Flow – official docs](https://docs.github.com/en/get-started/using-github/github-flow) | Lightweight feature‑branch workflow with continuous deployment and small pull requests. |
| Rebase vs Merge | Google search result for “Rebasing vs Merging git reflog git reset --hard HEAD@{2}” | Conceptual difference between merge and rebase, plus using `git reflog` and `git reset` to undo bad history rewrites. |
| Branching Strategies (Video) | YouTube: multi‑strategy video with chapters (Trunk‑Based, GitHub Flow, Forking, Release, Gitflow, Env branches) | Side‑by‑side comparison of common Git strategies and when each is appropriate. |
| Trunk‑Based Deep Dive (Video) | [Git Trunk‑Based Development – YouTube](https://www.youtube.com/watch?v=mB4O49B51Xs&t=114s) | Principles, implementation steps, feature toggles, and CI practices specific to trunk‑based teams. |

All these are backed by screenshots in the `images/` directory (e.g. `trunkbaseddevlopment.png`, `git-scm.png`, `atlassian.png`, `github docs.png`, `hackr.png`, `stackoverflow.png`, `merging vs rebasing.png`).

---

## 🌳 Trunk‑Based Development (TBD) in Depth

### 1. Core Principles
- **Single shared trunk**: Almost all development happens directly on `main`/`trunk`, not long‑lived feature branches. Short‑lived branches (hours → a couple of days) are allowed but must merge back quickly.  
- **“Do not break the build” mindset**: Every commit to trunk must keep the build green; CI runs on each change to catch regressions early.  
- **Small, incremental stories**: Work is sliced into tiny changes that can safely be integrated frequently instead of multi‑week branches.  
- **Feature flags / toggles**: Incomplete work is hidden behind flags while still being merged into trunk, supporting continuous delivery without exposing half‑finished features.  
- **Continuous Integration & Delivery**: Trunk remains always releasable; deployment pipelines regularly ship changes straight from trunk.

Reference: [Trunk‑Based Development – main site](https://trunkbaseddevelopment.com/)

### 2. Deciding Factors for/against TBD

From the **“Deciding factors”** article I learned how organizational and technical context can make trunk‑based easier or harder to adopt [Trunk‑Based Development – Deciding factors](https://trunkbaseddevelopment.com/deciding-factors/):

- **Iteration length & release cadence**
  - Teams with **short iterations or continuous delivery** align naturally with trunk‑based development.
  - Long cycles (e.g. 4‑week iterations with rigid “hardening” phases) push teams toward heavier branch‑based models and reduce the benefit of committing straight to trunk.
- **Story size**
  - TBD relies on **small, INVEST‑style stories**—ideally changes that are started and finished in hours, not weeks.
  - Large stories push teams to create long‑lived feature branches, which drifts away from trunk‑based principles.
- **Build times**
  - Fast builds (a few minutes) allow frequent trunk commits and rapid feedback.
  - Slow builds (30+ minutes) discourage frequent integration; developers batch work and commit less often, again pushing toward longer‑lived branches.
- **VCS technology choice**
  - The VCS must support **fast fetch/pull/clone** operations so developers can sync trunk several times a day.
  - Very slow systems (e.g. older ClearCase/PVCS examples with 30–45 minute syncs) make true trunk‑based development almost impossible.
- **Repo size and binaries**
  - Git works best when history stays reasonably sized; huge monorepos with many binaries may need techniques like Git‑LFS, shallow clones, or even archive/rotate strategies.
  - The article mentions **Perforce** and **Subversion** as better fits when you need to store massive binary artifacts alongside source.
- **Peak commit frequency & the “race to push”**
  - On very busy repos, multiple devs race to push to trunk; failing pushes require re‑pulling and re‑merging.
  - Tools like **bors‑NG** (a merge bot) or GitHub’s PR queues help serialize merges safely while preserving a trunk‑based workflow.
- **Conway’s Law & organization structure**
  - If the company is structured into many independent teams, a huge monorepo with pure trunk might fight reality; the article hints that in such cases **microservices** or more modular repos sometimes align better with Conway’s Law.
- **Database migrations**
  - To practice TBD safely with relational databases, schema changes and data migrations must be **incremental, reversible, and versioned** alongside application code.
  - The article points to **evolutionary database design** as a companion discipline.
- **Shared code and ownership**
  - Trunk‑based teams usually have **shared code ownership**: everyone can read everything and contribute across the tree.
  - There may be per‑directory write rules and review expectations, but no “hidden” areas of the codebase.

---

## 🔀 Git Merge Strategies: Fast‑Forward vs Non‑Fast‑Forward

### 1. How `git merge` works (from official docs)

Reading the `git-merge` manual examples clarified the difference between **fast‑forward** and **true merge** [git‑merge examples](https://git-scm.com/docs/git-merge#_examples):

- **Fast‑forward merge**
  - Happens when the current branch tip is an **ancestor** of the branch being merged.
  - Git can simply **move the branch pointer forward**; no new merge commit is created.
  - History stays *perfectly linear*; it looks as if all commits were made directly on the target branch.
- **True (three‑way) merge**
  - Required when branches have diverged (both have unique commits).
  - Git finds a **common ancestor**, then combines changes from both branches to create a new **merge commit**.
  - This merge commit has two parents and clearly shows that two lines of development were joined.

The docs also highlight configuration such as `merge.ff`, `merge.stat`, and tools like `git mergetool` for conflict resolution.

### 2. Fast‑Forward vs `--no-ff`

From community explanations and articles [Stack Overflow – git fast forward vs no fast forward merge](https://stackoverflow.com/questions/6701292/git-fast-forward-vs-no-fast-forward-merge), [Hackr – Difference between git merge and git merge --no-ff](https://hackr.io/blog/difference-between-git-merge-and-git-merge-no-ff):

- **Default (`git merge` with fast‑forward allowed)**
  - If a fast‑forward is possible, Git will not create a merge commit.
  - Pros: cleaner, linear history; easier to follow for solo work or tight trunk‑based integration.
  - Cons: you lose the **explicit record of the feature branch**—commits look like they were made directly on `main`.
- **`git merge --no-ff`**
  - Forces Git to create a **merge commit** even when a fast‑forward is possible.
  - Pros:
    - Keeps the **feature branch boundary** visible in `git log` / `git log --graph`.
    - Makes it easier to see which commits belonged to a specific feature or pull request.
  - Cons:
    - Adds extra merge commits, which can clutter history if used for every tiny change.

**Practical guideline I took away:**
- For **small, trunk‑based, or solo changes**, fast‑forward merges are often ideal.
- For **team features merged via Pull Requests**, `--no-ff` (or equivalent PR settings) can make it easier to audit and revert a feature as a unit.

---

## 🔁 Rebase vs Merge + Recovery with `git reflog`

### 1. Conceptual difference: Merge vs Rebase

From the “Rebasing vs Merging” readings (via the Google search link in the prompt), I reinforced the classic comparison:

- **Merge**
  - Preserves the **true history**: all commits stay where they were created, plus a merge commit.
  - Good for **shared branches** where other people may already have based work on existing commits.
  - History can become “branchy” with many merge commits, but it is faithful to what actually happened.
- **Rebase**
  - **Replays commits** from one branch on top of another, creating *new* commits with new SHAs.
  - Produces a **linear, clean history** that looks like the feature branch was always up‑to‑date with the target branch.
  - Dangerous if you rebase commits that are already pushed/shared, because it rewrites history that collaborators depend on.

The main rule I noted again: **rebase local/private work, merge shared/public branches.**

### 2. Using `git reflog` and `git reset` for safety

The same materials (and examples from the Google search result) emphasized:

- **`git reflog`**
  - Keeps a **local log of every HEAD movement** (checkouts, commits, rebases, resets, merges).
  - Even if I “lose” commits after a bad rebase or reset, reflog shows entries like `HEAD@{2}`, `HEAD@{5}`, etc.
- **`git reset --hard HEAD@{2}`**
  - Lets me **jump back to a previous HEAD position**, essentially undoing a rebase or merge gone wrong.
  - `--hard` also resets the working directory and index to that point, so it must be used carefully.

Key takeaway: experimenting with advanced history manipulation (rebase, `reset --hard`) is much safer once you know how to read `git reflog` and restore earlier states.

---

## 🧬 Branching & Workflow Models Compared

### 1. Gitflow Workflow (Atlassian)

From Atlassian’s Gitflow guide [Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow):

- **Main branches**
  - `main`: always represents **production releases**.
  - `develop`: integration branch where features are merged before being promoted to production.
- **Supporting branches**
  - **Feature branches**: branch from `develop`, merge back into `develop` when complete.
  - **Release branches**: branch from `develop` to stabilize a release; once ready, merge into `main` *and* back into `develop`.
  - **Hotfix branches**: branch from `main` to fix production issues quickly; merge back into both `main` and `develop`.
- **Use cases and trade‑offs**
  - Great for **scheduled releases**, longer QA cycles, and environments where production must be very stable.
  - Heavier and more complex than trunk‑based or GitHub Flow, which is why many modern teams are moving away from pure Gitflow.

### 2. GitHub Flow

From the official GitHub docs [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow):

- **Core loop**
  1. Create a **branch** from `main` for each small change.
  2. Commit and push regularly.
  3. Open a **Pull Request** early for discussion.
  4. CI runs on the PR.
  5. Once approved and passing, merge back into `main`.
  6. Deploy from `main` frequently (often automatically).
- **Characteristics**
  - Designed for **continuous deployment** and **small, frequent changes**.
  - No separate `develop` branch, release branch, or long‑lived env branches.

### 3. Forking Strategy

From the YouTube and article content:

- Common in **open source**:
  - Contributors fork the main repo into their own namespace.
  - They create feature branches in their fork, then open PRs back to the original (`upstream`) repository.
- Pros:
  - Maintainers don’t need to grant write access to everyone.
  - Contributors can experiment freely without risking the upstream repo.
- Cons:
  - Slightly more complex remote management (`origin` vs `upstream`).

### 4. Release Branches & Environment Branches

From the multi‑strategy video (chapters around **Release branches**, **Git Flow**, and **Environment branches**):

- **Release branches**
  - Used to **stabilize a particular version** while new work continues on `develop` or `main`.
  - Helpful when you need a “code freeze” area separate from ongoing feature development.
- **Environment branches (e.g., `dev`, `qa`, `staging`, `prod`)**
  - Each branch corresponds to a **deployment environment**.
  - Teams merge or cherry‑pick changes between them as code moves through the pipeline.
  - This is powerful but can become complex, especially when hotfixes must be synchronized across all env branches.

### 5. Trunk‑Based vs Gitflow vs GitHub Flow (Video Summary)

From the video that compared multiple strategies (timecodes in the prompt: Trunk‑Based, feature branches/GitHub Flow, forking, release branches, Gitflow, environment branches):

- **Trunk‑Based Development**
  - Minimal branching, heavy emphasis on **CI/CD**, feature flags, and small increments.
  - Simplifies merges and reduces “big bang” integration risk.
- **GitHub Flow**
  - Still trunk‑centric but relies on **short‑lived feature branches and PRs**.
  - Great for SaaS apps and teams shipping multiple times per day.
- **Gitflow**
  - Best for **enterprise, regulated, or on‑prem products** with clear release trains.
  - More overhead: more branches to manage and more merge choreography.
- **Choosing a strategy**
  - For high‑frequency deployment and modern CI/CD, **Trunk‑Based** or **GitHub Flow** generally win.
  - For slower, batch releases with heavy QA, **Gitflow** and **release branches** may still be appropriate.

---

## 🌲 Trunk‑Based Development vs Gitflow (Dedicated Video)

From the focused Trunk‑Based Development video [Git Trunk‑Based Development](https://www.youtube.com/watch?v=mB4O49B51Xs&t=114s):

- **What is TBD?**
  - Frequent commits to trunk, ideally multiple times per day.
  - Use of **feature toggles** to hide incomplete features in production.
  - Continuous integration ensures trunk is always in a deployable state.
- **TBD vs Gitflow**
  - Gitflow relies on multiple long‑lived branches; TBD tries to avoid them.
  - Gitflow fits slower, batch‑style releases; TBD is optimized for **continuous delivery**.
  - TBD reduces integration risk by merging early and often; Gitflow defers integration until the end of features or releases.
- **Implementing TBD**
  - Invest in **automated tests**, fast CI, and good monitoring.
  - Break down work into very small, independently releasable slices.
  - Culture change: devs must be disciplined about not breaking trunk and writing safe, incremental changes.

---

## 🎓 Key Learnings Summary

- **Branching strategies shape delivery speed**: Trunk‑Based and GitHub Flow favor rapid, incremental releases; Gitflow and heavy release branching favor structured, slower cadences.
- **Merge options (`ff` vs `--no-ff`) are about history readability vs simplicity**: fast‑forward keeps history linear; `--no-ff` preserves feature boundaries and PR context.
- **Rebase is powerful for cleaning history but dangerous on shared branches**; learning `git reflog` and `git reset --hard HEAD@{n}` is critical for safe experimentation.
- **Technical constraints (build times, repo size, VCS performance) and organizational structure (Conway’s Law) directly impact whether Trunk‑Based Development is realistic.**

---

## ✅ Evidence Checklist
- All learning today was theory‑driven from **articles, docs, and videos** listed above.
- Screenshots of each key resource are saved under `2025-12-2/images/`:
  - `trunkbaseddevlopment.png` – main Trunk‑Based Development site.
  - `git-scm.png` – `git-merge` documentation.
  - `atlassian.png` – Gitflow workflow article.
  - `github docs.png` – GitHub Flow documentation.
  - `hackr.png` – `git merge` vs `git merge --no-ff` article.
  - `stackoverflow.png` – fast‑forward vs no‑fast‑forward discussion.
  - `merging vs rebasing.png` – reference explaining merge vs rebase and reflog/reset usage.
- README structure and tone match previous daily reports (`2025-12-1`, `2025-11-28`, etc.) for consistency.

---

**Learning Progress:** Solid conceptual understanding of modern Git workflows, merge strategies, and Trunk‑Based Development trade‑offs. Ready to reinforce this theory with hands‑on Git practice in upcoming sessions. 🚀


