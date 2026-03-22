import os
print("\n\n   ==================")
print("|| Python Log Analyzer ||")
print("   ==================\n")

file_path = os.path.join(os.path.dirname(__file__), "log.txt")

with open(file_path, "r") as file:
    logs = file.readlines()

for line in logs:
    print(line.strip())

failed_attempts = []

for line in logs:
    line = line.strip()
    
    if "failed" in line.lower():
        failed_attempts.append(line)

print("\n==== Failed Login Attempts ====\n")
for attempt in failed_attempts:
    print(attempt)

ip_count = {}

for line in logs:
    line = line.strip()

    if "failed" in line.lower():
        ip = line.split(" - ")[0]

        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1
print("\n Suspicious IPs (more than 2 failed attempts):")

found = False

for ip, count in ip_count.items():
    if count > 2:
        print(f"{ip} = {count} failed attempts")
        found = True

if not found:
    print("No suspicious activity detected.")