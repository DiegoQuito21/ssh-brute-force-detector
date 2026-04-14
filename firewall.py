blocked_ips = set()

def block_ip(ip):
    if ip in blocked_ips:
        print(f"[FIREWALL] {ip} is already blocked")
        return 
    blocked_ips.add(ip)
    print (f"[FIREWALL] Blocking {ip}")
    print(f"[FIREWALL] Simulated command: iptables -A INPUT -s {ip} -j DROP")

    with open("data/blocked_ips.txt" , "a") as f:
        f.write(ip + "\n")
