import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 500))
my_surface = pygame.Surface((100, 100))
my_rect = pygame.Rect(75, 100, 150, 150)

timer = pygame.time.Clock()
x = 150
y = 200

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color("green"))
    my_surface.fill((35, 237, 219))
    screen.blit(my_surface, (x, y))
    pygame.draw.rect(screen, pygame.Color("purple"), my_rect)
    #  print(f"x = {x} et y = {y}")
    pygame.display.update()
    #  x = x + 1
    timer.tick(60)

