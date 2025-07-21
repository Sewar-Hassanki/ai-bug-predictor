import os
import pandas as pd

buggy_folder = "C:/Users/sewar/OneDrive/Documents/GitHub/ai-bug-predictor/data/buggy"
clean_folder = "C:/Users/sewar/OneDrive/Documents/GitHub/ai-bug-predictor/data/clean"


data = []

# Loop through both folders
for filename in os.listdir(buggy_folder):
    buggy_path = os.path.join(buggy_folder, filename)
    clean_path = os.path.join(clean_folder, filename.replace("buggy", "clean"))

    # Check if matching clean file exists
    if os.path.exists(clean_path):
        with open(buggy_path, "r", encoding="utf-8") as f_buggy, open(clean_path, "r", encoding="utf-8") as f_clean:
            buggy_code = f_buggy.read()
            clean_code = f_clean.read()
            data.append({"buggy_code": buggy_code, "clean_code": clean_code})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)
print("✅ dataset.csv created!")
