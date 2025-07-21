import os

# Create the dataset folder
os.makedirs("data/buggy", exist_ok=True)
os.makedirs("data/clean", exist_ok=True)

# Sample buggy code
buggy_codes = [
    "def divide(a, b):\n    return a / b  # no check for b == 0",
    "for i in range(10)\n    print(i)",  # missing colon
    "print('Hello World'"  # missing closing parenthesis
]

# Sample clean code
clean_codes = [
    "def divide(a, b):\n    return a / b if b != 0 else None",
    "for i in range(10):\n    print(i)",
    "print('Hello World')"
]

# Save buggy code files
for idx, code in enumerate(buggy_codes):
    with open(f"data/buggy/buggy_{idx}.py", "w") as f:
        f.write(code)

# Save clean code files
for idx, code in enumerate(clean_codes):
    with open(f"data/clean/clean_{idx}.py", "w") as f:
        f.write(code)

print("✅ Dataset created: check the 'data/' folder!")
