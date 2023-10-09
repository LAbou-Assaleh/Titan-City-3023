import pygame
import random
import math
import sys
from pygame.locals import QUIT

go = False
gray = (128, 128, 128)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
shayaanBlue = (1, 23, 45)
astroidpos = []
linepos = []
iarray = []
mlist = []
pygame.init()
ship = pygame.image.load("ship.png")
boom = pygame.image.load("boom.png")
btn = pygame.image.load("launch.png")
titan = pygame.image.load("TITAN.png")
mars = pygame.image.load("mars.png")
imp = pygame.image.load("NavBackgroundv2.png")
m1 = pygame.image.load("meteor1.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Navigation')
amask = pygame.mask.from_surface(m1)
tmask = pygame.mask.from_surface(titan)
mmask = pygame.mask.from_surface(mars)
smask = pygame.mask.from_surface(ship)

def path():
    pathcords = []
    x = 545
    y = 485
    while x > 250 or y > 100:
        if x > 250:
            x -= random.randrange(-5, 10)
        if y > 100:
            y -= random.randrange(-5, 10)
        pathcords.append([x, y])
    return pathcords

array = path()
def launch():
    end = False
    clock = pygame.time.Clock()
    global linepos
    x = 545
    y = 485
    while len(linepos) > 0:
        # print(linepos[0][0], linepos[0][1], x, y)
        dx = linepos[0][0] - x
        dy = linepos[0][1] - y
        d = pygame.math.Vector2(dx, dy).length()
        while d > 2:
            dx = linepos[0][0] - x
            dy = linepos[0][1] - y
            d = pygame.math.Vector2(dx, dy).length()
            if d > 2:
                direction = pygame.math.Vector2(dx, dy).normalize()
                x += direction.x * 2
                y += direction.y * 2
                x = int(x)
                y = int(y)
            screen.fill(shayaanBlue)
            screen.blit(mars, (520, 460))
            screen.blit(titan, (200, 40))
            screen.blit(ship, (x, y))
            pygame.draw.circle(screen, white, (250, 100), 10)
            screen.blit(imp, (0, 0))
            for i in range(len(astroidpos)):
                screen.blit(m1, astroidpos[i])
                if amask.overlap(smask, (astroidpos[i][0] - x, astroidpos[i][1] - y)):
                    end = True
            if end:
                screen.fill(black)
                font = pygame.font.SysFont('Retro Game', 50)
                txt = font.render("Mission Failed!", True, red)
                screen.blit(imp, (0, 0))
                screen.blit(txt, (260, 270))
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit(0)
            pygame.display.flip()
            clock.tick(120)
        linepos.pop(0)
        # x = linepos[0][0]
        # y = linepos[0][1]
        # a = smask.to_surface()
        # screen.fill(shayaanBlue)
        # screen.blit(mars, (520, 460))
        # screen.blit(titan, (200, 40))
        # screen.blit(a, (x, y))
        # pygame.draw.circle(screen, white, (250, 100), 10)
        # screen.blit(imp, (0, 0))
        # for i in range(len(astroidpos)):
        #     m = amask.to_surface()
        #     if amask.overlap(smask, (astroidpos[i][0] - x, astroidpos[i][1] - y)):
        #         print(amask.get_size())
        #         print(astroidpos[i], (x, y), (astroidpos[i][0] - x, astroidpos[i][1] - y))
        #         print(amask.overlap_area(smask, (astroidpos[i][0] - x, astroidpos[i][1] - y)))
        #         print(amask.overlap(smask, (astroidpos[i][0] - x, astroidpos[i][1] - y)))
        #         print("collide")
        #         end = True
        #         screen.fill(shayaanBlue)
        #         screen.blit(mars, (520, 460))
        #         screen.blit(titan, (200, 40))
        #         screen.blit(a, (x, y))
        #         pygame.draw.circle(screen, white, (250, 100), 10)
        #         screen.blit(imp, (0, 0))
        #     screen.blit(m, astroidpos[i])
        #     if end:
        #         break
        # linepos.pop(0)
        # pygame.display.flip()
        # clock.tick(120)
        # if end:
        #     return
def collide(x, y):
    for i in array:
        if (x - i[0] <= 30 and x-i[0] >= -30) and (y - i[1] <= 30 and y - i[1] >= -30):
            return True
    return False


def generate():
    x = random.randrange(210, 560)
    y = random.randrange(50, 430)
    while ((x > 560 or x < 300) and (y > 440 or y < 140)) or collide(x, y):
        # print(x - array[0][0], array[0][0], x)
        # print(x, y)
        x = random.randrange(210, 560)
        y = random.randrange(50, 500)
    astroidpos.append((x,y))

    return (x, y)
def end(x, y):
    if x > 325 and x < 475 and y > 540:
        return True
    else:
        return False

screen.fill(shayaanBlue)
screen.blit(mars, (520, 460))
screen.blit(titan, (200, 40))
screen.blit(ship, (545, 485))
pygame.draw.circle(screen, white, (250, 100), 10)
screen.blit(imp, (0, 0))
screen.blit(btn, (325, 540))
for i in range(30):
    screen.blit(m1, generate())
pygame.display.flip()
while True:
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        if end(x, y) and press[0]:
            launch()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION and x > 200 and x < 600 and y > 40 and y <540:
            if event.buttons[0]:
                last = (event.pos[0] - event.rel[0], event.pos[1] - event.rel[1])
                pygame.draw.line(screen, white, last, event.pos, 3)
                linepos.append([x, y])
        if pygame.mouse.get_pressed()[2]:
            linepos.clear()
            screen.fill(shayaanBlue)
            screen.blit(mars, (520, 460))
            screen.blit(titan, (200, 40))
            screen.blit(ship, (545, 485))
            pygame.draw.circle(screen, white, (250, 100), 10)
            screen.blit(imp, (0, 0))
            screen.blit(btn, (325, 540))
            for i in range(len(astroidpos)):
                screen.blit(m1, astroidpos[i])
    pygame.display.flip()
