import sys
import os
import joblib
from utils import extract_features

ROOT = os.path.join(os.path.dirname(__file__), "..")
MODEL_PATH = os.path.join(ROOT, "model", "url_phish_dt.pkl")

# Load trained model
data = joblib.load(MODEL_PATH)
model = data["model"]
cols = data["columns"]

# Check input
if len(sys.argv) < 2:
    print("Usage:")
    print("  python src/predict_url.py \"<url_here>\"")
    print("\nExample:")
    print("  python src/predict_url.py \"http://paypal.verify-login.com/confirm\"")
    sys.exit()

url = sys.argv[1]

# Extract features
feats = extract_features(url)
X = [[feats[col] for col in cols]]

# Predict
pred = model.predict(X)[0]
proba = model.predict_proba(X)[0]

print("\nURL:", url)
print("Prediction:", pred)
print("Confidence:", max(proba))
print("\nExtracted Features:", feats)
