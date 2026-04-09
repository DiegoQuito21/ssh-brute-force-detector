import time    
from detector import record_attempt, analyze_attempt, is_whitelisted , is_blacklisted
from log_parser import parse_log_line  



def monitor_log(log_file):
    """
    Opens a log file and watches it forever.
    Every time a new line appears it passes it to the parser.
    """
    print(f"[MONITOR] Watching {log_file} for SSH activity...\n")

    with open(log_file, "r") as f:
        f.seek(0)

        while True:
            line = f.readline()
            if line:
                result = parse_log_line(line)
                if result:
                    print(f"[{result['status']}] "
                    f"IP: {result['ip']} | "
                    f"User: {result['username']} | "
                    f"Time: {result['timestamp']}")
                    if is_whitelisted(result["ip"]):
                        continue                        

                    if is_blacklisted(result["ip"]):
                        print(f"[BLACKLIST] Known bad IP detected: {result['ip']}")
                        continue                         

                 
                    record_attempt(result["ip"], result["status"])
                    is_attack = analyze_attempt(result["ip"])
                    if is_attack:
                        print(f"[ALERT] BRUTE FORCE ATTACK DETECTED from {result['ip']}")
            else:
                time.sleep(0.5)