from docx2pdf import convert
def convert(company):
    company = 'Abaris'
    convert(company+'.docx')
    convert(company+'.docx',company+'1'+'.pdf')

