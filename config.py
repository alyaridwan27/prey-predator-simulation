DEFAULT_PARAMETERS = {
    "alpha": 0.1,        # Growth rate of prey
    "beta": 0.02,        # Rate of predation
    "delta": 0.01,       # Reproduction rate of predators per prey eaten
    "gamma": 0.1,        # Natural death rate of predators
    "prey0": 40,         # Initial prey population
    "predator0": 9       # Initial predator population
}

SIMULATION_SETTINGS = {
    "t_max": 200,  # Total simulation time
    "steps": 1000  # Number of time steps
}

FILE_PATHS = {
    "csv_output": "data/results.csv",  # Where to save CSV results
    "pdf_report": "data/report.pdf"   # Where to save the PDF report
}

VISUALIZATION_SETTINGS = {
    "prey_color": "blue",        # Color for prey population curve
    "predator_color": "red",     # Color for predator population curve
    "title_font_size": 16,       # Font size for plot titles
    "label_font_size": 12        # Font size for axis labels
}