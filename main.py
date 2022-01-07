import pygame
# import os
# import time
# import random
import settings

pygame.font.init()

if settings.full_screen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((settings.width, settings.height))


# Setting caption and icon
pygame.display.set_caption(settings.caption)
pygame.display.set_icon(pygame.image.load(settings.icon_image))

# Load images
PLAYER_IMAGE = pygame.image.load(settings.player_image)
ALIEN_IMAGES = pygame.image.load(settings.alien_image[0])
BULLET_IMAGE = pygame.image.load(settings.bullet_image)
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(settings.background_image), (screen.get_width(), screen.get_height()))


class Object:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.obj_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.obj_image, (self.x, self.y))


class Player(Object):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.obj_image = PLAYER_IMAGE
        self.laser_image = BULLET_IMAGE
        self.mask = pygame.mask.from_surface(self.obj_image)
        self.max_health = health

    def get_width(self):
        return self.obj_image.get_width()

    def get_height(self):
        return self.obj_image.get_height()


def main():
    run = True
    FPS = settings.fps
    level = settings.player_level
    lives = settings.player_lives
    player_speed = settings.player_speed
    main_font = pygame.font.SysFont("comics", 50)
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # creating a player
    player = Player(screen_width/2, screen_height*3/4)

    clock = pygame.time.Clock()

    def redraw_screen():
        screen.blit(BACKGROUND_IMAGE, (0, 0))

        # Draw text
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (screen_width - level_label.get_width() - 10, 10))

        # Draw player
        player.draw(screen)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Checking all keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run = False
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x > 0:
            player.x -= player_speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player.get_width() < screen_width:
            player.x += player_speed
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y > 0:
            player.y -= player_speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player.get_height() < screen_height:
            player.y += player_speed


main()
