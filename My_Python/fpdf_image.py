from fpdf import FPDF
import urllib
pdf = FPDF()
img_url="https://sfmayor.org/sites/default/files/seal-of-the-city-of-san-francisco_1.jpg"
urllib. request. urlretrieve(img_url, "C:\\Users\\sdasyapu\\Desktop\\new_image.jpg")

pdf.add_page()
pdf.image("C:\\Users\\sdasyapu\\Desktop\\new_image.jpg",
          x = 7, y = 7, w = 25, h = 25, type = '', link = '')
pdf.output("C:\\Users\\sdasyapu\\Desktop\\new_image.pdf", 'F')