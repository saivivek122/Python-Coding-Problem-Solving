from fpdf import FPDF
import urllib

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", 'B', size=12)
pdf.set_text_color(0, 0, 0)

pdf.set_font("Times",'B' ,size=10)
pdf.set_text_color(0,0,0)
epw = pdf.w - 2 * pdf.l_margin
col_width = epw / 4
# img_url="https://sfmayor.org/sites/default/files/seal-of-the-city-of-san-francisco_1.jpg"
# urllib. request. urlretrieve(img_url, 'C:\\Users\\sdasyapu\\Desktop\\image.jpg')
data = [(1000.0, 1, 'Candidate', 'F'), (964.0, 2, 'Candidate', 'C'), (964.0, 2, 'Candidate', 'I'), (906.0, 3, 'Candidate', 'H'), (876.0, 4, 'Candidate', 'B'), (795.0, 5, 'Candidate', 'E'), (744.0, 6, 'Candidate', 'A'),
(705.0, 7, 'Candidate', 'G'), (703.0, 8, 'Candidate', 'D'), (702.0, 9, 'Candidate', 'K'), (700.0, 10, 'Candidate', 'J'),
(1000.0, 1, 'Candidate', 'F'), (964.0, 2, 'Candidate', 'C'), (964.0, 2, 'Candidate', 'I'), (906.0, 3, 'Candidate', 'H'), (876.0, 4, 'Candidate', 'B'), (795.0, 5, 'Candidate', 'E'), (744.0, 6, 'Candidate', 'A'),
(705.0, 7, 'Candidate', 'G'), (703.0, 8, 'Candidate', 'D'), (702.0, 9, 'Candidate', 'K'), (700.0, 10, 'Candidate', 'J'),
(1000.0, 1, 'Candidate', 'F'), (964.0, 2, 'Candidate', 'C'), (964.0, 2, 'Candidate', 'I'), (906.0, 3, 'Candidate', 'H'), (876.0, 4, 'Candidate', 'B'), (795.0, 5, 'Candidate', 'E'), (744.0, 6, 'Candidate', 'A'),
(705.0, 7, 'Candidate', 'G'), (703.0, 8, 'Candidate', 'D'), (702.0, 9, 'Candidate', 'K'), (700.0, 10, 'Candidate', 'J'),
(1000.0, 1, 'Candidate', 'F'), (964.0, 2, 'Candidate', 'C'), (964.0, 2, 'Candidate', 'I'), (906.0, 3, 'Candidate', 'H'), (876.0, 4, 'Candidate', 'B'), (795.0, 5, 'Candidate', 'E'), (744.0, 6, 'Candidate', 'A'),
(705.0, 7, 'Candidate', 'G'), (703.0, 8, 'Candidate', 'D'), (702.0, 9, 'Candidate', 'K'), (700.0, 10, 'Candidate', 'J'),
(1000.0, 1, 'Candidate', 'F'), (964.0, 2, 'Candidate', 'C'), (964.0, 2, 'Candidate', 'I'), (906.0, 3, 'Candidate', 'H'), (876.0, 4, 'Candidate', 'B'), (795.0, 5, 'Candidate', 'E'), (744.0, 6, 'Candidate', 'A'),
(705.0, 7, 'Candidate', 'G'), (703.0, 8, 'Candidate', 'D'), (702.0, 9, 'Candidate', 'K'), (700.0, 10, 'Candidate', 'J')]
pdf.set_font('Times', 'B', 14.0)
pdf.cell(epw, 0.0, align='C')
pdf.set_font('Times', '', 10.0)
pdf.ln(0.5)
th = pdf.font_size
#pdf.image('C:\\Users\\sdasyapu\\Desktop\\image.jpg',x = 7, y = 7, w = 20, h = 20, type = '', link = '')
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, th, str(datum))

    pdf.ln(2 * th)
#pdf.image('C:\\Users\\sdasyapu\\Desktop\\image.jpg',x = 7, y = 7, w = 20, h = 20, type = '', link = '')


pdf.output("C:\\Users\\sdasyapu\\Desktop\\vashist.pdf", 'F')