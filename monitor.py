import time    
from log_parser import parse_log_line     

def monitor_log(log_file):
    """
    Opens a log file and watches it forever.
    Every time a new line appears it passes it to the parser.
    """
    print(f"[MONITOR] Watching {log_file} for SSH activity...\n")

    with open(log_file, "r") as f:
        f.seek(0) #Starts from tge beginning of the file      

        while True: #this loops forever 

            line = f.readline()   #attempts to read the next line if available 
            if line:
                result = parse_log_line(line)
                if result:
                    print(f"[{result['status']}] "
                          f"IP: {result['ip']} | "
                          f"User: {result['username']} | "
                          f"Time: {result['timestamp']}")
            else:
                time.sleep(0.5)
    
         
