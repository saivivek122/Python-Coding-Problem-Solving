from fpdf import FPDF
import urllib
pdf = FPDF()
img_url="https://sfmayor.org/sites/default/files/seal-of-the-city-of-san-francisco_1.jpg"
urllib. request. urlretrieve(img_url, "C:\\Users\\sdasyapu\\Desktop\\new_image.jpg")

# Add a page
pdf.add_page()
with open("C:\\Users\\sdasyapu\\Desktop\\new.pdf", 'wb'):


# set style and size of font
# that you want in the pdf
    pdf.set_font("Arial",'B' ,size=13)
    pdf.set_text_color(0,0,205)

    pdf.cell(200, 10, txt = "City and County of San Francisco Department of Human Resources", ln = 100, align = 'C')
    pdf.cell(200, 10, txt = "Eligible list", ln = 100, align = 'C')
    pdf.ln(2*10)
    pdf.set_font("Arial",'B' ,size=10)
    pdf.set_text_color(0,0,0)
    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 4

    # create a cell
    data2 = [70009,"Ruleof","6","Continuous CBT","4/3/2020","2/3/2021","Police"]
    print(data2[0])
    pdf.cell(40, 0, txt="list id: "+str(data2[0]),ln=1, align='C')
    pdf.cell(300, 0, txt="List Type: "+"continuous CBT",ln=2, align='C')
    pdf.ln(2)
    pdf.cell(110, 10, txt="Working Title:"+"Junior Process ",ln=3,align='C')
    pdf.cell(281, -10, txt="Post: "+"2/05/2021",ln=6,align='C')
    pdf.ln(2)
    pdf.cell(48, 20, txt="cert Rule: "+"Rule of 3",ln=4,align='C')
    pdf.cell(150, -20, txt="Adoption: "+"2/05/2021",ln=6,align='C')
    pdf.cell(285, 20, txt="Duration: "+"6 Monts",ln=7,align='C')
    pdf.ln(2)
    pdf.cell(55, -10, txt="Inspection Start:"+"2/05/2021",ln=4,align='C')
    pdf.cell(200, 10, txt="Inspection End:"+"2/05/2021",ln=4,align='C')
    pdf.cell(10,35,txt="First Name",align='C')
    pdf.cell(85,35,txt="Last Name",align='C')
    pdf.cell(10,35,txt="Rank",align='C')
    pdf.cell(85,35,txt="Last Name",align='C')
    pdf.ln(2 * 10)
    data = [
            ['Jules', 'Smith', 34, 'San Juan'],
            ['Mary', 'Ramos', 45, 'Orlando'], [
                'Carlson', 'Banks', 19, 'Los Angeles']
            ]
    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(epw, 0.0, align='C')
    pdf.set_font('Arial', '', 10.0)
    pdf.ln(0.5)
    th = pdf.font_size
    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, th, str(datum))

        pdf.ln(2 * th)
    pdf.image("C:\\Users\\sdasyapu\\Desktop\\new_image.jpg",
            x = 12, y = 12, w = 25, h = 25, type = '', link = '')
pdf.output("C:\\Users\\sdasyapu\\Desktop\\version2.pdf", 'F')
