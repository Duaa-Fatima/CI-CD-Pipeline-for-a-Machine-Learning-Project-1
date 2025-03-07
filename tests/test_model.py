import sys
import os

# Add the app folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app import app  # ✅ Import Flask app

def test_home_route():
    """Test if the home page loads successfully."""
    test_client = app.test_client()
    response = test_client.get('/')
    assert response.status_code == 200, "Home route is not working!"

def test_prediction():
    """Test if prediction works correctly with valid data."""
    test_client = app.test_client()
    
    data = {
        "Pregnancies": "2",
        "Glucose": "120",
        "BloodPressure": "70",
        "SkinThickness": "25",
        "Insulin": "100",
        "BMI": "28.5",
        "DiabetesPedigreeFunction": "0.5",
        "Age": "40"
    }

    response = test_client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200, "Prediction request failed!"
