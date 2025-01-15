import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot_combined_dynamics(t, prey, predator, title):
    """
    Plots the population dynamics (time series) and phase plane in a single window.
    
    Parameters:
        t (array): Time steps.
        prey (array): Prey population over time.
        predator (array): Predator population over time.
        title (str): Title for the combined plot.
    """
    fig = plt.figure(figsize=(12, 6))
    gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1], width_ratios=[1, 1])
    fig.suptitle(title, fontsize=16)

    # Time Dynamics Plot
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(t, prey, label="Prey (Time)", color="blue")
    ax1.plot(t, predator, label="Predator (Time)", color="red")
    ax1.set_title("Predator-Prey Dynamics")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Population")
    ax1.legend()

    # Phase Plane Plot
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(prey, predator, label="Phase Plane", color="green")
    ax2.set_title("Phase Plane")
    ax2.set_xlabel("Prey Population")
    ax2.set_ylabel("Predator Population")
    ax2.legend()

    # Descriptions
    ax3 = fig.add_subplot(gs[1, :])
    ax3.axis("off")
    description = (
        "The left graph shows the predator-prey population dynamics over time.\n"
        "- The blue line represents the prey population.\n"
        "- The red line represents the predator population.\n"
        "The right graph shows the phase plane trajectory:\n"
        "- The green curve illustrates the interaction between prey and predator populations.\n"
        "- It highlights the cyclical nature of their populations."
    )
    ax3.text(
        0.5,
        0.5,
        description,
        ha="center",
        va="center",
        fontsize=10,
        wrap=True,
        bbox=dict(boxstyle="round", edgecolor="gray", facecolor="lightyellow"),
    )

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
