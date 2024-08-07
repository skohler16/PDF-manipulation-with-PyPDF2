import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)


# from PyPDF2 import PdfWriter, PdfReader
#
# reader = PdfReader("dummy.pdf")
# writer = PdfWriter()
#
#
# writer.add_page(reader.pages[0])
# writer.pages[0].rotate(90)
#
# with open("dummy90.pdf", "wb") as fp:
#     writer.write(fp)