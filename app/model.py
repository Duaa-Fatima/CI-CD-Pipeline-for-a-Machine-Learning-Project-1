import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# Get the absolute path of the current script
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root directory
MODEL_PATH = os.path.join(ROOT_DIR, "diabetes_model.pkl")  # Save in root
# Define paths
DATA_PATH = os.path.join(ROOT_DIR, "data", "diabetes.csv")  # Ensure correct path
def train_model():
    """Train and save the model."""
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["Outcome"])
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved!")
def load_model():
    """Load the trained model, retraining if necessary."""
    if not os.path.exists(MODEL_PATH):
        print("Model file not found, training model...")
        train_model()
    return joblib.load(MODEL_PATH)
