import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configurar la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento de Formas")

# Definir la velocidad de movimiento
velocidad = 5

# Clase para el triángulo
class Triangulo:
    def __init__(self, x, y):
        self.pos = [x, y]

    def mover(self, teclas):
        if teclas[pygame.K_w]:
            self.pos[1] -= velocidad
        if teclas[pygame.K_s]:
            self.pos[1] += velocidad
        if teclas[pygame.K_a]:
            self.pos[0] -= velocidad
        if teclas[pygame.K_d]:
            self.pos[0] += velocidad

    def dibujar(self, pantalla):
        pygame.draw.polygon(pantalla, ROJO, [(self.pos[0], self.pos[1]), 
                                             (self.pos[0]-30, self.pos[1]+50), 
                                             (self.pos[0]+30, self.pos[1]+50)])

# Clase para el cuadrado
class Cuadrado:
    def __init__(self, x, y):
        self.pos = [x, y]

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
        pygame.draw.rect(pantalla, VERDE, (*self.pos, 50, 50))

# Clase para el círculo
class Circulo:
    def __init__(self, x, y):
        self.pos = [x, y]

    def mover(self, teclas):
        if teclas[pygame.K_i]:
            self.pos[1] -= velocidad
        if teclas[pygame.K_k]:
            self.pos[1] += velocidad
        if teclas[pygame.K_j]:
            self.pos[0] -= velocidad
        if teclas[pygame.K_l]:
            self.pos[0] += velocidad

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, AZUL, self.pos, 25)

# Crear las formas
triangulo = Triangulo(100, 300)
cuadrado = Cuadrado(300, 300)
circulo = Circulo(500, 300)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover las formas
    triangulo.mover(teclas)
    cuadrado.mover(teclas)
    circulo.mover(teclas)

    # Dibujar las formas
    pantalla.fill(BLANCO)
    triangulo.dibujar(pantalla)
    cuadrado.dibujar(pantalla)
    circulo.dibujar(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()

