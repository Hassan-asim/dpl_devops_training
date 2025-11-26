<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#00a86b;">Daily DevOps Practice • Linux Foundations • Networking</h3>

---

## 🎧 Study Log – Linux Essentials Chapters 12 → 14

I continued the **Linux Essentials** series on YouTube and covered three more chapters. Today's focus areas:

- ⌨️ 4:49:25 – **Chapter 12: User Environment** – practiced keyboard shortcuts for shell navigation, learned `Ctrl-L`, `Ctrl-D`, `Ctrl-Z`, `Ctrl-C`, and other essential shortcuts for efficient terminal usage.
- ⌨️ 5:13:32 – **Chapter 13: Manipulating Text** – deep dive into text processing tools including `cat`, `sed`, `awk`, `grep`, `sort`, `uniq`, `paste`, `join`, `split`, `tr`, `tee`, `wc`, and `cut`.
- ⌨️ 5:40:04 – **Chapter 14: Network Operations** – explored network configuration, IP addressing, and attempted SSH connections between VMs.

---

## 🖥️ Practical Lab Work

### Multi-VM Command Practice

I practiced commands across both Amazon Linux 2 and Ubuntu VMs simultaneously, keeping logs of all commands in a text file for future reference.

![Practicing Linux Commands](images/practicing%20the%20linux%20commands%20from%20the%20yt%20video%20in%20both%20amazon%20linux%202%20and%20ubuntu%20,%20and%20keeping%20the%20logs%20of%20the%20commands%20ina%20txt%20file%20.png)

### Ubuntu Terminal & Networking Practice

Practiced Linux commands on Ubuntu while learning networking concepts specific to the Linux environment.

![Practicing on Ubuntu](images/practicing%20the%20linux%20command%20on%20ubuntu%20and%20also%20learning%20the%20networking%20stuff%20on%20linux%20ubuntu%20.png)

---

## 🌐 Network Operations Lab

### Learning Network Information Extraction

Studied different methods to extract network information, referencing documentation from linuxfoundation.org.

![Network Info](images/learning%20different%20ways%20to%20extract%20network%20info%20from%20linuxfoundation.org.png)

### VM IP Configuration

Accessed the IP addresses of both Ubuntu and Amazon Linux VMs to practice remote file copying operations.

![Accessing IPs](images/accessing%20the%20ip%20of%20both%20ubuntu%20ans%20anmazin%20linux%20to%20practice%20remote%20coping%20of%20file.png)

### Host IP Discovery

Searched for the current host user IP information to understand network configuration.

![Host IP Info](images/searching%20for%20the%20current%20host%20user%20ip%20info.png)

### Network Host Scanning

Attempted to discover other hosts on the network – currently none available.

![Searching Hosts](images/searching%20for%20more%20host%20on%20the%20network%20%20currently%20i%20have%20none%20.png)

### SSH Connection Attempt

Tried connecting both VMs using SSH but encountered issues that need further troubleshooting.

![SSH Attempt](images/tried%20connecting%20the%20both%20vm%20using%20ssh%20but%20for%20some%20reasdon%20was%20unable%20too%20.png)

---

## 🧪 Command Journal – 65 Commands Learned

All of today's terminal drills are logged verbatim in `commands I learned.txt`. Highlights by category:

### Keyboard Shortcuts (User Environment)
- `Ctrl-L` (clear screen), `Ctrl-D` (exit shell), `Ctrl-Z` (suspend process), `Ctrl-C` (kill process)
- `Ctrl-H` (backspace), `Ctrl-A` (beginning of line), `Ctrl-E` (end of line)
- `Ctrl-W` (delete word), `Ctrl-U` (delete to beginning), `Tab` (auto-complete)

### File Ownership & Permissions
- `chown`, `chgrp`, `chmod` – ownership and permission management
- Octal permission system (r=4, w=2, x=1) for `chmod 777 filename` style commands

### Text Display & Navigation
- `cat`, `cat -n`, `less`, `head -n`, `tail -n` – file viewing and pagination
- `cat file1 file2 > newfile` – file concatenation and redirection

### Stream Editing with sed
- `sed s/old/new/` – first occurrence substitution
- `sed s/old/new/g` – global substitution
- `sed -i` – in-place editing
- `sed 1,3s/old/new/g` – range-based substitution

### Field Processing with awk
- `awk '{ print $0 }'` – print entire file
- `awk -F: '{ print $1 }'` – field extraction with custom delimiter

### Sorting & Filtering
- `sort`, `sort -r`, `sort -k`, `sort -u` – various sorting operations
- `uniq -c` – duplicate counting

### File Operations
- `paste`, `join`, `split` – file merging and splitting
- `cut -d" " -f3` – column extraction

### Pattern Matching with grep
- `grep [pattern]`, `grep -v`, `grep -C` – pattern searching with context
- `grep [0-9]` – numeric pattern matching

### Text Transformation with tr
- `tr a-z A-Z` – case conversion
- `tr -s`, `tr -d`, `tr -c` – squeeze, delete, complement operations

### Utility Commands
- `tee` – save output while displaying
- `wc -l/-c/-w` – line/byte/word counting

---

## 🗂️ Reference Assets & Next Steps

- `commands I learned.txt` – canonical list of all 65 commands learned today with descriptions.
- `images/` – seven screenshots documenting networking practice and multi-VM work.

Next session I will:

1. Troubleshoot the SSH connection issue between VMs.
2. Practice remote file operations (`scp`, `rsync`) once connectivity is established.
3. Continue with remaining Linux Essentials chapters.

---

## 📚 References

- Linux Essentials Chapters 12–14 video timestamps noted above.

