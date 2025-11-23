import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
from utils import extract_features

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_PATH = os.path.join(ROOT, "data", "urls.csv")
MODEL_DIR = os.path.join(ROOT, "model")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "url_phish_dt.pkl")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Extract features for each row
feature_rows = []
labels = []

for _, row in df.iterrows():
    feats = extract_features(row["url"])
    feature_rows.append(feats)
    labels.append(row["label"])

X = pd.DataFrame(feature_rows)
y = pd.Series(labels)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Decision Tree model (simple & student-friendly)
clf = DecisionTreeClassifier(max_depth=6, random_state=42)
clf.fit(X_train, y_train)

# Save model + column order
joblib.dump({
    "model": clf,
    "columns": X.columns.tolist()
}, MODEL_PATH)

print(f"Model saved at: {MODEL_PATH}")

# Print accuracy
print("Training accuracy:", clf.score(X_train, y_train))
print("Testing accuracy:", clf.score(X_test, y_test))
