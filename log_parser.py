import re

def parse_log_line(line):
    """
    Takes a single SSH log line and extracts useful information.
    Returns a dictionary with the parsed data, or None if not relevant.
    """

    failed_pattern = re.compile(
        r'(\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+)'
    )

    invalid_pattern = re.compile(
        r'(\w+\s+\d+\s+\d+:\d+:\d+).*Invalid user (\S+) from (\d+\.\d+\.\d+\.\d+)'
    )

    success_pattern = re.compile(
        r'(\w+\s+\d+\s+\d+:\d+:\d+).*Accepted password for (\S+) from (\d+\.\d+\.\d+\.\d+)'
    )

    for pattern, status in [
        (failed_pattern, "FAILED"),
        (invalid_pattern, "INVALID"),
        (success_pattern, "SUCCESS")
    ]:
        match = pattern.search(line)
        if match:
            return {
                "timestamp": match.group(1),
                "username": match.group(2),
                "ip": match.group(3),
                "status": status,
                "raw": line.strip()
            }

    return None