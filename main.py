# import speech_recognition as srec

# def perintah():
#     mendengar = srec.Recognizer()
#     with srec.Microphone() as source:
#         print("Silakan berbicara:.......")
#         suara = mendengar.listen(source, phrase_time_limit=5)
#         try:
#             print('diterima....')
#             dengar = mendengar.recognize_google(suara, language="id-ID")
#             print(dengar)
#         except:
#             pass
#         return dengar
    
# def run_sarip():
#     layanan = perintah()
#     print(layanan)

# run_sarip()

import speech_recognition as srec
from gtts import gTTS
import os

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print("Silakan berbicara.......")
        suara = mendengar.listen(source, phrase_time_limit=5)
        
        try:
            print('diterima....')
            dengar = mendengar.recognize_google(suara, language="id-ID")
            print(dengar)
            return dengar 
        except srec.UnknownValueError:
            print("Google Speech Recognition tidak dapat memahami audio.")
            return None
        except srec.RequestError as e:
            print(f"Kesalahan saat menghubungi Google Speech Recognition service: {e}")
            return None

def bacot(teks):
    bahasa = 'id'
    namafile = 'bacot.mp3'
    
    # Membuat file suara
    suara = gTTS(text=teks, lang=bahasa, slow=False)
    suara.save(namafile)
    os.system(f'start {namafile}')  # Untuk Windows, gunakan 'start', untuk Mac gunakan 'afplay'
    
def run_sarip():
    layanan = perintah()
    if layanan:  
        print(f"Layanan yang diterima: {layanan}")
        bacot(layanan)  # Memanggil fungsi bacot dengan teks yang diterima
    else:
        print("Tidak ada layanan yang diterima.")

run_sarip()
