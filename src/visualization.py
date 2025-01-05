import plotly.graph_objects as go

def plot_population_dynamics(t, prey, predator):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=prey, mode='lines', name='Prey'))
    fig.add_trace(go.Scatter(x=t, y=predator, mode='lines', name='Predator'))
    fig.update_layout(
        title="Predator-Prey Dynamics",
        xaxis_title="Time",
        yaxis_title="Population",
        legend_title="Species"
    )
    fig.show()

def plot_phase_plane(prey, predator):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prey, y=predator, mode='lines', name='Phase Plane'))
    fig.update_layout(
        title="Phase Plane: Prey vs Predator",
        xaxis_title="Prey Population",
        yaxis_title="Predator Population",
    )
    fig.show()
