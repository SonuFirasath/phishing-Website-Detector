import re
import urllib
from urllib.parse import urlparse

def extract_features(url):
    features = []
    
    parsed = urlparse(url)
    hostname = parsed.netloc
    path = parsed.path

    # Feature 1: Length of URL
    features.append(len(url))

    # Feature 2: Presence of '@'
    features.append(1 if '@' in url else 0)

    # Feature 3: Presence of '-'
    features.append(1 if '-' in hostname else 0)

    # Feature 4: Count of subdomains
    features.append(len(hostname.split('.')))

    # Feature 5: Use of HTTPS
    features.append(1 if parsed.scheme == 'https' else 0)

    # Feature 6: Presence of IP address
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    features.append(1 if ip_pattern.search(hostname) else 0)

    # Feature 7: Presence of suspicious keywords
    suspicious_keywords = ['secure', 'account', 'update', 'login', 'free', 'bank', 'verify']
    features.append(any(keyword in url.lower() for keyword in suspicious_keywords))

    return features
