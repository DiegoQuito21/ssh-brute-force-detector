from log_parser import parse_log_line
# Fake log lines to test the parser
test_lines = [
     "Apr  6 14:23:11 server sshd[1234]: Failed password for root from 192.168.1.10 port 22 ssh2",
    "Apr  6 14:24:05 server sshd[1234]: Invalid user admin from 45.33.32.156 port 22",
    "Apr  6 14:25:00 server sshd[1234]: Accepted password for diego from 192.168.1.10 port 22 ssh2",
    "Apr  6 14:26:00 server sshd[1234]: Some random log line we don't care about",
]

for line in test_lines:
    result = parse_log_line(line)
    if result:
        print(f"[{result['status']}] IP: {result['ip']} | User: {result['username']} | Time: {result['timestamp']}")
    else: 
        print("[IGNORED] Line not relevant")