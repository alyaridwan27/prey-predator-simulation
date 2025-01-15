import numpy as np
from scipy.integrate import odeint


# Lotka-Volterra equations
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    prey, predator = y
    dydt = [
        alpha * prey - beta * prey * predator,
        delta * prey * predator - gamma * predator,
    ]
    return dydt


# Simulation function
def simulate_lotka_volterra(alpha, beta, delta, gamma, prey0, predator0, t_max=200, steps=1000):
    """
    Simulates the Lotka-Volterra predator-prey model.
    
    Parameters:
        alpha (float): Prey birth rate.
        beta (float): Predation rate.
        delta (float): Predator reproduction rate.
        gamma (float): Predator death rate.
        prey0 (float): Initial prey population.
        predator0 (float): Initial predator population.
        t_max (float): Total simulation time.
        steps (int): Number of time steps.
        
    Returns:
        t (ndarray): Time array.
        result (ndarray): Solution array with prey and predator populations.
    """
    t = np.linspace(0, t_max, steps)
    y0 = [prey0, predator0]
    result = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
    return t, result


# Metrics calculation
def calculate_metrics(t, result):
    """
    Calculates key metrics for the simulation.
    
    Parameters:
        t (ndarray): Time array.
        result (ndarray): Solution array with prey and predator populations.
        
    Returns:
        dict: Metrics including max prey, max predator, and extinction time.
    """
    prey, predator = result.T
    max_prey = prey.max()
    max_predator = predator.max()

    # Find extinction time if any population goes to zero
    extinction_time = (
        t[np.where((prey <= 0) | (predator <= 0))[0][0]]
        if np.any(prey <= 0) or np.any(predator <= 0)
        else None
    )

    return {
        "max_prey": max_prey,
        "max_predator": max_predator,
        "extinction_time": extinction_time,
    }
