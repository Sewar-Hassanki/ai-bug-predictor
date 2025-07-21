import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("dataset.csv")

# Combine buggy and clean code into one column
df_combined = pd.DataFrame({
    "code": df["buggy_code"].tolist() + df["clean_code"].tolist(),
    "is_bug": [1] * len(df) + [0] * len(df)
})

# Vectorize the code
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df_combined["code"])
y = df_combined["is_bug"]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
