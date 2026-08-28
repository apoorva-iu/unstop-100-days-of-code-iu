import subprocess

# Ask for a commit message
message = input("Enter commit message: ")

# Add all changed files
subprocess.run(["git", "add", "."])

# Commit the changes
subprocess.run(["git", "commit", "-m", message])

# Push to GitHub
subprocess.run(["git", "push"])

print("\nSuccessfully pushed to GitHub!")