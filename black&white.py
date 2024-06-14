import pygame
import sys
import source.players.players as players

pygame.init()

display_size = (950, 450)
display_caption = 'white'

clock = pygame.time.Clock()

screen = pygame.display.set_mode(display_size)
pygame.display.set_caption(display_caption)

player = players.deploy(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('grey')

    player.run(screen)
    pygame.display.update()
    clock.tick(60)