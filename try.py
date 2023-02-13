import random

import pygame
from pygame.locals import *
import os
import sys

FPS = 35
fps = 12
all_sprites = pygame.sprite.Group()
pygame.font.init()


def load_image(name, color_key=None):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
        return image


def terminate():
    print("exit")
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def comics(image):
    fon = pygame.transform.scale(load_image(image), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tiles_group):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

        if tile_type == 'tent1':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'tent2':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'wall':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall2':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall3':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall4':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall5':
            self.add(vertical_group, box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall6':
            self.add(vertical_group, box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall7':
            self.add(horizontal_group, box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall8':
            self.add(horizontal_group, box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall9':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall10':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall11':
            self.add(box_group, horizontal_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall12':
            self.add(box_group, horizontal_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'crater1':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater2':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater3':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater4':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater5':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater6':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater7':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater8':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif tile_type == 'crater9':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        else:
            self.add(tiles_group, all_sprites)


class Cat(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y, tiles_group):
        super(Cat, self).__init__(tiles_group, box_group, all_sprites)
        if path == 'animations/cats/cat4/':
            self.index = 0
            self.images = []
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.images.append(pygame.image.load(f'{path}stand_2.png'))
            self.images.append(pygame.image.load(f'{path}stand_3.png'))
            self.images.append(pygame.image.load(f'{path}stand_4.png'))
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.images.append(pygame.image.load(f'{path}stand_2.png'))
            self.images.append(pygame.image.load(f'{path}stand_3.png'))
            self.images.append(pygame.image.load(f'{path}stand_4.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_7.png'))
            self.images.append(pygame.image.load(f'{path}stand_7.png'))
            self.images.append(pygame.image.load(f'{path}stand_8.png'))
            self.images.append(pygame.image.load(f'{path}stand_9.png'))
            self.images.append(pygame.image.load(f'{path}stand_8.png'))
            self.images.append(pygame.image.load(f'{path}stand_9.png'))
            self.images.append(pygame.image.load(f'{path}stand_8.png'))
            self.images.append(pygame.image.load(f'{path}stand_9.png'))
            self.images.append(pygame.image.load(f'{path}stand_8.png'))
            self.images.append(pygame.image.load(f'{path}stand_9.png'))
            self.images.append(pygame.image.load(f'{path}stand_10.png'))
            self.images.append(pygame.image.load(f'{path}stand_10.png'))
            self.images.append(pygame.image.load(f'{path}stand_11.png'))
            self.images.append(pygame.image.load(f'{path}stand_11.png'))
            self.images.append(pygame.image.load(f'{path}stand_12.png'))
            self.images.append(pygame.image.load(f'{path}stand_12.png'))
            self.images.append(pygame.image.load(f'{path}stand_12.png'))
            self.images.append(pygame.image.load(f'{path}stand_12.png'))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)
        elif path == 'animations/cats/cat5/':
            self.index = 0
            self.images = []
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)
        elif path == 'animations/cats/cat6/':
            self.index = 0
            self.images = []
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.index = 0
            self.images = []
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.images.append(pygame.image.load(f'{path}stand_2.png'))
            self.images.append(pygame.image.load(f'{path}stand_3.png'))
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.images.append(pygame.image.load(f'{path}stand_2.png'))
            self.images.append(pygame.image.load(f'{path}stand_3.png'))
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.images.append(pygame.image.load(f'{path}stand_2.png'))
            self.images.append(pygame.image.load(f'{path}stand_3.png'))
            self.images.append(pygame.image.load(f'{path}stand_1.png'))
            self.images.append(pygame.image.load(f'{path}stand_2.png'))
            self.images.append(pygame.image.load(f'{path}stand_3.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_7.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_7.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_7.png'))
            self.images.append(pygame.image.load(f'{path}stand_5.png'))
            self.images.append(pygame.image.load(f'{path}stand_6.png'))
            self.images.append(pygame.image.load(f'{path}stand_7.png'))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.mask = pygame.mask.from_surface(self.image)


class Balloon(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y, tiles_group):
        super(Balloon, self).__init__(tiles_group, all_sprites)
        if path == 'animations/balloons/balloon3/':
            super(Balloon, self).__init__(tiles_group, purpose_group, all_sprites)
            self.index = 0
            self.images = []
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)
        else:
            super(Balloon, self).__init__(tiles_group, box_group, all_sprites)
            self.index = 0
            self.images = []
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_1.png'))
            self.images.append(pygame.image.load(f'{path}/stand_2.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_3.png'))
            self.images.append(pygame.image.load(f'{path}/stand_4.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_5.png'))
            self.images.append(pygame.image.load(f'{path}/stand_6.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.images.append(pygame.image.load(f'{path}/stand_7.png'))
            self.images.append(pygame.image.load(f'{path}/stand_8.png'))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.mask = pygame.mask.from_surface(self.image)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, cloud_group):
        super().__init__(cloud_group, all_sprites)
        self.image = cloud_image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.mask = pygame.mask.from_surface(self.image)


class Purpose(pygame.sprite.Sprite):
    def __init__(self, purpose_type, pos_x, pos_y, purpose_group):
        super().__init__(purpose_group, all_sprites)
        self.image = purpose_image[purpose_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y, player_group):
        super(Player, self).__init__(player_group, all_sprites)
        self.x = 0
        self.y = 0
        if path == 'animations/player/cat1/':
            self.index = 0
            self.move = ''
            self.player_image = []
            self.player_image.append(pygame.image.load(f'{path}walk_1.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_2.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_1.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_2.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_3.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_4.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_3.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_4.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_5.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_6.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_5.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_6.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_7.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_8.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_7.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_8.png'))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_1.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_2.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_1.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_2.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_3.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_4.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_3.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_4.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_5.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_6.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_5.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_6.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_7.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_8.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_7.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_8.png'), True, False))
            self.image = self.player_image[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

        elif path == 'animations/player/cat2/':
            self.index = 0
            self.move = ''
            self.player_image = []
            self.player_image.append(pygame.image.load(f'{path}walk_1.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_2.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_1.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_2.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_3.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_4.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_3.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_4.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_5.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_6.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_5.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_6.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_7.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_8.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_7.png'))
            self.player_image.append(pygame.image.load(f'{path}walk_8.png'))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_1.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_2.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_1.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_2.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_3.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_4.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_3.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_4.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_5.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_6.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_5.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_6.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_7.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_8.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_7.png'), True, False))
            self.player_image.append(pygame.transform.flip(pygame.image.load(f'{path}walk_8.png'), True, False))
            self.image = self.player_image[self.index]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.index += 1
        if self.move == 'move_left':
            if self.index >= len(self.player_image):
                self.index = 0
            if self.index == 0:
                self.index = 16
                self.image = self.player_image[self.index]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.player_image[self.index]
                self.mask = pygame.mask.from_surface(self.image)
        elif self.move == 'move_right':
            if self.index >= len(self.player_image):
                self.index = 0
            if self.index == 16:
                self.index = 0
                self.image = self.player_image[self.index]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.player_image[self.index]
                self.mask = pygame.mask.from_surface(self.image)

    def move_down(self):
        self.rect = self.rect.move(0, +30)
        self.y += 30

    def move_up(self):
        self.rect = self.rect.move(0, -30)
        self.y -= 30

    def move_right(self):
        self.move = 'move_right'
        self.rect = self.rect.move(+30, 0)
        self.x += 30

    def move_left(self):
        self.move = 'move_left'
        self.rect = self.rect.move(-30, 0)
        self.x -= 30

    def updater(self):
        return f'{self.x}   {self.y}'


class Player2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, player_group):
        super(Player2, self).__init__(player_group, all_sprites)
        self.image = player_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.x = 0
        self.y = 0

    def move_down(self):
        self.rect = self.rect.move(0, +30)
        self.y += 30

    def move_up(self):
        self.rect = self.rect.move(0, -30)
        self.y -= 30

    def move_right(self):
        self.rect = self.rect.move(+30, 0)
        self.x += 30

    def move_left(self):
        self.rect = self.rect.move(-30, 0)
        self.x -= 30

    def updater(self):
        return f'{self.x}   {self.y}'


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, pos_x, pos_y, enemy_group):
        super().__init__(enemy_group, all_sprites)
        self.image = enemy_image[enemy_type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        allowed_values = list(range(-3, 3))
        allowed_values.remove(0)
        self.vx = random.choice(allowed_values)
        self.vy = random.choice(allowed_values)
        self.fx = 0

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_group):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_group):
            self.vx = -self.vx


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def play_level():
    player, purpose, x, y = generate_level(load_level('map.txt'))
    global tiles_group, player_group, purpose_group, box_group

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.move_down()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_up()
                elif event.key == pygame.K_UP:
                    player.move_up()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_right()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_left()
        camera.update(player)
        player.update()
        tiles_group.update()
        for sprite in all_sprites:
            camera.apply(sprite)

        if not pygame.sprite.collide_rect(player, purpose):
            screen.fill((209, 224, 27))
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
        else:
            all_sprites.empty()
            tiles_group.empty()
            player_group.empty()
            purpose_group.empty()
            enemy_group.empty()
            return

        pygame.display.flip()
        clock.tick(FPS)


def play_level_2():
    player, enemy1, enemy2, enemy3, cloud, purpose, x, y = generate_level_2(load_level('map2.txt'))
    global tiles_group, player_group, purpose_group, box_group, cloud_group
    font = pygame.font.Font(None, 35)
    font2 = pygame.font.Font(None, 30)
    text = font.render(player.updater(), True, (255, 255, 255))
    text2 = font2.render('Coords: 360 -2010', True, (255, 255, 255))
    text_rect = text.get_rect(center=(width / 2, 20))
    text_rect2 = text.get_rect(center=(width / 2.5, 50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.move_down()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_up()
                    text = font.render(player.updater(), True, (255, 255, 255))
                elif event.key == pygame.K_UP:
                    player.move_up()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_down()
                    text = font.render(player.updater(), True, (255, 255, 255))
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_right()
                    text = font.render(player.updater(), True, (255, 255, 255))
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_left()
                    text = font.render(player.updater(), True, (255, 255, 255))
        enemy_group.update()
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        if not pygame.sprite.groupcollide(player_group, enemy_group, False, False):
            gameover = pygame.transform.scale(load_image('dead.png'), size)
            screen.blit(gameover, (0, 0))
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
            cloud_group.draw(screen)
            screen.blit(text, text_rect)
            screen.blit(text2, text_rect2)
        else:
            gameover = pygame.transform.scale(load_image('dead.png'), size)
            screen.blit(gameover, (0, 0))
            all_sprites.empty()
            tiles_group.empty()
            player_group.empty()
            purpose_group.empty()
            enemy_group.empty()
            cloud_group.empty()
            running = False

        if not pygame.sprite.collide_rect(player, purpose):
            gameover = pygame.transform.scale(load_image('dead.png'), size)
            screen.blit(gameover, (0, 0))
            cloud_group.draw(screen)
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
            cloud_group.draw(screen)
            screen.blit(text, text_rect)
            screen.blit(text2, text_rect2)
        else:
            cloud_group.empty()
            all_sprites.empty()
            tiles_group.empty()
            player_group.empty()
            purpose_group.empty()
            enemy_group.empty()
            return True

        pygame.display.flip()
        clock.tick(FPS)
    pygame.time.wait(3000)
    return False


def play_level_3():
    player, purpose, enemy1, enemy2, x, y = generate_level_3(load_level('map3.txt'))

    counter = 30
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    font = pygame.font.SysFont(None, 32)
    font2 = pygame.font.Font(None, 35)
    font3 = pygame.font.Font(None, 30)
    text = font.render(f"Time: {str(counter)}", True, (255, 255, 255))
    text2 = font2.render(player.updater(), True, (255, 255, 255))
    text3 = font3.render('Coords: 570 1320', True, (255, 255, 255))
    text_rect = text2.get_rect(center=(width / 2, 20))
    text_rect2 = text3.get_rect(center=(width / 2, 50))

    global tiles_group, player_group, purpose_group, box_group
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.move_down()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_up()
                    text2 = font2.render(player.updater(), True, (255, 255, 255))
                elif event.key == pygame.K_UP:
                    player.move_up()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_down()
                    text2 = font2.render(player.updater(), True, (255, 255, 255))
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_right()
                    text2 = font2.render(player.updater(), True, (255, 255, 255))
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    if pygame.sprite.spritecollide(player, box_group, False, pygame.sprite.collide_mask):
                        player.move_left()
                    text2 = font2.render(player.updater(), True, (255, 255, 255))
            elif event.type == timer_event:
                counter -= 1
                text = font.render(f"Time: {str(counter)}", True, (255, 255, 255))
                if counter == 0:
                    all_sprites.empty()
                    tiles_group.empty()
                    player_group.empty()
                    purpose_group.empty()
                    enemy_group.empty()
                    pygame.time.set_timer(timer_event, 0)
                    # text = font.render(f"Time: {str(counter)}", True, (255, 255, 255))
                    # text2 = font2.render(player.updater(), True, (255, 255, 255))
                    # text3 = font3.render(player.updater(), True, (255, 255, 255))
                    running = False

        enemy_group.update()
        camera.update(player)
        player.update()
        for sprite in all_sprites:
            camera.apply(sprite)

        if not pygame.sprite.groupcollide(player_group, enemy_group, False, False):
            gameover = pygame.transform.scale(load_image('dead.png'), size)
            screen.blit(gameover, (0, 0))
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
            cloud_group.draw(screen)
            screen.blit(text, (6, 4))
            screen.blit(text2, text_rect)
            screen.blit(text3, text_rect2)
        else:
            gameover = pygame.transform.scale(load_image('dead.png'), size)
            screen.blit(gameover, (0, 0))
            pygame.time.set_timer(timer_event, 0)
            # text = font.renderf(f"Time: {str(counter)}", True, (255, 255, 255))
            # text2 = font2.render(player.updater(), True, (255, 255, 255))
            # text3 = font3.render(player.updater(), True, (255, 255, 255))
            all_sprites.empty()
            tiles_group.empty()
            player_group.empty()
            purpose_group.empty()
            enemy_group.empty()
            cloud_group.empty()
            running = False

        if not pygame.sprite.collide_rect(player, purpose):
            gameover = pygame.transform.scale(load_image('dead.png'), size)
            screen.blit(gameover, (0, 0))
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
            screen.blit(text, (6, 4))
            screen.blit(text2, text_rect)
            screen.blit(text3, text_rect2)
        else:
            all_sprites.empty()
            tiles_group.empty()
            player_group.empty()
            purpose_group.empty()
            enemy_group.empty()
            return True

        pygame.display.flip()
        clock.tick(FPS)

    pygame.time.wait(3000)
    return False


# группы:
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
purpose_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
horizontal_group = pygame.sprite.Group()
vertical_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()


def generate_level(level):
    global tiles_group, player_group, purpose_group

    new_player, new_purpose, x, y = None, None, None, None

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_player = Player('animations/player/cat1/', x, y, player_group)
            elif level[y][x] == '+':
                Tile('grass', x, y, tiles_group)
            elif level[y][x] == '!':
                new_purpose = Balloon('animations/balloons/balloon3/', x, y, tiles_group)
            elif level[y][x] == '_':
                Cat('animations/cats/cat1/', x, y, tiles_group)
            elif level[y][x] == '-':
                Cat('animations/cats/cat2/', x, y, tiles_group)
            elif level[y][x] == ')':
                Cat('animations/cats/cat3/', x, y, tiles_group)
            elif level[y][x] == '(':
                Cat('animations/cats/cat4/', x, y, tiles_group)
            elif level[y][x] == '[':
                Cat('animations/cats/cat5/', x, y, tiles_group)
            elif level[y][x] == ']':
                Cat('animations/cats/cat6/', x, y, tiles_group)
            elif level[y][x] == '1':
                Tile('tent1', x, y, tiles_group)
            elif level[y][x] == '2':
                Tile('tent2', x, y, tiles_group)
            elif level[y][x] == '3':
                Balloon('animations/balloons/balloon1/', x, y, tiles_group)
            elif level[y][x] == '4':
                Balloon('animations/balloons/balloon2/', x, y, tiles_group)
            elif level[y][x] == 'a':
                Tile('wall', x, y, tiles_group)
            elif level[y][x] == 'b':
                Tile('wall2', x, y, tiles_group)
            elif level[y][x] == 'c':
                Tile('wall3', x, y, tiles_group)
            elif level[y][x] == 'd':
                Tile('wall4', x, y, tiles_group)

    return new_player, new_purpose, x, y


def generate_level_2(level):
    global tiles_group, player_group, purpose_group, enemy_group, cloud_group

    new_player, new_enemy1, new_enemy2, new_enemy3, cloud, new_purpose, x, y = None, None, None, None, None, None, None, \
        None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '!':
                new_purpose = Purpose('purpose', x, y, purpose_group)
            elif level[y][x] == '@':
                new_player = Player2(x, y, player_group)
            elif level[y][x] == '-':
                new_enemy1 = Enemy('enemy1', x, y, enemy_group)
            elif level[y][x] == '?':
                new_enemy2 = Enemy('enemy2', x, y, enemy_group)
            elif level[y][x] == '*':
                new_enemy3 = Enemy('enemy3', x, y, enemy_group)
            elif level[y][x] == '+':
                Tile('sky', x, y, tiles_group)
            elif level[y][x] == '$':
                Cloud(x, y, cloud_group)
            elif level[y][x] == '1':
                Tile('wall5', x, y, tiles_group)
            elif level[y][x] == '2':
                Tile('wall6', x, y, tiles_group)
            elif level[y][x] == '3':
                Tile('wall7', x, y, tiles_group)
            elif level[y][x] == '4':
                Tile('wall8', x, y, tiles_group)

    return new_player, new_enemy1, new_enemy2, new_enemy3, cloud, new_purpose, x, y


def generate_level_3(level):
    global tiles_group, player_group, purpose_group, enemy_group

    new_player, new_purpose, new_enemy1, new_enemy2, x, y = None, None, None, None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '+':
                Tile('the_moon', x, y, tiles_group)
            elif level[y][x] == '!':
                new_purpose = Purpose('purpose2', x, y, purpose_group)
            elif level[y][x] == '@':
                new_player = Player('animations/player/cat2/', x, y, player_group)
            elif level[y][x] == '5':
                Tile('wall9', x, y, tiles_group)
            elif level[y][x] == '6':
                Tile('wall10', x, y, tiles_group)
            elif level[y][x] == '7':
                Tile('wall11', x, y, tiles_group)
            elif level[y][x] == '8':
                Tile('wall12', x, y, tiles_group)
            elif level[y][x] == 'a':
                Tile('crater1', x, y, tiles_group)
            elif level[y][x] == 's':
                Tile('crater2', x, y, tiles_group)
            elif level[y][x] == 'd':
                Tile('crater3', x, y, tiles_group)
            elif level[y][x] == 'f':
                Tile('crater4', x, y, tiles_group)
            elif level[y][x] == 'g':
                Tile('crater5', x, y, tiles_group)
            elif level[y][x] == 'h':
                Tile('crater6', x, y, tiles_group)
            elif level[y][x] == 'j':
                Tile('crater7', x, y, tiles_group)
            elif level[y][x] == 'k':
                Tile('crater8', x, y, tiles_group)
            elif level[y][x] == 'l':
                Tile('crater9', x, y, tiles_group)
            elif level[y][x] == 'q':
                new_enemy1 = Enemy('metheor1', x, y, enemy_group)
            elif level[y][x] == 'w':
                new_enemy2 = Enemy('metheor2', x, y, enemy_group)
    return new_player, new_purpose, new_enemy1, new_enemy2, x, y


pygame.init()

size = width, height = 650, 550
screen = pygame.display.set_mode(size, 0, 32)

cloud_image = load_image('cloud.png')

tile_images = {
    'wall': load_image('side1.png'),
    'wall2': load_image('side2.png'),
    'wall3': load_image('side3.png'),
    'wall4': load_image('side4.png'),
    'tent1': load_image('tent1.png'),
    'tent2': load_image('tent2.png'),
    'grass': load_image('grass.png'),
    'sky': load_image('sky.png'),
    'wall5': load_image('sider1.png'),
    'wall6': load_image('sider2.png'),
    'wall7': load_image('sider3.png'),
    'wall8': load_image('sider4.png'),
    'the_moon': load_image('the_moon.png'),
    'crater1': load_image('crater1.png'),
    'crater2': load_image('crater2.png'),
    'crater3': load_image('crater3.png'),
    'crater4': load_image('crater4.png'),
    'crater5': load_image('crater5.png'),
    'crater6': load_image('crater6.png'),
    'crater7': load_image('crater7.png'),
    'crater8': load_image('crater8.png'),
    'crater9': load_image('crater9.png'),
    'wall9': load_image('mooner1.png'),
    'wall10': load_image('mooner2.png'),
    'wall11': load_image('mooner3.png'),
    'wall12': load_image('mooner4.png'),
}

purpose_image = {
    'purpose': load_image('purpose2.png'),
    'purpose2': load_image('purpose3.png')
}

player_image = load_image('airballon.png')

enemy_image = {
    'enemy1': load_image('enemy1.png'),
    'enemy2': load_image('enemy2.png'),
    'enemy3': load_image('enemy3.png'),
    'metheor1': load_image('metheor1.png'),
    'metheor2': load_image('metheor2.png')
}

tile_width = tile_height = 50

clock = pygame.time.Clock()
camera = Camera()

while True:
    start_screen()

    pygame.mixer.music.load("sounds/1-1.mp3")
    pygame.mixer.music.play(-1, start=0.0, fade_ms=1000)
    pygame.mixer.music.set_volume(0.7)
    comics('first.png')
    play_level()
    pygame.mixer.music.stop()

    pygame.mixer.music.load("sounds/2-1.mp3")
    pygame.mixer.music.play(-1, start=0.0, fade_ms=1000)
    pygame.mixer.music.set_volume(2.0)
    comics('second.png')
    level2 = False
    while not level2:
        level2 = play_level_2()
    comics('third.png')
    pygame.mixer.music.stop()

    pygame.mixer.music.load("sounds/8-1.mp3")
    pygame.mixer.music.play(-1, start=0.0, fade_ms=10)
    comics('fourth.png')
    comics('fifth.png')
    level3 = False
    while not level3:
        level3 = play_level_3()
    comics('sixth.png')
    comics('seventh.png')
    pygame.mixer.music.stop()
