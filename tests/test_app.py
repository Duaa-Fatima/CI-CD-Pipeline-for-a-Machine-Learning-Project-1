import unittest
from app import app  # ✅ Import Flask app correctly

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        """Set up test client before running tests"""
        self.app = app.test_client()  # ✅ Ensure app has `test_client()`
        self.app.testing = True  # Enable testing mode

    def test_home(self):
        """Test if the home page loads successfully"""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        """Test prediction API"""
        sample_data = {
            "Pregnancies": 5, "Glucose": 116, "BloodPressure": 74,
            "SkinThickness": 0, "Insulin": 0, "BMI": 25.6,
            "DiabetesPedigreeFunction": 0.201, "Age": 30
        }
        response = self.app.post("/", data=sample_data)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
