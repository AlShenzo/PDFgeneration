from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
# p stands for portrait, l stands for land scape, unit is the dimension so mm in this case

df = pd.read_csv('topics (1).csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)  # time font, B = bold, size of 12
    pdf.set_text_color(100, 100, 100)

    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)  # this is a add a line below the topic name

    # if we want another font for another cell we need to have another set_font above the cell.
pdf.output('output.pdf')

# w=width,if 0 means it extend to the end of the page, border if = 0 there is no border.
# h=height, it's near the size of the text itself in this case 12 which looks more neat
# align argument here we have L which means it align from left
# ln is line, if its 1 then the next cell will be in the next line
# if ln is 0 then it will be added after the width ends which looks like ghost print
# (R,G,B) depends on combination we get colors
