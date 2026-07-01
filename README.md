<p align="center">
  <img src="https://raw.githubusercontent.com/retr0hck3r/retr0hck3r/main/header.svg" alt="retr0hck3r header" width="100%" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/retr0hck3r/retr0hck3r/main/crt_banner.svg" alt="retr0hck3r terminal banner" width="100%" />
</p>

```text
retr0@white-server:~$ cat /etc/motd
================================================================================
██████╗ ███████╗████████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██╔══██╗██╔════╝
██████╔╝█████╗     ██║   ██████╔╝██║   ██║██╔██╗ ██║██║   ██║██║  ██║█████╗  
██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║██║   ██║██║  ██║██╔══╝  
██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝
================================================================================
 * System:      Linux white-server 6.1.0-rt-amd64
 * Status:      Fully automated & secure
 * Kernel:      x86_64 GNU/Linux
 * Terminal:    ttyS001 (monochrome CRT green #00FF99)
 * Alert:       No vulnerabilities found. Annoying, but responsible.
================================================================================

retr0@white-server:~$ uptime
<!-- START_UPTIME -->
 19:03:16 up 47 days, 07:03,  1 user,  load average: 0.11, 0.14, 0.43
<!-- END_UPTIME -->

retr0@white-server:~$ systemctl status system-load.service
● system-load.service - Resource Monitor
     Loaded: loaded (/etc/systemd/system/system-load.service; enabled)
     Active: active (running) since Wed 2026-05-15 12:00:00 UTC
<!-- START_SYSTEM_LOAD -->
cpu_load: [██░░░░░░░░░░░░░░░░░░] 14%
ram_load: [█████████████░░░░░░░] 69%
<!-- END_SYSTEM_LOAD -->

retr0@white-server:~$ cat /sys/devices/system/skills.status
============================ SKILL MODULES ============================
OFFENSIVE   [██████████████████░░] 90%  (BurpSuite, Nmap, Exploits, Web)
DEFENSIVE   [████████████░░░░░░░░] 60%  (Suricata, Wireshark, SIEM, Logs)
AUTOMATION  [████████████████░░░░] 80%  (Python, Go, Bash, Docker, Git)
RESEARCH    [██████████████░░░░░░] 70%  (CTF Reverse/Pwn, 0-day Tracking)
=======================================================================

retr0@white-server:~$ cat /var/log/active_ops.json
<!-- START_OPS -->
{
  "PID_8043": {
    "process": "subdomain-scanner-go",
    "status": "optimizing_concurrency",
    "progress": "85%"
  },
  "PID_2210": {
    "process": "preparation-osep-cert",
    "status": "active_study",
    "progress": "50%"
  },
  "PID_1337": {
    "process": "ctf-competition-engagement",
    "status": "solving_reverse_pwn",
    "progress": "running"
  }
}
<!-- END_OPS -->

retr0@white-server:~$ systemctl status motivation.service
● motivation.service - Motivation Daemon
     Loaded: loaded (/etc/systemd/system/motivation.service; enabled)
     Active: failed (Result: core-dump) since Wed 2026-07-01 18:00:21 MSK
     Status: "Failed to establish meaningful dopamine loop."

retr0@white-server:~$ ping -c 1 reality
PING reality (127.0.0.1) 56(84) bytes of data.
Request timed out (100% packet loss).
```

```bash
retr0@white-server:~$ query-analytics --github
```

<p align="left">
  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img src="https://github-readme-stats.vercel.app/api?username=retr0hck3r&show_icons=true&title_color=00FF99&icon_color=00FF99&text_color=a0a0a0&bg_color=0d1117&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats" height="180px" />
  </a>
  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=retr0hck3r&layout=compact&title_color=00FF99&icon_color=00FF99&text_color=a0a0a0&bg_color=0d1117&hide_border=true&langs_count=6" alt="Top Languages" height="180px" />
  </a>
</p>

<br clear="both" />

<details>
  <summary>🔑 retr0@white-server:~$ gpg --decrypt contacts.asc.gpg</summary>
  <br />
  <pre>
gpg: encrypted with 4096-bit RSA key, ID FAD1337BEEF, created 2026-07-01
      "retr0 &lt;retr0@example.com&gt;"
gpg: Signature made Wed Jul  1 18:00:00 2026 MSK
gpg:                using RSA key FAD1337BEEF
gpg: Good signature from "retr0 &lt;retr0@example.com&gt;"

=============================================
--- DECRYPTED CONTACT INFO ---
=============================================
Telegram:   https://t.me/retr0_sec
Keybase:    https://keybase.io/retr0_sec
E-mail:     retr0@example.com
=============================================

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: OpenPGP.js v4.10.2

mQINBF2Wv...
[INSERT YOUR PUBLIC PGP KEY HERE]
-----END PGP PUBLIC KEY BLOCK-----
  </pre>
</details>

<br />

```bash
retr0@white-server:~$ fortune | cowsay
```

```text
 _________________________________________
/ Security is not a product, but a        \
\ process. - Bruce Schneier               /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
