import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from os import system

system("cls")


#$ Escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #° Almacenar recognizer en variable
    r = sr.Recognizer()

    with sr.Microphone() as origen:
        #% Tiempo de espera
        r.pause_threshold = 0.5

        #% Informar que comenzo la grabacion
        print("Ya puedes hablar")

        #% Guardar el audio
        audio = r.listen(origen)

        try:
            #% buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            #% prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            #% devolver pedido
            return pedido
        #% En caso de que no comprenda el audio
        except sr.UnknownValueError:

            #% Prueba de que no comprendio el audio
            print("No entendi")

            #% devolver error
            return "Sigo esperando"

        #% En caso de no resolver el pedido
        except sr.RequestError:
             #% Prueba de que no comprendio el audio
            print("No hay servicio")

            #% devolver error
            return "Sigo esperando"

        #% En caso de no resolver el pedido
        except sr.RequestError:
             #% Prueba de que no comprendio el audio
            print("Algo ha salido mal")

            #% devolver error
            return "Sigo esperando"
#transformar_audio_en_texto()

def hablar(mensaje):

    #° encender el motor de pyttsx3
    engine = pyttsx3.init()

    #% pronuncia rl mensaje
    engine.say(mensaje)
    engine.runAndWait()
#hablar("Hola perry")

#hablar(transformar_audio_en_texto())

def pedir_dia():
    #° crear variabe con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #% crear variable para el día de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de los dias
    calendario = {0:"Lunes", 1:"Martes", 2:"Miercoles", 3:"Jueves", 4:"Viernes", 5:"Sabado", 6:"Domingo"}
    
    # decir el dia de hoy
    hablar(f"Hoy es {calendario[dia_semana]}")

#pedir_dia()

def pedir_cosas():
    #! variable de corte
    comenzar = True

    #% loop central
    while comenzar:
        #% activar el micro y guardar el pedido en string
        pedido = transformar_audio_en_texto().lower()

        if 'abre youtube' in pedido:
            hablar("Abriendo")
            webbrowser.open("https://www.youtube.com/watch?v=b8HpBSxu6O8&t=3420s")
            continue

        elif "busca en wikipedia" in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(resultado)

        elif "busca en internet" in pedido:
            hablar("Buscando en internet")
            pedido = pedido.replace("busca en wikipedia", "")
            pywhatkit.search(pedido)
            hablar("Encontre esto")

        elif "reproducir" in pedido:
            hablar("Reproduciendo el video")
            pywhatkit.playonyt(pedido)
            if "pension" in pedido or "pensión" in pedido:
                hablar("Yo si me prendo con la pensión sion sion")

        elif "chiste" in pedido:
            hablar(pyjokes.get_joke("es"))

        elif "adíos" in pedido:
            hablar("Adios")
            break

pedir_cosas()

