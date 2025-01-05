import unittest
from src.simulation import lotka_volterra_model

class TestSimulation(unittest.TestCase):
    def test_lotka_volterra_model(self):
        # Test with simple parameters
        params = {
            "alpha": 0.1,
            "beta": 0.02,
            "delta": 0.01,
            "gamma": 0.1,
            "prey0": 40,
            "predator0": 9
        }
        t_max = 10
        steps = 100
        t, results = lotka_volterra_model(params, t_max, steps)
        
        # Check output dimensions
        self.assertEqual(len(t), steps)
        self.assertEqual(results.shape, (steps, 2))  # Two columns: prey, predator

        # Ensure populations remain non-negative
        self.assertTrue((results >= 0).all())

if __name__ == "__main__":
    unittest.main()
