import pygame
import random
import math
from pygame import mixer


# Iniciar Pygame
pygame.init()


# Crear pantalla y establecer dimensiones
pantalla = pygame.display.set_mode((800,600))


# Establecer título
pygame.display.set_caption('Marcianitos Sensuales')

# Definir icono - El icono es recomendable que sea formato png y de 32px
icono = pygame.image.load('marcianito.png')
pygame.display.set_icon(icono)

# Música de fondo
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Guardar imagen de fondo
fondo = pygame.image.load('fondo.jpg')


# Variables del jugador
img_jugador = pygame.image.load('jugador.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

# Variables del proyectil
img_proyectil = pygame.image.load('proyectil.png')
proyectil_x = 0
proyectil_y = 500
proyectil_x_cambio = 0
proyectil_y_cambio = 3
proyectil_visible = False

# Puntuación
puntos = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf',60)

def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60,200))

# Función mostrar puntuación
def mostrar_puntuacion(x,y):
    texto = fuente.render(f'Puntuación: {puntos}', True, (255,255,255))
    pantalla.blit(texto, (x, y))

# Función jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

# Función enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

# Función disparar proyectil
def disparar_proyectil(x,y):
    global proyectil_visible
    proyectil_visible = True
    pantalla.blit(img_proyectil,(x+16,y+10))

# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego, mantiene la ventana hasta que es cerrada manualmente
se_ejecuta = True
while se_ejecuta:


    # Cambiar color de fondo de la pantalla
    # pantalla.fill((76, 53, 15))
    # Usar imagen de fondo
    pantalla.blit(fondo,(0,0))

    # Iteración de eventos
    for evento in pygame.event.get():

        # Cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Presión de tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not proyectil_visible:
                    proyectil_x = jugador_x
                    disparar_proyectil(proyectil_x,proyectil_y)

        # Soltar tecla (flechas)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0


    # Modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    # Colisión de los bordes del jugador
    if jugador_x <= 0:
        jugador_X = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        enemigo_x[e] += enemigo_x_cambio[e]

        # Colisión de los bordes del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisión
        colision = hay_colision(enemigo_x[e], enemigo_y[e], proyectil_x, proyectil_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.play(   )
            proyectil_y = 500
            proyectil_visible = False
            puntos += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        # Visualizar enemigo en pantalla
        enemigo(enemigo_x[e], enemigo_y[e], e)

        # Movimiento proyectil
        if proyectil_y <= -64:
            proyectil_y = 500
            proyectil_visible = False
        if proyectil_visible:
            disparar_proyectil(proyectil_x, proyectil_y)
            proyectil_y -= proyectil_y_cambio



    # Visualizar jugador en pantalla
    jugador(jugador_x,jugador_y)

    # Mostrar puntuación
    mostrar_puntuacion(texto_x,texto_y)


    # Actualizar el juego
    pygame.display.update()
