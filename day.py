import os

day = int(input("Enter day number: "))
problems = int(input("How many problems today? "))

folder = f"Day{day:02d}"

os.makedirs(folder, exist_ok=True)

for i in range(1, problems + 1):

    filename = f"Problem{i:02d}.py"
    filepath = os.path.join(folder, filename)

    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write(
                f"# Unstop 100 Days of Code\n"
                f"# Day {day}\n"
                f"# Problem {i}\n\n"
            )

print(f"\n{folder} created successfully!")
print(f"{problems} problem files created.")