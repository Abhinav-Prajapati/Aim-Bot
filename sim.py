import pygame
import math

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
clock = pygame.time.Clock()


class Rectangle:
    def __init__(self, pos_x: int, pos_y: int, color: tuple) -> None:
        self.width = 0
        self.hight = 0
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.COLOR = color

    def drawBar(self, screen, width: int, hight: int):
        arrowHight = 30
        arrowWidth = 8
        self.width = width
        self.hight = hight

        self.pos_x = self.pos_x-self.width
        self.pos_y = self.pos_y-self.hight
        pygame.draw.rect(screen, self.COLOR, (self.pos_x,
                                              self.pos_y, self.width, self.hight))
        pygame.draw.polygon(screen, (0, 0, 0),
                            ((self.pos_x-arrowWidth, self.pos_y), (self.pos_x+(self.width/2), self.pos_y-arrowHight), (self.pos_x+self.width+arrowWidth, self.pos_y)))


bar_width = 40
val = 0
font = pygame.font.SysFont("Arial", 28)

while True:

    val += 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("white")

    bar_hight = (math.sin(val) + 1)*100

    bar_1 = Rectangle(120, SCREEN_HIGHT - 150, (0, 0, 0))
    bar_2 = Rectangle(195, SCREEN_HIGHT - 150, (0, 0, 0))
    bar_3 = Rectangle(270, SCREEN_HIGHT - 150, (0, 0, 0))

    bar_1.drawBar(screen, 10, bar_hight)
    bar_2.drawBar(screen, 10, bar_hight*0.6)
    bar_3.drawBar(screen, 10, bar_hight*0.8)

    pygame.draw.rect(screen, (0, 0, 0),
                     (100, SCREEN_HIGHT-150, 180, 50), 10, 10)

    # Divider line
    pygame.draw.rect(screen, (100, 100, 100), (850, 30, 5, SCREEN_HIGHT-30*2))
    # Horizontal line
    pygame.draw.rect(screen, (100, 100, 100), (850, 300, 330, 5))

    sensor_1 = font.render(
        f"Sensor 1 : { int(bar_hight*0.5)}", True, (0, 0, 0))
    screen.blit(sensor_1, (860, 310))

    sensor_2 = font.render(
        f"Sensor 2 : { int(bar_hight*0.7)}", True, (0, 0, 0))
    screen.blit(sensor_2, (860, 340))

    sensor_3 = font.render(f"Sensor 3 : { int(bar_hight)}", True, (0, 0, 0))
    screen.blit(sensor_3, (860, 370))

    targate_distance = font.render(
        f"Targate Dst : {10} Cm", True, (0, 0, 0))
    screen.blit(targate_distance, (860, 430))

    current_distance = font.render(
        f"Current Dst : {6} Cm", True, (0, 0, 0))
    screen.blit(current_distance, (860, 460))

    # Aim status

    x_lock_msg = font.render(
        f"Rotation ", True, (0, 0, 0))
    screen.blit(x_lock_msg, (860, 50))

    pygame.draw.circle(screen,(0,255,0),(1000,62),20)


    x_lock_msg = font.render(
        f"Forward ", True, (0, 0, 0))
    screen.blit(x_lock_msg, (860, 120))

    pygame.draw.circle(screen,(255,0,0),(1000,132),20)


    pygame.time.delay(10)
    pygame.display.flip()  # Refresh on-screen display
