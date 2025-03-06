import unittest
import numpy as np
from app.model import load_model

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = load_model()

    def test_prediction(self):
        sample_input = np.array([5, 116, 74, 0, 0, 25.6, 0.201, 30]).reshape(1, -1)
        prediction = self.model.predict(sample_input)[0]
        self.assertIn(prediction, [0, 1])

if __name__ == "__main__":
    unittest.main()
