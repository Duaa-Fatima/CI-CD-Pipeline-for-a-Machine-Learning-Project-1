import unittest
import os
import pandas as pd
from model import load_model, train_model, MODEL_PATH  # ✅ Fix import (same directory)
from app import app  # ✅ Fix Flask import

class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Ensure the model is trained and loaded before running tests."""
        if not os.path.exists(MODEL_PATH):
            train_model()  # Train model if it doesn't exist
        cls.model = load_model()

    def test_model_file_exists(self):
        """Check if the trained model file exists."""
        self.assertTrue(os.path.exists(MODEL_PATH), "Model file not found!")

    def test_prediction_output(self):
        """Test if the model's prediction is a valid class (0 or 1)."""
        column_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
        
        sample_input = pd.DataFrame([[5, 116, 74, 0, 0, 25.6, 0.201, 30]], columns=column_names)
        prediction = self.model.predict(sample_input)[0]
        self.assertIn(prediction, [0, 1], "Prediction should be 0 or 1.")

    def test_model_loading(self):
        """Ensure the model loads properly without errors."""
        model = load_model()
        self.assertIsNotNone(model, "Model failed to load.")

if __name__ == "__main__":
    unittest.main()
