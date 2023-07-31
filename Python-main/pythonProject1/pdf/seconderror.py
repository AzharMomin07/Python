# import re
#
# import pdf
# from PyPDF2 import PdfReader
#
# import pandas as pd
#
# # Set display options to show all columns
# pd.set_option('display.max_columns', None)
#
# reader = PdfReader('C:/Users/CA-SHUBHAMKANDEKAR/Downloads/Elior C8144 MT panel.pdf', 'rb')
# page = reader.pages[0]
# text = page.extract_text()
#
# # Define regular expressions to extract provider information
# provider_re = pdf.PdfReader(r'^(.*?\n.*?)\n(.+)\n(.+)\n(.+)\n\((\d{3})\) (\d{3}-\d{4})\n(.+)$', re.MULTILINE)
#
# # Find all provider matches in the text
# providers = provider_re.findall(text)
#
#
# # Print the extracted provider information
# for provider in providers:
#     clinic_name, provider_name, provider_type, address, phone_area_code, phone_number, distance = provider
#     name = f'{clinic_name.strip()} - {provider_name.strip()}'
#     print(f'Provider Name: {name}')
#     print(f'Provider Type: {provider_type}')
#     print(f'Address: {address}')
#     print(f'Phone Number: ({phone_area_code}) {phone_number}')
#     print(f'Estimated Distance: {distance}\n')

import re
import PyPDF2


def extract_primary_care_providers(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

    providers = []
    pattern = r'Primary Care Provider\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n'
    regex = re.compile(pattern, re.DOTALL)

    for text in pdf_text:
        matches = regex.findall(text)
        providers.extend(matches)

    return providers


if __name__ == '__main__':
    extracted_providers = extract_primary_care_providers('C:/Users/CA-SHUBHAMKANDEKAR/Downloads/Elior C8144 MT panel.pdf')
    for provider in extracted_providers:
        print(provider)
