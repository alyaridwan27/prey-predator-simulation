import matplotlib.pyplot as plt
import numpy as np
from src.simulation import extended_lotka_volterra_model

def plot_extended_scenario():
    # Define different parameter sets to test
    param_sets = [
        {"alpha": 0.1, "beta": 0.02, "delta": 0.01, "gamma": 0.1, "mu": 0.05, "eta": 0.1, "zeta": 0.05, "prey0": 40, "predator0": 9, "competitor0": 30},
        {"alpha": 0.2, "beta": 0.02, "delta": 0.01, "gamma": 0.1, "mu": 0.05, "eta": 0.1, "zeta": 0.05, "prey0": 40, "predator0": 9, "competitor0": 30}
    ]

    # Time and simulation setup
    t_max = 100
    steps = 1000
    t = np.linspace(0, t_max, steps)

    plt.figure(figsize=(12, 8))

    for params in param_sets:
        t, results = extended_lotka_volterra_model(params, t_max, steps)
        
        # Plot the results for prey, predator, and competitor populations
        plt.plot(t, results[:, 0], label=f"Prey: α={params['alpha']}, β={params['beta']}")
        plt.plot(t, results[:, 1], label=f"Predator: α={params['alpha']}, β={params['beta']}")
        plt.plot(t, results[:, 2], label=f"Competitor: α={params['alpha']}, β={params['beta']}")

    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.title("Predator-Prey-Competitor Dynamics")
    plt.legend()
    plt.grid(True)

    plt.show()
