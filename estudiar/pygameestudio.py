## crear colisiones de cuadrados 
import pygame 
pygame.init()

##crear colores 
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
color_primario1 = (255, 0, 0)
color_primario2 = (0, 255, 0)
## velocidad del movimiento 
velocidad = 0.5
## pantalla 
Alto = 600
Ancho = 800
pantalla = pygame.display.set_mode((Ancho, Alto))

class Cuadrado:
    def __init__(self, x, y):
        self.pos = [x,y]

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
        pygame.draw.rect(pantalla, Blanco, (*self.pos,50,50))
class Circulo:
    def __init__(self, x, y):
        self.pos = [x,y]

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
        pygame.draw.circle(pantalla, Blanco, self.pos, 25)

cuadrado1 = Cuadrado(30,30)
Circulo1 = Circulo(80,80)
## Bucle principal 
ejecutando = True ## ejecutando, verdadero, mientras ejecutando sea verdadero, para evento en pygame.event.get()
while ejecutando:  ## si evento de tipo PYGAME.QUIT: entonces ejecutando sera falso 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False 
    teclas = pygame.key.get_pressed()
    cuadrado1.mover(teclas)
    Circulo1.mover(teclas)
    pantalla.fill(Negro)
    cuadrado1.dibujar(pantalla)
    Circulo1.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
