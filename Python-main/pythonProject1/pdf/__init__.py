from PyPDF2 import PdfReader

import pyap

reader = PdfReader('C:/Users/CA-SHUBHAMKANDEKAR/Downloads/Elior C8144 MT panel.pdf', 'rb')

page = reader.pages[0]

text = page.extract_text()

addresses = pyap.parse(text, country='US')

for address in addresses:
    print(address.as_dict())
