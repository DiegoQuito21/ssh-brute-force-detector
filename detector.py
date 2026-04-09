from datetime import datetime
from config import THRESHOLD, TIME_WINDOW
whitelist = open("whitelist.txt", "r").read().splitlines()
blacklist = open("blacklist.txt", "r").read().splitlines()

attempt_history = {}
def is_whitelisted(ip):
     if ip in whitelist:
            return True
     else:
        return False


def is_blacklisted(ip):
     if ip in blacklist:
        return True
     else:
        return False




def record_attempt(ip, status):
    if status in ["FAILED", "INVALID"]:
        if ip not in attempt_history:
            attempt_history[ip] = []
        attempt_history[ip].append(datetime.now())

def analyze_attempt(ip):
    if ip not in attempt_history:
        return False
    count = 0 
    now = datetime.now()
    for attempt in attempt_history[ip]:
        age = (now - attempt).total_seconds()
        if age < TIME_WINDOW: 
            count += 1 
    if count >= THRESHOLD:
            return True
    else:
            return False
