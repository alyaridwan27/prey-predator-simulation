import numpy as np
from scipy.integrate import odeint

def lotka_volterra(y, t, alpha, beta, delta, gamma):
    prey, predator = y
    dydt = [
        alpha * prey - beta * prey * predator,
        delta * prey * predator - gamma * predator
    ]
    return dydt

def simulate_lotka_volterra(alpha, beta, delta, gamma, prey0, predator0, t_max=200, steps=1000):
    t = np.linspace(0, t_max, steps)
    y0 = [prey0, predator0]
    result = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
    return t, result
