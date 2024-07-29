import os
import subprocess
from datetime import datetime, timedelta

# Define the pattern of your graffiti
# This is a 7x7 grid where '1' represents a commit and '0' represents no commit
pattern = [
    "0110000",
    "0101000",
    "0101000",
    "0110000",
    "0101000",
    "0100100",
    "0100010",
]

start_date = datetime(2023, 1, 1)  # Start date of your graffiti

for i, row in enumerate(pattern):
    for j, val in enumerate(row):
        if val == '1':
            date = start_date + timedelta(days=i*7 + j)
            date_str = date.strftime("%Y-%m-%d")
            with open("graffiti.txt", "a") as file:
                file.write(f"Commit for {date_str}\n")
            subprocess.run(["git", "add", "graffiti.txt"])
            subprocess.run(["git", "commit", "--date", f"{date_str} 12:00:00", "-m", f"Commit for {date_str}"])
