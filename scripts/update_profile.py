import os
import sys
import json
import random
import urllib.request
from datetime import datetime

# Start of uptime tracking (stable system boot timestamp: May 15, 2026)
BOOT_TIME = datetime(2026, 5, 15, 12, 0, 0)

def get_github_username():
    # 1. Check GITHUB_REPOSITORY (owner/repo)
    github_repo = os.environ.get('GITHUB_REPOSITORY')
    if github_repo and '/' in github_repo:
        return github_repo.split('/')[0]
    
    # 2. Check GITHUB_ACTOR (the user who triggered the run)
    github_actor = os.environ.get('GITHUB_ACTOR')
    if github_actor:
        return github_actor
        
    return "retr0hck3r"  # default fallback

def fetch_active_ops(username):
    # Fetch user public events
    url = f"https://api.github.com/users/{username}/events/public"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AntigravityIDE/1.0')
    
    # Use GitHub Actions token if available to avoid rate limit issues
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('INPUT_GITHUB_TOKEN')
    if token:
        req.add_header('Authorization', f'token {token}')
        
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            events = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching GitHub events: {e}", file=sys.stderr)
        return get_fallback_ops()
        
    push_events = [e for e in events if e.get('type') == 'PushEvent']
    if not push_events:
        return get_fallback_ops()
        
    ops = {}
    seen_repos = set()
    pid_counter = 8043
    
    for event in push_events:
        repo_name = event.get('repo', {}).get('name', '').split('/')[-1]
        if not repo_name or repo_name in seen_repos:
            continue
            
        commits = event.get('payload', {}).get('commits', [])
        if not commits:
            continue
            
        commit_msg = commits[0].get('message', 'Active coding session').split('\n')[0]
        
        # Calculate a stable progress percentage based on repository name character codes
        repo_hash = sum(ord(c) for c in repo_name)
        progress = f"{50 + (repo_hash % 46)}%"  # between 50% and 95%
        
        status = commit_msg
        if len(status) > 40:
            status = status[:37] + "..."
            
        pid = f"PID_{pid_counter}"
        ops[pid] = {
            "process": repo_name,
            "status": status,
            "progress": progress
        }
        
        seen_repos.add(repo_name)
        pid_counter += 127  # increment to simulate distinct PIDs
        if len(ops) >= 3:
            break
            
    # If we couldn't find 3 active repos, fill in the rest with fallback ops
    if len(ops) < 3:
        fallbacks = get_fallback_ops()
        for pid, data in fallbacks.items():
            if len(ops) >= 3:
                break
            if pid not in ops and data["process"] not in [o["process"] for o in ops.values()]:
                ops[pid] = data
                
    return ops

def get_fallback_ops():
    return {
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

def get_uptime_string():
    now = datetime.utcnow()
    delta = now - BOOT_TIME
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    current_time_str = now.strftime("%H:%M:%S")
    
    h = hash(f"{now.hour}:{now.minute}")
    l1 = 0.05 + ((h % 15) / 100.0)
    l2 = 0.10 + (((h + 3) % 25) / 100.0)
    l3 = 0.20 + (((h + 7) % 40) / 100.0)
    
    load_avg = f"{l1:.2f}, {l2:.2f}, {l3:.2f}"
    
    return f" {current_time_str} up {days} days, {hours:02d}:{minutes:02d},  1 user,  load average: {load_avg}"

def get_system_load_string():
    cpu = random.randint(12, 85)
    ram = random.randint(30, 72)
    
    def draw_bar(pct, width=20):
        filled = int((pct / 100) * width)
        return "[" + "█" * filled + "░" * (width - filled) + f"] {pct}%"
        
    return f"cpu_load: {draw_bar(cpu)}\nram_load: {draw_bar(ram)}"

def update_file(filepath, uptime_str, ops_json, load_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Uptime
    start_uptime_tag = "<!-- START_UPTIME -->"
    end_uptime_tag = "<!-- END_UPTIME -->"
    
    if start_uptime_tag in content and end_uptime_tag in content:
        before = content.split(start_uptime_tag)[0]
        after = content.split(end_uptime_tag)[1]
        content = f"{before}{start_uptime_tag}\n{uptime_str}\n{end_uptime_tag}{after}"
        
    # Replace Active Ops
    start_ops_tag = "<!-- START_OPS -->"
    end_ops_tag = "<!-- END_OPS -->"
    
    if start_ops_tag in content and end_ops_tag in content:
        before = content.split(start_ops_tag)[0]
        after = content.split(end_ops_tag)[1]
        ops_str = json.dumps(ops_json, indent=2)
        content = f"{before}{start_ops_tag}\n{ops_str}\n{end_ops_tag}{after}"

    # Replace System Load
    start_load_tag = "<!-- START_SYSTEM_LOAD -->"
    end_load_tag = "<!-- END_SYSTEM_LOAD -->"
    
    if start_load_tag in content and end_load_tag in content:
        before = content.split(start_load_tag)[0]
        after = content.split(end_load_tag)[1]
        content = f"{before}{start_load_tag}\n{load_str}\n{end_load_tag}{after}"
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("README.md updated successfully.")

def main():
    username = get_github_username()
    print(f"Target GitHub username: {username}")
    
    uptime_str = get_uptime_string()
    ops_json = fetch_active_ops(username)
    load_str = get_system_load_string()
    
    # Locate README.md in parent directory of the script or locally
    readme_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")
    if not os.path.exists(readme_path):
        readme_path = "README.md"
        
    update_file(readme_path, uptime_str, ops_json, load_str)

if __name__ == "__main__":
    main()
