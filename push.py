import subprocess
import os

# Ask which day you want to push
day = input("Enter day number: ")

# Create folder name
folder = f"Day{int(day):02d}"

# Check if folder exists
if not os.path.exists(folder):
    print(f"{folder} does not exist!")
    exit()

# Add ONLY that day's folder
subprocess.run(["git", "add", folder])

# Automatic commit message
message = f"Day {int(day):02d}: Completed"

# Commit
result = subprocess.run(["git", "commit", "-m", message])

# Push only if commit was successful
if result.returncode == 0:
    subprocess.run(["git", "push"])
    print(f"\n{message}")
    print("Successfully pushed to GitHub!")
else:
    print("\nNothing new to commit.")