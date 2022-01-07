import pygame
import settings

# Initializing pygame
pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

# Screen setup
screen = pygame.display.set_mode(800, 600)
pygame.display.set_caption(settings.caption)
background = pygame.image.load(settings.background_image)
pygame.display.set_icon(pygame.image.load(settings.icon_image))


# TODO Sounds setup
"""
explosion_fx = pygame.mixer.Sound("img/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound("img/laser.wav")
laser_fx.set_volume(0.25)
"""


running = True
while running:
    screen.blit(background, (0, 0))
    clock.tick(settings.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    

pygame.quit()