import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.feature_extraction import extract_features
import joblib

# Load dataset
data = pd.read_csv("phishing_urls_500.csv")  # should have 'url' and 'label' columns

# Feature extraction
data['features'] = data['url'].apply(extract_features)
X = list(data['features'])
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(clf, "model/phishing_model.pkl")
