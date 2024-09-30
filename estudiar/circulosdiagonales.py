import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
MORADO = (128, 0, 128)

# Configurar la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento de Círculos")

# Definir la velocidad de movimiento
velocidad = 5

# Clase para los círculos
class Circulo:
    def __init__(self, x, y, color):
        self.pos = [x, y]
        self.color = color
        self.radio = 25

    def mover(self, teclas):
        if teclas[pygame.K_UP]:
            self.pos[1] -= velocidad
        if teclas[pygame.K_DOWN]:
            self.pos[1] += velocidad
        if teclas[pygame.K_LEFT]:
            self.pos[0] -= velocidad
        if teclas[pygame.K_RIGHT]:
            self.pos[0] += velocidad

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, self.pos, self.radio)

    def colisionar(self, otro):
        # Verificar si colisiona con otro círculo
        distancia = ((self.pos[0] - otro.pos[0]) ** 2 + (self.pos[1] - otro.pos[1]) ** 2) ** 0.5
        return distancia < (self.radio + otro.radio)

# Crear los círculos
circulo1 = Circulo(300, 300, AZUL)
circulo2 = Circulo(500, 300, VERDE)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover los círculos
    circulo1.mover(teclas)
    circulo2.mover(teclas)

    # Verificar colisiones y cambiar colores
    if circulo1.colisionar(circulo2):
        circulo1.color = MORADO
        circulo2.color = MORADO
    else:
        circulo1.color = AZUL
        circulo2.color = VERDE

    # Dibujar las formas
    pantalla.fill(BLANCO)
    circulo1.dibujar(pantalla)
    circulo2.dibujar(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
