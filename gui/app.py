import tkinter as tk
from tkinter import messagebox
from src.backend import simulate_lotka_volterra
from src.visualization import plot_population_dynamics
from config import DEFAULT_PARAMETERS

class LotkaVolterraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lotka-Volterra Simulation")

        # Input fields for parameters
        self.entries = {}
        for i, (param, default) in enumerate(DEFAULT_PARAMETERS.items()):
            tk.Label(root, text=f"{param}:").grid(row=i, column=0)
            entry = tk.Entry(root)
            entry.insert(0, str(default))
            entry.grid(row=i, column=1)
            self.entries[param] = entry

        # Run button
        tk.Button(root, text="Run Simulation", command=self.run_simulation).grid(row=len(DEFAULT_PARAMETERS), column=0, columnspan=2)

    def run_simulation(self):
        try:
            params = {key: float(entry.get()) for key, entry in self.entries.items()}
            t, result = simulate_lotka_volterra(**params)
            prey, predator = result.T
            plot_population_dynamics(t, prey, predator)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

