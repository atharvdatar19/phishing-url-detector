import csv
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'urls.csv')

legit = [
    "https://www.google.com",
    "https://www.amazon.in",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://vitbhopal.ac.in",
    "https://github.com",
    "https://www.facebook.com",
    "https://docs.python.org",
    "https://stackoverflow.com",
    "https://www.linkedin.com"
]

phishing = [
    "http://paypal.verify-login.xyz/confirm",
    "http://paypal.account.verify-login.xyz",
    "http://secure-paypal-login.com/verify",
    "http://facebook.account-reset-login.co/verify",
    "http://google-login-security-check.site/confirm",
    "http://amazon.refund-center.xyz/verify",
    "http://bankofindia.secure-update-login.com",
    "http://secure-update-payments.com/login",
    "http://account-verification-security.com/reset",
    "http://verify-account-security.xyz/confirm",
]

rows = []
for u in legit:
    rows.append([u, "legitimate"])

for u in phishing:
    rows.append([u, "phishing"])

# Variations
for u in phishing:
    rows.append([u + "?id=1023", "phishing"])
    rows.append([u.replace("http://", "http://secure-"), "phishing"])
    rows.append([u.replace(".xyz", ".info"), "phishing"])

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["url", "label"])
    writer.writerows(rows)

print("Improved dataset saved:", file_path)
print("Total rows:", len(rows))
