import PyPDF2

def pdf_f():
    pdf_file = open("prueba.pdf", "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        print(text)

    pdf_file.close()
