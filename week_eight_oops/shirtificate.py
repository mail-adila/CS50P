#  In a file called shirtificate.py, implement a program that prompts the user for their name
#  and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to
# this one for John Harvard, with these specifications:
#
# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.
# All other details we leave to you. You’re even welcome to add borders, colors, and lines.
# Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across
# multiple lines.
#
# Before writing any code, do read through fpdf2’s tutorial to learn how to use it.
# Then skim fpdf2’s API (application programming interface) to see all of its functions and
# parameters therefor.
#
# Hints
# Note that fpdf2 comes with a class called FPDF, which has quite a few methods, per
# py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF. You can install it with:
# pip install fpdf2
# Note that you can extend FPDF and instantiate your own subclass thereof in order to add a header
# to every page of a PDF, per py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image.
# Or you can add it as text yourself.
# Note that you can disable automatic page breaks, which might otherwise cause your PDF to overflow
# from one page to two, with set_auto_page_break, per py-pdf.github.io/fpdf2/Margins.html.
# Note that a cell’s height can be negative, to move it upward.
# You can open shirtificate.pdf, once outputted, by clicking it in VS Code’s file explorer.
from fpdf import fpdf, FPDF


def main():
    name = get_name()
    create_shirtificate(name)

def get_name():
    n = input("Enter your name: ")
    return n

def create_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.set_font("helvetica", style="B", size=16)
    pdf.cell(pdf.epw, 15, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.image(
        "shirtificate.png", 0, 30, 210)
    pdf.set_text_color(255, 255, 255)  # white
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_y(150)  # position vertically on the shirt
    pdf.cell(pdf.epw, 10, name + " took CS50", align='C')
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()