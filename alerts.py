from datetime import datetime
def log_attack(ip, username , timestamp):
    log_entry = (
        f"[{datetime.now()}] ATTACK DETECTED | "
        f"IP: {ip} | "
        f"User: {username} | "
        f"First seen: {timestamp}\n"
    )
    print(f"[ALERT] {log_entry.strip()}")
    with open("data/attack_log.txt", "a") as f:
        f.write(log_entry)

        