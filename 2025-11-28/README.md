<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • SSH Connectivity • Git Foundations</h3>

---

## 🎯 Objective Recap
- Bring two Ubuntu 22.04 Live Server VMs online (`vm1`, `vm2`) dedicated to SSH testing.
- Validate host-only networking, bidirectional SSH, and secure file transfers.
- Capture proof for every milestone and store it under `images/`.
- Kick off the new Git learning track assigned for the week.

---

## 🛠️ Lab Topology
- **Host:** Windows 11 + MobaXterm client.
- **Hypervisor:** VirtualBox with host-only adapters for isolation.
- **Guests:** `vm1` and `vm2`, both running Ubuntu 22.04 (Live Server).
- **Tooling:** `openssh-server`, `scp`, and temporary `/tmp` mounts for file sharing.

![VM naming convention](images/made%202%20vm%20with%20ubuntu%20live%20server%20with%20proper%20naming%20convention%20as%20vm1%20and%20vm2.png)

---

## 🔐 SSH Connectivity Lab

### 1. Network Reachability
- Enabled host-only adapters, then validated connectivity with reciprocal `ping` tests to ensure both VMs share the same isolated subnet.

![Testing host-only network](images/enabled%20the%20host%20network%20setting%20and%20pinging%20both%20vm%20from%20each%20other%20to%20varify%20that%20they%20are%20on%20the%20same%20host%20network%20.png)

### 2. SSH Daemon Hardening
- Installed `openssh-server` on both nodes and confirmed services start automatically so remote access survives reboots.

![Enabling SSH server](images/enabling%20ssh%20server%20on%20both%20the%20vm%20ubuntu%20live%20server%20.png)

### 3. Host → VM Onboarding
- Built a dedicated session profile in MobaXterm for `vm1`, validated host fingerprints, and stored credentials securely for reuse.

![MobaXterm profile for vm1](images/made%20ssh%20connection%20for%20vm1%20using%20the%20mobaxtrem%20setup.png)

### 4. VM1 → VM2 Jump-Host Flow
- From the established `vm1` session, initiated a nested SSH session to `vm2` to simulate production-style bastion workflows.

![Nested SSH initiation](images/getting%20remote%20accessed%20of%20vm2%20from%20vm1%20in%20the%20mobaxtrem%20terminal%20.png)

![Session established on vm2](images/accessed%20the%20vm2%20ubuntu%20server%20form%20the%20remote%20accessed%20vm1%20using%20the%20mobaxtrem%20terminal%20%20ssh%20connection%20asstablished%20.png)

### 5. Terminal Validation
- Executed commands inside the chained shell to prove interactive control of `vm2` purely through SSH.

![Terminal proof](images/getting%20started%20with%20git%20using%20the%20wasp%20terminal.png)

### 6. Cross-VM File Sharing
- Mounted the `/tmp` directory from `vm2` onto `vm1` to keep the exchange transient yet auditable.

![Temporary share mount](images/shearing%20teh%20vm2%20home%20directory%20with%20the%20vm1%20at%20teh%20tmp%20directory%20.png)

### 7. Persistent Sync via `scp`
- Ran recursive `scp` copies from `vm2` → `vm1` to migrate lab artifacts and confirmed checksums post-transfer.

![Recursive scp transfer](images/using%20scp%20command%20to%20shear%20the%20folder%20of%20vm2%20with%20vm1%20permanentely%20recursively.png)

---

## 🆕 New Task – Git Practice Rollout
- Stand up Git repos on both Windows (PowerShell) and Ubuntu so every README update is versioned with semantic commit messages.
- Align `user.name`, `user.email`, and SSH key usage across environments to keep audit logs consistent.
- Prepare a short comparison of host vs. guest Git workflows for the upcoming sync.

---

## 📚 Git Learning Notes (YouTube Series)
Source: [Git Series Chapter Playlist](https://www.youtube.com/watch?v=zTjRZNkhiEU)

| Timestamp | Chapter | Deep Dive Notes |
|-----------|---------|-----------------|
| ⌨️ 0:00:00 | Introduction | Revisited Git’s distributed design, why snapshots beat diffs, and the trio of working tree → index → local repo. |
| ⌨️ 0:05:54 | `git init` & `.git` | Practiced initializing repos, explored `HEAD`, `config`, `objects/`, `refs/`, and stressed picking the correct root directory before running `git init`. |
| ⌨️ 0:23:27 | Commits & Logs | Focused on staging discipline, meaningful commit messages, `git log --oneline`, `git show`, and how chained SHA hashes enable safe `reset`/`revert`. |
| ⌨️ 0:40:02 | Internals & Config | Broke down blobs/trees/commits, edited `.git/config` vs. `~/.gitconfig`, and practiced `git config --global` to prep identities ahead of remote collaboration. |

---

## ✅ Evidence Checklist
- Every screenshot referenced above is stored in `2025-11-28/images/` with the exact filenames used in the captions.
- Lab steps can be replayed by following this README top to bottom.

---

**Next Review Window:** Ready for feedback on the SSH workflow or additional Git modules to prioritize next.

