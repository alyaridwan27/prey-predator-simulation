import numpy as np

def extended_lotka_volterra_model(params, t_max, steps):
    # Extracting the parameters
    alpha = params['alpha']  # Prey growth rate
    beta = params['beta']    # Predator rate
    delta = params['delta']  # Predator growth rate due to predation
    gamma = params['gamma']  # Predator death rate
    mu = params['mu']        # Prey-competitor competition rate
    eta = params['eta']      # Competitor growth rate
    zeta = params['zeta']    # Predator rate on competitor

    # Initial populations
    prey0 = params['prey0']
    predator0 = params['predator0']
    competitor0 = params['competitor0']

    # Time setup
    t = np.linspace(0, t_max, steps)
    dt = t[1] - t[0]  # Time step

    # Initial population vector
    populations = np.array([prey0, predator0, competitor0])

    # Prepare array to store population data over time
    result = np.zeros((steps, 3))
    result[0] = populations

    # Run the simulation (Euler's method)
    for i in range(1, steps):
        prey, predator, competitor = populations

        # Differential equations
        dPdt = alpha * prey - beta * prey * predator - mu * prey * competitor
        dHdt = delta * prey * predator - gamma * predator
        dCdt = eta * competitor - zeta * predator * competitor

        # Update populations
        populations += np.array([dPdt, dHdt, dCdt]) * dt

        # Store results
        result[i] = populations

    return t, result
