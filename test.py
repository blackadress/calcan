import fpdf

pdf = fpdf.FPDF()
pdf_width = 210
pdf_height = 297

pdf.add_page()
title = 'ASDF'

pdf.set_xy(0.0, 0.0)
pdf.set_font('Arial', 'B', 16)
pdf.cell(w=210.0, h=40.0, align='C', txt=title, border=0)

pdf.set_font('Arial', '', 13)

pdf.set_xy(20.0, 30.0)
pdf.cell(w=40.0, h=10.0, align='L', txt="asdf", border=1)
pdf.set_xy(60.0, 30.0)
pdf.cell(w=40.0, h=10.0, align='L', txt="asdf", border=1)

pdf.set_xy(110.0, 30.0)
pdf.cell(w=40.0, h=10.0, align='L', txt="asdf", border=1)
pdf.set_xy(150.0, 30.0)
pdf.cell(w=40.0, h=10.0, align='L', txt="asdf", border=1)

pdf.output('test.pdf', 'F')
