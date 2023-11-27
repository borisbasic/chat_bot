import PyPDF2

pdf = open('tech_with_tim_chat\Petar Janjatovic - Ex Yu Rock Enciklopedija_text.pdf', 'rb')

pdf_read = PyPDF2.PdfReader(pdf)

first_page = pdf_read.pages[0]
for page in pdf_read.pages:
    print(page.extract_text())
    with open('rock.txt', 'a', encoding='utf-8') as f:
        f.write(page.extract_text())