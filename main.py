from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
# p stands for portrait, l stands for land scape, unit is the dimension so mm in this case
pdf.set_auto_page_break(auto=False, margin=0)
# to have page not be broken automatically, which set to false
# as the footer was not aligned properly

df = pd.read_csv('topics (1).csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)  # time font, B = bold, size of 12
    pdf.set_text_color(100, 100, 100)

    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)  # this is a add a line below the topic name
    # add footer for page with title
    pdf.ln(265)  # this is the size of the break lines, 278 because A4 is around 297 height
    # which should fit nicely with 265, reduce accordingly if don't see the footer
    pdf.set_font(family='Times', style='B', size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)

    # if we want another font for another cell we need to have another set_font above the cell.
    for page in range(row['Pages'] - 1):
        pdf.add_page()
        # this is to add pages according to the pages in the csv
        # in range is used for the range numbers in the pages colum

        # add footers for other page with no titles
        pdf.ln(277)  # this is 265 +h=12 = 277, as this counts from top of the page

        # this is the size of the break lines, 278 because A4 is around 297 height
        # which should fit nicely with 265, reduce accordingly if you don't see the footer
        pdf.set_font(family='Times', style='B', size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)
        # align to the right.

pdf.output('output.pdf')

# w=width,if 0 means it extend to the end of the page, border if = 0 there is no border.
# h=height, it's near the size of the text itself in this case 12 which looks more neat
# align argument here we have L which means it align from left
# ln is line, if its 1 then the next cell will be in the next line
# if ln is 0 then it will be added after the width ends which looks like ghost print
# (R,G,B) depends on combination we get colors
