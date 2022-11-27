import fitz #PyMuPdf
import PyPDF2
import pdfplumber

import time
import os
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def PyMuPDF(archivo, nombreArchivo, cuenta):
    try:
        inicio = time.time()
        pdf = fitz.open(archivo)

        pages = pdf.page_count
        text_page = ""

        for page in range (pages):
            pagina = pdf.load_page(page)        
            text_page += pagina.get_text()

        fin = time.time()

        palabras_total = word_tokenize(text_page) # Se extraen todas las palabras.
        stop_words = set(stopwords.words('english')) # Guardamos los conectores de la libreria NLTK 
        palabras = list(filter(lambda token: token not in string.punctuation, palabras_total)) # Se quitan los signos de puntación.
        filtro = []
        # Se quitan las stopwords (conectores, pronombres y demas).
        for palabra in palabras:
            if palabra not in stop_words:
                filtro.append(palabra)

        correctas = 0
        for palabra in filtro:
            significado = wordnet.synsets(palabra)
            if len(significado) > 0:
                correctas += 1

        print('PyMuPdf|' + str(cuenta) + '|' + str(nombreArchivo) + '|' + str(fin-inicio) + "|" + str(len(palabras_total)) + "|" + str(len(palabras)) + "|" + 
                str(len(filtro)) + "|" + str(correctas))
        
    except Exception as inst:

        print("PyMuPdf|" + str(cuenta) + "|" + str(nombreArchivo) + "|Error: " + str(type(inst)) + " " + str(inst) + "|TE|PTE|PFE|PCE")

def PyPdf2(archivo, nombreArchivo, cuenta):
    try:
        inicio = time.time()    
        pdf = open(archivo, "rb")

        reader = PyPDF2.PdfReader(pdf)
        texto = ""    
        for num_page in range(len(reader.pages)):        
            info_page = reader._get_page(num_page)
            texto += info_page.extract_text()

        fin = time.time()  

        palabras_total = word_tokenize(texto) # Se extraen todas las palabras.
        stop_words = set(stopwords.words('english')) # Guardamos los conectores de la libreria NLTK
        palabras = list(filter(lambda token: token not in string.punctuation, palabras_total)) # Se quitan los signos de puntación.
        filtro = []
        # Se quitan las stopwords (conectores, pronombres y demas).
        for palabra in palabras:
            if palabra not in stop_words:
                filtro.append(palabra)

        correctas = 0
        for palabra in filtro:
            significado = wordnet.synsets(palabra)
            if len(significado) > 0:
                correctas += 1

        print('PyPdf2|' + str(cuenta) + '|' + str(nombreArchivo) + '|' + str(fin-inicio) + "|" + str(len(palabras_total)) + "|" + str(len(palabras)) + "|" + 
                str(len(filtro)) + "|" + str(correctas))
        
    except Exception as inst:

        print("PyPdf2|" + str(cuenta) + "|" + str(nombreArchivo) + "|Error: " + str(type(inst)) + " " + str(inst) + "|TE|PTE|PFE|PCE")

def PyPdfPlumber(archivo, nombreArchivo, cuenta):
    try:        
        inicio = time.time()

        pdf = pdfplumber.open(archivo)  

        text = ""    
        for pages in pdf.pages:       
            text += pages.extract_text()

        fin = time.time()

        palabras_total = word_tokenize(text) # Se extraen todas las palabras.
        stop_words = set(stopwords.words('english')) # Guardamos los conectores de la libreria NLTK
        palabras = list(filter(lambda token: token not in string.punctuation, palabras_total)) # Se quitan los signos de puntación.
        filtro = []
        # Se quitan las stopwords (conectores, pronombres y demas).
        for palabra in palabras:
            if palabra not in stop_words:
                filtro.append(palabra)

        correctas = 0
        for palabra in filtro:
            significado = wordnet.synsets(palabra)
            if len(significado) > 0:
                correctas += 1

        print('PyPdfPlumber|' + str(cuenta) + '|' + str(nombreArchivo) + '|' + str(fin-inicio) + "|" + str(len(palabras_total)) + "|" + str(len(palabras)) + "|" + 
                str(len(filtro)) + "|" + str(correctas))

    except Exception as inst:

        print("PyPdfPlumber|" + str(cuenta) + "|" + str(nombreArchivo) + "|Error: " + str(type(inst)) + " " + str(inst) + "|TE|PTE|PFE|PCE")

carpeta = "carpeta"
cuenta = 1
files = os.listdir(carpeta)

print("Libreria|# Archivo|Archivo|Tiempo|Palabras Totales|Palabras sin signos|Palabras finales|Plabras correctas")
for file in files:
    if ".pdf" in file:
        archivo = carpeta + "/" + file

        ## PyMuPdf ## 
        PyMuPDF(archivo, file, cuenta)

        ## PyPdf2 ##
        PyPdf2(archivo, file, cuenta)
        
        ## PyPdfPlumber ##   
        PyPdfPlumber(archivo, file, cuenta)
        cuenta += 1

# print(str(fin-inicio)) #Tiempo de proceso
# print(str(len(palabras_total))) #palabras totales del archivo
# print(str(len(palabras))) #palabras sin signos de puntuación
# print(str(len(filtro))) #palabras sin stopwords
# print(str(correctas) + "\n\n") #palabras correctas