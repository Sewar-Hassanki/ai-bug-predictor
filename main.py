# main.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 👩‍💻 Sample dummy data for now
# Pretend this is code + whether it's buggy (1 = buggy, 0 = clean)
data = {
    "code": [
        "for i in range(10): print(i)",               # clean
        "if x = 5 print('hello')",                    # buggy
        "def add(x, y): return x + y",               # clean
        "while True print('loop')",                  # buggy
        "print('hello world')",                      # clean
        "if (x == 5) { console.log('yes'); }",       # clean
        "if x == 5 print('yes')",                    # buggy
        "def divide(a, b): return a / b",            # clean
        "def bad_func() print('oops')",              # buggy
        "for i in range(10) print(i)",               # buggy
    ],
    "is_bug": [0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
}


df = pd.DataFrame(data)

# Step 2: Convert code into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['code'])
y = df['is_bug']

# Step 3: Train a basic model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
preds = model.predict(X_test)
print("Predictions:", preds)
print(classification_report(y_test, preds))
