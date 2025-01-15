import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from src.backend import simulate_lotka_volterra
from src.visualization import plot_combined_dynamics
from config import DEFAULT_PARAMETERS

PARAMETER_DESCRIPTIONS = {
    "alpha": "Prey birth rate: Higher values increase prey growth.",
    "beta": "Predation rate: Higher values increase prey loss to predators.",
    "delta": "Predator reproduction rate: Higher values increase predator growth based on prey.",
    "gamma": "Predator death rate: Higher values increase predator decline over time.",
    "prey0": "Initial prey population: The starting population of prey.",
    "predator0": "Initial predator population: The starting population of predators."
}


class LotkaVolterraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lotka-Volterra Simulation")
        self.root.configure(bg="#f7f7f7")

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 700
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Title
        tk.Label(
            root,
            text="Lotka-Volterra Simulation",
            font=("Arial", 16, "bold"),
            bg="#f7f7f7",
            fg="#333",
        ).grid(row=0, column=0, columnspan=3, pady=10)

        # Sliders for parameters
        self.sliders = {}
        row = 1
        for param, default in DEFAULT_PARAMETERS.items():
            tk.Label(root, text=f"{param}:", bg="#f7f7f7", fg="#333").grid(row=row, column=0, padx=10, sticky="w")
            slider = tk.Scale(
                root, from_=0, to=default * 2, resolution=0.01, orient=tk.HORIZONTAL, bg="#f7f7f7", fg="#333"
            )
            slider.set(default)
            slider.grid(row=row, column=1, sticky="ew", padx=10)
            self.sliders[param] = slider

            # Add descriptions for each parameter
            description = PARAMETER_DESCRIPTIONS.get(param, "No description available.")
            tk.Label(root, text=description, wraplength=200, bg="#f7f7f7", fg="#555").grid(row=row, column=2, sticky="w")
            row += 1

        # Custom time range and steps
        tk.Label(root, text="t_max:", bg="#f7f7f7", fg="#333").grid(row=row, column=0, padx=10, sticky="w")
        self.t_max_entry = tk.Entry(root)
        self.t_max_entry.insert(0, "200")
        self.t_max_entry.grid(row=row, column=1, padx=10, sticky="w")
        row += 1

        tk.Label(root, text="Steps:", bg="#f7f7f7", fg="#333").grid(row=row, column=0, padx=10, sticky="w")
        self.steps_entry = tk.Entry(root)
        self.steps_entry.insert(0, "1000")
        self.steps_entry.grid(row=row, column=1, padx=10, sticky="w")
        row += 1

        # Run button
        self.run_button = tk.Button(
            root, text="Run Simulation", command=self.run_simulation, bg="#0078D7", fg="white", font=("Arial", 12, "bold")
        )
        self.run_button.grid(row=row, column=0, columnspan=3, pady=20, ipadx=10, ipady=5)
        row += 1

        # Error display area
        self.error_label = tk.Label(root, text="", fg="red", bg="#f7f7f7", font=("Arial", 10, "italic"))
        self.error_label.grid(row=row, column=0, columnspan=3, pady=5)

        # Metrics display area
        self.metrics_label = tk.Label(root, text="", fg="green", bg="#f7f7f7", font=("Arial", 10, "italic"))
        self.metrics_label.grid(row=row + 1, column=0, columnspan=3, pady=5)

    def run_simulation(self):
        try:
            # Get slider values as parameters
            params = {key: slider.get() for key, slider in self.sliders.items()}
            t_max = float(self.t_max_entry.get())
            steps = int(self.steps_entry.get())

            # Run the simulation
            t, result = simulate_lotka_volterra(**params, t_max=t_max, steps=steps)
            prey, predator = result.T

            # Calculate metrics
            max_prey = prey.max()
            max_predator = predator.max()
            extinction_time = (
                t[(prey <= 0) | (predator <= 0)][0]
                if any(prey <= 0) or any(predator <= 0)
                else "None"
            )

            # Update error and metrics display
            if extinction_time != "None":
                self.error_label.config(text=f"Warning: Extinction occurred at t={extinction_time:.2f}")
            else:
                self.error_label.config(text="")

            self.metrics_label.config(
                text=f"Max Prey: {max_prey:.2f}, Max Predator: {max_predator:.2f}, Extinction Time: {extinction_time}"
            )

            # Update the combined plot
            title = (
                f"Predator-Prey Dynamics\n"
                f"(alpha={params['alpha']}, beta={params['beta']}, delta={params['delta']}, gamma={params['gamma']}, "
                f"prey0={params['prey0']}, predator0={params['predator0']}, t_max={t_max}, steps={steps})"
            )
            plot_combined_dynamics(t, prey, predator, title)

        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all inputs are valid numerical values.")



