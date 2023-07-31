import re

from PyPDF2 import PdfReader

reader = PdfReader('C:/Users/CA-SHUBHAMKANDEKAR/Downloads/Elior C8144 MT panel.pdf')

# Define regular expression pattern

provider_re = re.compile(r'^(.*?)\n(.+)?\n(.*?)\n(.*?)\n\((\d{3})\) (\d{3}-\d{4})\nEstimated Distance: (.+)$',re.MULTILINE)

# Iterate over all pages in the PDF

for page in reader.pages:
    text = page.extract_text()
    providers = provider_re.findall(text)

    # Process the extracted provider information

    for provider in providers:
        clinic_name = provider[0].strip()

        provider_name = provider[1].strip() if provider[1] else ""

        provider_type = provider[2]

        address = provider[3]

        phone_area_code = provider[4]

        phone_number = provider[5]

        distance = provider[6]

        print(f'clinic Name: {clinic_name}')

        print(f'Provider Name: {provider_name}')

        print(f'Provider Type: {provider_type}')

        print(f'Address: {address}')

        print(f'Phone Number: ({phone_area_code}) {phone_number}')

        print(f'Estimated Distance: {distance}\n')
