import unittest
import json
from app import app

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        sample_data = {
            "features": [5, 116, 74, 0, 0, 25.6, 0.201, 30]
        }
        response = self.app.post('/predict', json=sample_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json)

if __name__ == "__main__":
    unittest.main()
