import PyPDF2

# Open the PDF file
with open('C:/Users/CA-SHUBHAMKANDEKAR/Downloads/Elior C8144 MT panel.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfFileReader(file)

    # Extract the text from each page
    addresses = []
    for page in range(reader.numPages):
        text = reader.getPage(page).extract_text()
        addresses.append(text.strip())

    # Print the addresses
    for address in addresses:
        print(address)
