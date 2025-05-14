from datetime import datetime

with open("daily.txt", "w") as file:
    file.write(f"Updated on {datetime.utcnow().isoformat()} UTC\n")