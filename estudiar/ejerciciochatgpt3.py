import pygame 
pygame.init()

# Crear colores 
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Velocidad del movimiento 
velocidad = 0.5

# Pantalla 
ALTO = 600
ANCHO = 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))

class Cuadrado:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = BLANCO  # Color inicial

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
        pygame.draw.rect(pantalla, self.color, (*self.pos, 50, 50))

    def colision(self, circulo):
        # Comprobar colisión con el círculo
        distancia = ((self.pos[0] + 25 - circulo.pos[0]) ** 2 + (self.pos[1] + 25 - circulo.pos[1]) ** 2) ** 0.5
        return distancia < 50  # Radio del círculo + la mitad del lado del cuadrado

class Circulo:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = BLANCO  # Color inicial

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
        pygame.draw.circle(pantalla, self.color, self.pos, 25)

# Crear los objetos
cuadrado1 = Cuadrado(30, 30)
circulo1 = Circulo(80, 80)

# Bucle principal 
ejecutando = True 
while ejecutando:  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False 

    teclas = pygame.key.get_pressed()
    cuadrado1.mover(teclas)
    circulo1.mover(teclas)

    # Comprobar colisión
    if cuadrado1.colision(circulo1):
        cuadrado1.color = ROJO
        circulo1.color = ROJO
    else:
        cuadrado1.color = BLANCO
        circulo1.color = BLANCO

    pantalla.fill(NEGRO)
    cuadrado1.dibujar(pantalla)
    circulo1.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()

