# SSH Brute Force Detector

A Python-based security tool that monitors SSH authentication logs in real time, 
detects brute force attack patterns, and simulates automated firewall responses. 
Built to demonstrate log parsing, threat detection, and automated incident response 
concepts used in production security systems.

---

## Features

- Real-time SSH log file monitoring
- Pattern recognition for failed and invalid login attempts
- Brute force detection using a configurable time window and threshold
- IP whitelist and blacklist management
- Simulated firewall blocking with iptables command output
- Persistent attack logging and audit trail
- Escalating response — detect, alert, block

---

## How It Works

The tool watches an SSH auth log file continuously. Every time a new line appears 
it is parsed for relevant events. Failed and invalid login attempts are tracked per 
IP address over a sliding time window. If an IP exceeds the configured threshold 
it is flagged as a brute force attacker, logged, and a simulated firewall block is issued.

Whitelisted IPs are ignored entirely. Blacklisted IPs are flagged and blocked immediately 
on first appearance.

---
## Project Structure 
ssh-brute-force detector
├── main.py           ← entry point
├── monitor.py        ← real-time log file watcher
├── log_parser.py     ← SSH log line parser
├── detector.py       ← brute force detection engine
├── firewall.py       ← simulated firewall response
├── alerts.py         ← attack logging and alerts
├── config.py         ← configurable settings
├── whitelist.txt     ← trusted IP addresses
├── blacklist.txt     ← known bad IP addresses
├── logs/
│   └── auth.log      ← sample SSH auth log
└── data/
├── attack_log.txt    ← persistent attack records
└── blocked_ips.txt   ← record of blocked IPs

---

## Configuration

Edit `config.py` to adjust detection sensitivity:

```python
THRESHOLD = 5      # number of failures before flagging as attack
TIME_WINDOW = 600  # time window in seconds (600 = 10 minutes)
```

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/DiegoQuito21/ssh-brute-force-detector.git
cd ssh-brute-force-detector

# Set up virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install rich watchdog

# Run the detector
python main.py
```

---

## Sample Output

[MONITOR] Watching logs/auth.log for SSH activity...
[FAILED] IP: 45.33.32.156 | User: root | Time: Apr  6 14:20:01
[FAILED] IP: 45.33.32.156 | User: root | Time: Apr  6 14:20:03
[FAILED] IP: 45.33.32.156 | User: admin | Time: Apr  6 14:20:05
[INVALID] IP: 45.33.32.156 | User: test | Time: Apr  6 14:20:07
[FAILED] IP: 45.33.32.156 | User: root | Time: Apr  6 14:20:09
[ALERT] BRUTE FORCE ATTACK DETECTED from 45.33.32.156 
[FIREWALL] Blocking 45.33.32.156
[FIREWALL] Simulated command: iptables -A INPUT -s 45.33.32.156 -j DROP
[BLACKLIST] Known bad IP detected: 78.12.44.91
[FIREWALL] Blocking 78.12.44.91
[FIREWALL] Simulated command: iptables -A INPUT -s 78.12.44.91 -j DROP

---

## Key Concepts Demonstrated

- Log file parsing and regex pattern matching
- Real-time file monitoring with continuous polling
- Sliding time window threat detection
- IP reputation management with whitelist and blacklist
- Simulated firewall integration and automated response
- Persistent logging and audit trails
- Producer-consumer style architecture

---

## Future Improvements

- Email and Slack alerting
- Real iptables integration on Linux
- Web dashboard for live monitoring
- Database storage for attack records
- Machine learning based anomaly detection

---

## Status

Complete — built as a portfolio project demonstrating cybersecurity tooling and Python systems programming.
