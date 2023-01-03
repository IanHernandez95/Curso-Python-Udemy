import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Opciones de voz/idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'


# escuchar nuestro microfono y pasar el audio a texto
def audio_a_texto():

    # Almacenar el Reconocedor en una variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('Empezo la grabacion')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language='es_CL')

            # Prueba de que ingreso
            print('Dijiste: ' + pedido)

            # Devolver pedido
            return pedido

        # en caso de que no comprenda
        except sr.UnknownValueError:

            # Prueba de que no comprendio el audio
            print('No entendi')

            # Devolver error
            return 'Sigo esperando'

        # En caso de no resolver el pedido
        except sr.RequestError:

            # Prueba de que no comprendio el audio
            print('No hay servicio')

            # Devolver error
            return 'Sigo esperando'

        # Error inesperado
        except:

            # Prueba de que no comprendio el audio
            print('Algo salio mal')

            # Devolver error
            return 'Sigo esperando'

# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1 )

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Pedir el dia de la semana
def pedir_dia():
    
    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #Crear variable para el dia de Semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres de dias
    semana = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo',
    }

    # Decir el dia de la semana
    hablar(f'Hoy es {semana[dia_semana]}')

# Pedir que hora es
def pedir_hora():

    #Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    
    # Decir la hora
    hablar(hora)

def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 12:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento}, soy Samira, tu asistente personal. Por favor dime en que te puedo ayudar')

def pedir_cosas():

    # Activart saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # Activar el micro y guardar el pedido
        pedido = audio_a_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('Https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Con gusto, estoy abriedo el navegador')
            webbrowser.open('Https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar(f'buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducir')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple':'APPL',
                'amazon':'AMZN',
                'google':'GOOGL'
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


pedir_cosas()