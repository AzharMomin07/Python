import re
import PyPDF2


def extract_information(pdf_file: str, patterns: dict) -> dict:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        extracted_data = {}

        for pattern_name, pattern in patterns.items():
            regex = re.compile(pattern, re.DOTALL)
            extracted_data[pattern_name] = set()

            for text in pdf_text:
                matches = regex.findall(text)
                extracted_data[pattern_name].update(matches)

        return extracted_data


if __name__ == '__main__':
    patterns = {
        'primary_care_providers': r'Primary Care Provider\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)|$(.*?)\n',
        'clinics': r'Clinic\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n',
        'acute_care_facilities': r'Acute Care Facility\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n',

    }

    extracted_data = extract_information('C:/Users/CA-SHUBHAMKANDEKAR/Downloads/Elior C8144 MT panel.pdf', patterns)

    for pattern_name, data in extracted_data.items():
        print(f'{pattern_name}:')
        for item in data:
            print(item)
        print()
