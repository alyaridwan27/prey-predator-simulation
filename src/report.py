import pandas as pd
from fpdf import FPDF

def save_results(t, prey, predator, filename="results.csv"):
    data = pd.DataFrame({"Time": t, "Prey": prey, "Predator": predator})
    data.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def generate_report(alpha, beta, delta, gamma, prey0, predator0, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Lotka-Volterra Simulation Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(0, 10, f"Alpha: {alpha}, Beta: {beta}, Delta: {delta}, Gamma: {gamma}", ln=True)
    pdf.cell(0, 10, f"Initial Prey: {prey0}, Initial Predator: {predator0}", ln=True)
    pdf.output(filename)
    print(f"Report saved to {filename}")
