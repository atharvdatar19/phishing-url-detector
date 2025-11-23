from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure", "account", "update",
    "confirm", "password", "reset", "pay", "paypal",
    "bank", "verify-login", "security", "authenticate",
    "verification", "refund", "xyz", "confirm", "center"
]


def extract_features(url: str) -> dict:
    """
    Extract simple numeric features from a URL for ML model.
    Beginner-friendly feature set.
    """
    url = url.strip()
    parsed = urlparse(url)

    length = len(url)
    dot_count = url.count(".")
    slash_count = url.count("/")
    at_count = url.count("@")
    hyphen_count = url.count("-")
    eq_count = url.count("=")
    question_count = url.count("?")
    has_https = 1 if url.startswith("https://") else 0

    kw_count = sum(1 for kw in SUSPICIOUS_KEYWORDS if kw in url.lower())

    host = parsed.netloc if parsed.netloc else ""
    host_len = len(host)

    return {
        "length": length,
        "dot_count": dot_count,
        "slash_count": slash_count,
        "at_count": at_count,
        "hyphen_count": hyphen_count,
        "eq_count": eq_count,
        "question_count": question_count,
        "has_https": has_https,
        "kw_count": kw_count,
        "host_len": host_len
    }
