import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Voz en inglés
id_ingles = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# Escuchar el micrófono y devolver el audio como texto
def transformar_audio_en_texto():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:

        # Tiempo de espera hasta la activación del micro
        r.pause_threshold = 0.8

        # Informar que empezó la grabación
        print('Ya puedes hablar')

        # Guardar el audio en variable
        audio = r.listen(origen)

        # En caso de errores
        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language='es-es')

            # Prueba de funcionamiento
            print('Has dicho: ' + pedido)

            # Devolver pèdido
            return pedido

        # En caso de error de comprension
        except sr.UnknownValueError:

            # Prueba de incomprensión de audio
            print('No te he entendido.')

            # Devolver error
            return 'Sigo esperando'

        # En caso de no poder resolver la petición
        except sr.RequestError:

            # Prueba de incomprensión de audio
            print('En este momento, la función no se encuentra disponible.')

            # Devolver error
            return 'Sigo esperando'

        # Error inesperado
        except:

            # Prueba de incomprensión de audio
            print('Se ha producido un error.')

            # Devolver error
            return 'Sigo esperando'


# Función para poder escuchar al asistente
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Función para poder escuchar al asistente en inglés
def hablar_ingles(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Establecer voz en inglés
    engine.setProperty('voice', id_ingles)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar del día de la semana
def pedir_dia():

    # Crear variable con datos de hoy
    dia = datetime.date.today()

    # Crear una variable para el día de la semana
    dia_semana = dia.weekday()

    # Diccionario con nombres de días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}.')


# Dar la hora
def pedir_hora():
    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} y {hora.minute}.'

    # Decir la hora
    hablar(hora)


# Saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches.'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días.'
    else:
        momento = 'Buenas tardes.'

    # Saludar
    hablar(f'Hola, {momento} Soy Helena, tu asistente virtual. ¿En qué puedo ayudarte?')


# Función central del asistente
def pedir_cosas():

    # Activar el saludo inicial
    saludo_inicial()

    # Variable de corte para el loop while
    comenzar = True

    # Loop central
    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        # Derivar en función del contenido de la petición
        if 'abre youtube' in pedido:
            hablar('Estoy abriendo YouTube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abre el navegador' in pedido:
            hablar('Estoy abriendo el navegador.')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Estoy buscando en la Wikipedia.')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f'Esto es lo que he encontrado sobre {pedido}. {resultado}')
            continue
        elif 'busca en internet' in pedido:
            hablar('Buscando en internet...')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado.')
            continue
        elif 'reproduce' in pedido:
            hablar('Vamos allá.')
            pedido = pedido.replace('reproduce', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'informacion sobre las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Lo siento, no he podido localizar la información.')
                continue

        elif 'adiós' in pedido:
            hablar('¡Hasta pronto!')
            comenzar = False

pedir_cosas()
