from fpdf import FPDF

def create_sample_cv():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add CV content
    pdf.cell(200, 10, txt="John Doe", ln=1, align='C')
    pdf.cell(200, 10, txt="Machine Learning Engineer", ln=1, align='C')
    pdf.cell(200, 10, txt="john.doe@email.com | (123) 456-7890", ln=1, align='C')
    
    # Education
    pdf.cell(200, 10, txt="Education", ln=1, align='L')
    pdf.cell(200, 10, txt="BS in Computer Science - Stanford University", ln=1, align='L')
    
    # Skills
    pdf.cell(200, 10, txt="Skills", ln=1, align='L')
    pdf.cell(200, 10, txt="Python, TensorFlow, PyTorch, Machine Learning, Deep Learning", ln=1, align='L')
    
    # Save the pdf
    pdf.output("cv_04_24.pdf")

if __name__ == "__main__":
    create_sample_cv() 