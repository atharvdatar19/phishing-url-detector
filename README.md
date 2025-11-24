Phishing URL Detection Using Machine Learning

This project is a small, machine-learning-based tool that can classify URLs as either legitimate or phishing. The main idea was to understand how simple URL patterns can be used to detect suspicious links. The project is made using Python and is completely beginner-friendly.

About the Project

Phishing attacks often use fake websites that look similar to trusted ones. Since many fake links follow certain patterns, I created a small dataset of URLs and trained a Decision Tree classifier to identify whether a given URL looks safe or suspicious.

This project was made to teach:

How to extract features from URLs

How to create a simple dataset

How to train a basic ML model

How to test the model on new URLs

Folder Structure

text
phishing-url-detector/
│
├── data/
│   └── urls.csv              # Synthetic dataset of URLs
│
├── src/
│   ├── generate_dataset.py   # Creates dataset
│   ├── utils.py              # Feature extraction
│   ├── train_model.py        # Trains Decision Tree model
│   └── predict_url.py        # Predicts if a URL is phishing
│
├── model/
│   └── url_phish_dt.pkl      # Saved trained model
│
├── report/
│   └── report.md             # Project report
│
└── requirements.txt
How to Run the Project

Install dependencies

bash
pip install -r requirements.txt
Generate the dataset

bash
python src/generate_dataset.py
This will create a fresh urls.csv file inside the data folder.

Train the model

bash
python src/train_model.py
This trains the Decision Tree model and saves it in the model folder.

Test a URL

To check a URL:

bash
python src/predict_url.py "<your_url_here>"
Example:

bash
python src/predict_url.py "http://paypal.verify-login.xyz/confirm"
Output will show:

phishing or legitimate

model confidence score

URL feature details

Features Used in the Model

The project does not use any advanced NLP techniques. It only uses simple, logical features such as:

Length of the URL

Number of dots .

Number of slashes /

Keyword count (like "login", "verify", "paypal", etc.)

Whether HTTPS is used

Length of the domain part

Count of @, -, =, ? symbols

These features were chosen because they are easy to understand and implement.

Model Used

A Decision Tree Classifier was used because it is:

Easy to visualize

Beginner-friendly

Works well with small datasets

Does not require complex preprocessing

The model achieved high accuracy on the small dataset.

Why This Project?

I made this project to get hands-on experience with:

Python

Pandas

Scikit-Learn

Basic cybersecurity concepts

Feature engineering

It is not designed to replace professional phishing detection systems, but to understand how ML approaches work on simple problems.

Future Improvements

Some ideas for future improvements:

Use large, real phishing datasets

Add more URL features

Test other algorithms, like Random Forest

Add domain age, SSL info, WHOIS data

Create a small web app or browser extension



