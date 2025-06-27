import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Create sample CSV data
csv_file = "sample_data.csv"
csv_data = [
    ["Name", "Age", "Department"],
    ["Akash", "20", "AI & DS"],
    ["Priya", "22", "CSE"],
    ["Ravi", "21", "EEE"],
    ["Meena", "23", "ECE"]
]

# Write to CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Read the data from CSV
def analyze_data(csv_file):
    data = []
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Generate PDF report
def generate_report(data, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 80, "Automated Report - Sample Data Analysis")

    c.setFont("Helvetica", 12)
    y = height - 120
    for index, row in enumerate(data):
        line = f"{index + 1}. Name: {row['Name']}, Age: {row['Age']}, Department: {row['Department']}"
        c.drawString(80, y, line)
        y -= 20
        if y < 100:
            c.showPage()
            y = height - 100
    c.save()

# Run the program
data = analyze_data(csv_file)
generate_report(data, "sample_report.pdf")
print("PDF report generated: sample_report.pdf")
