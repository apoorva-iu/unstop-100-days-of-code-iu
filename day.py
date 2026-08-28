import os
import re

day = int(input("Enter day number: "))
problems = int(input("How many questions today? "))

folder = f"Day{day:02d}"

os.makedirs(folder, exist_ok=True)

for i in range(1, problems + 1):

    question_name = input(f"Enter name of question {i}: ")

    # Make the name suitable for a filename
    filename = re.sub(r'[^a-zA-Z0-9 ]', '', question_name)
    filename = filename.replace(' ', '_')

    filepath = os.path.join(folder, filename + ".py")

    # Create the file
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write(
                f"# Unstop 100 Days of Code\n"
                f"# Day {day}\n"
                f"# {question_name}\n\n"
            )

print()
print(f"{folder} created successfully!")
print(f"{problems} question files created.")