import docx
import PyPDF2
import sys

def getText(filename):
    split = filename.split('.')
    filetype = split[-1] #recocnizing text file type, pdf, docx or txt
    if filetype == 'docx': #actions with docx
        print('Working with docx...')
        try: #in case there is no such file in directory
            doc = docx.Document(filename)
            fullText = []
            text = ''
            for para in doc.paragraphs:
                fullText.append(para.text)
            for i in range(len(fullText)):
                text += ' ' + fullText[i]
            text = text.split() #formatting text for analys
            howlong = len(set(text)) #finding out the length of the text
            return set(text), howlong
        except Exception:
            return 'Something wrong with files', 'Error'
    if filetype == 'pdf':
        print('Working with pdf...')
        try:
            with open(filename, 'rb') as f:
                pdf = PyPDF2.PdfFileReader(f)
                if pdf.isEncrypted: #checking if file is encrypted. Can`t work with encrypted files. Maybe will be added
                    print(f'file ({filename}) is encrypted. Decrypt it first')
                    sys.exit()
                pages = pdf.numPages
                fullText = []
                text = ''
                for i in range(pages):
                    page = pdf.getPage(i)
                    text = page.extractText()
                    fullText.append(text)
                for i in range(len(fullText)):
                    text += ' ' + fullText[i] #quite the same algorithm, but with the specs of PyPDF2 module
                text = text.split()
                howlong = len(set(text))
            return set(text), howlong
        except Exception:
            return 'Something wrong with files', 'Error'
    if filetype == 'txt':
        print('Working with txt...')
        try:
            with open(filename, 'r') as f:
                fullText = []
                text = ''
                for text in f:
                    fullText.append(text)
                for i in range(len(fullText)):
                    text += ' ' + fullText[i]
                text = text.split()
                howlong = len(set(text))
            return set(text), howlong
        except Exception:
            return 'Something wrong with files', 'Error'


file1words, file1len = getText('') #Enter file 1 path or name(if it is in the same directory)
file2words, file2len = getText('') #Enter file 2 path or name(if it is in the same directory)
if file1words == 'Something wrong with files':
    print(file1words)
else:
    inter = set.intersection(file1words, file2words)
    print(
        f'File 1 len = {file1len}, file 2 len = {file2len}, intersection = {len(inter)}. File 2 has originality {((file2len - len(inter)) * 100 / file2len)}% ')
