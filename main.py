import pygame

# Initializing pygame
pygame.init()
running = True
pygame.mouse.set_visible(False)

# Screen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Space-invaders by @JKrecisz')
background = pygame.image.load('images/background.png')
pygame.display.set_icon(pygame.image.load('images/icon.png'))

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
