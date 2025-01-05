import unittest
from src.backend import lotka_volterra

class TestLotkaVolterra(unittest.TestCase):
    def test_lotka_volterra(self):
        y = [40, 9]
        t = 0
        alpha, beta, delta, gamma = 0.1, 0.02, 0.01, 0.1
        dydt = lotka_volterra(y, t, alpha, beta, delta, gamma)
        self.assertEqual(len(dydt), 2)
