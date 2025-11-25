<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#00a86b;">Daily DevOps Practice • Linux Foundations • Virtualization</h3>

---

## 🎧 Study Log – Linux Essentials Chapters 7 → 12

I continued the **Linux Essentials** series on YouTube and covered six more chapters from the same long-form session ([video link](https://youtu.be/sWbUDq4S6Y8?si=2AMM6e4UC_pnplaA)). Today’s focus areas:

- ⌨️ 2:12:57 – **Chapter 7: Command Line Operations** – reinforced terminal navigation, `su` vs `sudo -i`, and why `pushd/popd` can accelerate directory hopping on headless servers.
- ⌨️ 3:25:50 – **Chapter 8: Finding Linux Documentation** – walked through `man`, `man -f`, `man page# topic`, and when `whatis` is faster than combing through PDF guides.
- ⌨️ 3:36:53 – **Chapter 9: Processes** – reviewed `ps`, `top`, `kill -9 <pid>`, `renice`, and the implications of priority tuning when sharing compute in labs.
- ⌨️ 4:07:51 – **Chapter 10: File Operations** – refreshed `ln`, `ln -s`, timestamps via `touch -t`, and recursive search helpers (`find`, `locate`, `updatedb`) before applying them in the VM.
- ⌨️ 4:31:11 – **Chapter 11: Text Editors** – compared quick edits in `nano` versus modal workflows in `vi`, noting which to reach for when documenting lab steps.
- ⌨️ 4:49:25 – **Chapter 12: User Environment** – practiced `echo $HOME`, shell variables, and session switching with `Ctrl+Alt+Fn` to stay productive even after dropping to a TTY.

---

## 🖥️ Virtualization & Ubuntu Desktop Trial

I spun up a fresh Ubuntu VM inside VirtualBox to complement the ongoing Amazon Linux 2 work. Key steps:

1. **ISO prep & VM creation** – attached the Ubuntu ISO, allocated disks, and documented each wizard screen for repeatability.  
   ![Creating the Ubuntu VM](images/making%20a%20new%20linux%20on%20a%20vm%20with%20ubuntu%20iso%20image%20.png)

2. **Boot validation** – tracked the boot loader and splash screens so I can confirm kernel progress if the VM ever hangs.  
   ![Ubuntu boot sequence](images/ubuntu%20being%20loading%20.png)

3. **Desktop walkthrough** – once the installer landed on the GNOME desktop, I captured the UI layout to map where system settings and terminal shortcuts live.  
   ![Ubuntu desktop UI](images/ui%20of%20ubuntu.png)

The Ubuntu VM supplements the Amazon Linux 2 CLI-only environment; having a GUI reference point helps when translating documentation screenshots into equivalent terminal instructions.

---

## 🧪 Amazon Linux 2 CLI Practice & Command Journal

All of today’s terminal drills are logged verbatim in `commands that i learned.txt` so I can re-run any sequence later. Highlights:

- **Privilege & session control** – toggled between `sudo -i`, `su`, and virtual terminals (`Ctrl+Alt+F{1-6}`) to understand how each impacts environment variables and `$HOME`.
- **Navigation fluency** – alternated between absolute (`cd /usr/bin`) and relative (`cd ../../usr/bin`) paths while monitoring context with `pwd`, `pushd`, and `popd`.  
  ![Practicing cd with absolute and relative paths](images/practcing%20the%20directory%20changing%20commands%20with%20absolute%20and%20relative%20paths%20.png)

- **Filesystem inspection** – compared bare `ls`, `ls -a`, `ls -li`, and `tree` (where available) to see how metadata changes after each exercise.  
  ![Listing /bin contents](images/listing%20the%20contents%20of%20bin%20fonder.png)

- **Link experiments** – created hard links with `ln` and symbolic links with `ln -s`, then verified inode reuse versus unique IDs.  
  ![Hard link lab](images/testing%20the%20concept%20of%20hard%20link%20.png)  
  ![Soft link lab](images/testing%20the%20concept%20of%20soft%20link%20.png)

- **Text processing** – rehearsed `cat`, `cat -n`, `less -N`, `head`, `tail`, `tac`, `wc`, `diff`, and `diff3` to cover the exam objectives for text comparisons.

- **Search & metadata** – used `which`, `whereis`, `find -name`, `find -type d`, `find -ctime`, `find -size`, `find -newer`, plus `locate`/`updatedb` to trace binaries and spot empty files.  
  ![General command drills](images/testing%20the%20different%20linux%20command%20teh%20general%20ones%20.png)

- **Cleanup routines** – practiced `rm`, `rm -f`, `rm -i`, `rm -rf`, and `rmdir`, reinforcing the safety differences before touching production-like directories.  
  ![Removal command practice](images/testing%20the%20different%20removing%20commands%20.png)

- **Process & scheduling tools** – ran `sleep`, `shutdown -h/-r`, timed shutdown messages, and `kill -9` scenarios to see how Amazon Linux 2 responds before/after switching runlevels (`sudo telinit 3` vs `sudo systemctl stop gdm`).

- **Mounting & disk checks** – reviewed `sudo mount /path1/file /path2`, `du`, and `find -exec` combos to automate follow-up actions (e.g., delete stray `.exe` files).

The screenshot set above maps directly to many of these steps and provides a visual audit trail for later review.

---

## 🗂️ Reference Assets & Next Steps

- `commands that i learned.txt` – canonical list of every command run today (rooted in the Amazon Linux 2 VM); use it as a replay script for future labs.
- `images/` – nine screenshots catalogued in this README to show Ubuntu provisioning, CLI drills, and filesystem experiments.

Next session I will:

1. Re-run the same commands inside Ubuntu’s terminal to compare package manager differences (`dnf` vs `apt`).
2. Document VirtualBox shared clipboard tweaks so that copying complex `find -exec` syntax from Windows is less error-prone.

---

## 📚 References

- Linux Essentials Chapters 7–12 video timestamps noted above ([YouTube](https://youtu.be/sWbUDq4S6Y8?si=2AMM6e4UC_pnplaA)).

