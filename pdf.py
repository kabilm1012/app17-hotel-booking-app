from fpdf import FPDF


def generate_pdf(name, hotel_name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt="Receipt nr.1", ln=1)
    pdf.cell(w=50, h=8, txt=f"Name: {name}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Hotel Name: {hotel_name}", ln=1)
    pdf.cell(w=50, h=8, txt="Thank you for your booking!", ln=1)

    pdf.output("receipt.pdf")
    print("PDF receipt generated successfully!")


if __name__ == "__main__":
    generate_pdf("Kabil", "Radisson")



