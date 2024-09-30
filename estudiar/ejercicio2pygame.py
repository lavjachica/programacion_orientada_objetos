import pygame

# Inicializamos Pygame
pygame.init()

# Definimos colores
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
MORADO = (128, 0, 128)  # Color que aparecerá cuando choquen

# Tamaño de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Clase Triángulo
class Triangulo:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = ROJO  # Color por defecto
        self.tiempo_choque = 0  # Tiempo desde el último choque

    def mover(self, dx, dy, otras_figuras):
        nueva_pos = [self.pos[0] + dx, self.pos[1] + dy]
        if not self.colision(nueva_pos, otras_figuras):
            self.pos = nueva_pos

    def dibujar(self, pantalla):
        pygame.draw.polygon(pantalla, self.color, [
            (self.pos[0], self.pos[1]),
            (self.pos[0] - 30, self.pos[1] + 50),
            (self.pos[0] + 30, self.pos[1] + 50)
        ])

    def obtener_rect(self):
        return pygame.Rect(self.pos[0] - 30, self.pos[1], 60, 50)

    def colision(self, nueva_pos, otras_figuras):
        for figura in otras_figuras:
            if figura != self and figura.obtener_rect().colliderect(pygame.Rect(nueva_pos[0] - 30, nueva_pos[1], 60, 50)):
                self.color = MORADO  # Cambia a color morado al colisionar
                figura.color = MORADO  # Cambia el color de la otra figura también
                self.tiempo_choque = pygame.time.get_ticks()  # Guardamos el tiempo de choque
                figura.tiempo_choque = pygame.time.get_ticks()  # Guardamos el tiempo de choque
                return True
        return False

    def actualizar_color(self):
        if self.color == MORADO and pygame.time.get_ticks() - self.tiempo_choque > 500:  # 500 ms
            self.color = ROJO  # Restablecer color a rojo

# Clase Cuadrado
class Cuadrado:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = VERDE  # Color por defecto
        self.tiempo_choque = 0  # Tiempo desde el último choque

    def mover(self, dx, dy, otras_figuras):
        nueva_pos = [self.pos[0] + dx, self.pos[1] + dy]
        if not self.colision(nueva_pos, otras_figuras):
            self.pos = nueva_pos

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (*self.pos, 50, 50))

    def obtener_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], 50, 50)

    def colision(self, nueva_pos, otras_figuras):
        for figura in otras_figuras:
            if figura != self and figura.obtener_rect().colliderect(pygame.Rect(nueva_pos[0], nueva_pos[1], 50, 50)):
                self.color = MORADO  # Cambia a color morado al colisionar
                figura.color = MORADO  # Cambia el color de la otra figura también
                self.tiempo_choque = pygame.time.get_ticks()  # Guardamos el tiempo de choque
                figura.tiempo_choque = pygame.time.get_ticks()  # Guardamos el tiempo de choque
                return True
        return False

    def actualizar_color(self):
        if self.color == MORADO and pygame.time.get_ticks() - self.tiempo_choque > 500:  # 500 ms
            self.color = VERDE  # Restablecer color a verde

# Clase Círculo
class Circulo:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = AZUL  # Color por defecto
        self.tiempo_choque = 0  # Tiempo desde el último choque

    def mover(self, dx, dy, otras_figuras):
        nueva_pos = [self.pos[0] + dx, self.pos[1] + dy]
        if not self.colision(nueva_pos, otras_figuras):
            self.pos = nueva_pos

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, self.pos, 25)

    def obtener_rect(self):
        return pygame.Rect(self.pos[0] - 25, self.pos[1] - 25, 50, 50)

    def colision(self, nueva_pos, otras_figuras):
        for figura in otras_figuras:
            if figura != self and figura.obtener_rect().colliderect(pygame.Rect(nueva_pos[0] - 25, nueva_pos[1] - 25, 50, 50)):
                self.color = MORADO  # Cambia a color morado al colisionar
                figura.color = MORADO  # Cambia el color de la otra figura también
                self.tiempo_choque = pygame.time.get_ticks()  # Guardamos el tiempo de choque
                figura.tiempo_choque = pygame.time.get_ticks()  # Guardamos el tiempo de choque
                return True
        return False

    def actualizar_color(self):
        if self.color == MORADO and pygame.time.get_ticks() - self.tiempo_choque > 500:  # 500 ms
            self.color = AZUL  # Restablecer color a azul

# Creación de las figuras
triangulo = Triangulo(100, 300)
cuadrado = Cuadrado(300, 300)
circulo = Circulo(500, 300)
figuras = [triangulo, cuadrado, circulo]

# Control de FPS
clock = pygame.time.Clock()

# Bucle principal
corriendo = True
while corriendo:
    pantalla.fill((255, 255, 255))  # Fondo blanco

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

    # Teclas para mover el triángulo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        triangulo.mover(-5, 0, figuras)
    if keys[pygame.K_d]:
        triangulo.mover(5, 0, figuras)
    if keys[pygame.K_w]:
        triangulo.mover(0, -5, figuras)
    if keys[pygame.K_s]:
        triangulo.mover(0, 5, figuras)

    # Teclas para mover el cuadrado
    if keys[pygame.K_LEFT]:
        cuadrado.mover(-5, 0, figuras)
    if keys[pygame.K_RIGHT]:
        cuadrado.mover(5, 0, figuras)
    if keys[pygame.K_UP]:
        cuadrado.mover(0, -5, figuras)
    if keys[pygame.K_DOWN]:
        cuadrado.mover(0, 5, figuras)

    # Teclas para mover el círculo
    if keys[pygame.K_j]:
        circulo.mover(-5, 0, figuras)
    if keys[pygame.K_l]:
        circulo.mover(5, 0, figuras)
    if keys[pygame.K_i]:
        circulo.mover(0, -5, figuras)
    if keys[pygame.K_k]:
        circulo.mover(0, 5, figuras)

    # Actualizar el color de las figuras si es necesario
    triangulo.actualizar_color()
    cuadrado.actualizar_color()
    circulo.actualizar_color()

    # Dibujamos las figuras
    triangulo.dibujar(pantalla)
    cuadrado.dibujar(pantalla)
    circulo.dibujar(pantalla)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Control de la velocidad del juego
    clock.tick(60)

# Cerramos Pygame
pygame.quit()
