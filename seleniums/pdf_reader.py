import PyPDF2
import pyttsx3

reader = PyPDF2.PdfReader(open('sf.pdf', 'rb'))
speaker = pyttsx3.init()

clean_text = ''

for page_num in range(reader.numPages):
    text = reader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'se.mp3')
speaker.runAndWait()

speaker.stop()