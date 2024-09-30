import pygame

# Inicializamos Pygame
pygame.init()

# Definimos colores
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
MORADO = (128, 0, 128)

# Tamaño de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Clase Círculo
class Circulo:
    def __init__(self, x, y, radio, color):
        self.pos = [x, y]
        self.radio = radio
        self.color = color
        self.color_original = color

    def mover(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

    def dibujar(self):
        pygame.draw.circle(pantalla, self.color, (int(self.pos[0]), int(self.pos[1])), self.radio)

    def colision(self, otro):
        distancia = ((self.pos[0] - otro.pos[0]) ** 2 + (self.pos[1] - otro.pos[1]) ** 2) ** 0.5
        if distancia < self.radio + otro.radio:
            self.color = MORADO
            otro.color = MORADO
        else:
            self.color = self.color_original
            otro.color = otro.color_original

# Creación de círculos
circulo1 = Circulo(300, 300, 30, ROJO)
circulo2 = Circulo(500, 300, 30, AZUL)

# Control de FPS
clock = pygame.time.Clock()

# Bucle principal
corriendo = True
while corriendo:
    pantalla.fill((255, 255, 255))  # Fondo blanco

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

    # Movimiento de los círculos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: circulo1.mover(-5, 0)
    if keys[pygame.K_d]: circulo1.mover(5, 0)
    if keys[pygame.K_w]: circulo1.mover(0, -5)
    if keys[pygame.K_s]: circulo1.mover(0, 5)

    # Colisión
    circulo1.colision(circulo2)

    # Dibujar círculos
    circulo1.dibujar()
    circulo2.dibujar()

    # Actualizamos la pantalla
    pygame.display.flip()

    # Control de la velocidad del juego
    clock.tick(60)

# Cerramos Pygame
pygame.quit()
