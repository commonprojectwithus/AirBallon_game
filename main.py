import random

import pygame
import os
import sys

FPS = 60
all_sprites = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join(name)
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
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tiles_group):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

        if tile_type == 'wall':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'clouds':
            self.add(cloud_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)

        elif tile_type == 'wall_2':
            self.add(box_group, tiles_group, all_sprites)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
        else:
            self.add(tiles_group, all_sprites)


class Purpose(pygame.sprite.Sprite):
    def __init__(self, purpose_type, pos_x, pos_y, purpose_group):
        super().__init__(purpose_group, all_sprites)
        self.image = purpose_image[purpose_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, player_type, pos_x, pos_y, player_group):
        super().__init__(player_group, all_sprites)
        self.image = player_image[player_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def move_down(self):
        self.rect = self.rect.move(0, +30)

    def move_up(self):
        self.rect = self.rect.move(0, -30)

    def move_right(self):
        self.rect = self.rect.move(+30, 0)

    def move_left(self):
        self.rect = self.rect.move(-30, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, enemy_group):
        super().__init__(enemy_group, all_sprites)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, mov):
        pass


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


# группы:
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
purpose_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()


def generate_level(level):
    global tiles_group, player_group, purpose_group

    new_player, new_purpose, x, y = None, None, None, None

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_player = Player('player', x, y, player_group)
            elif level[y][x] == '+':
                Tile('grass', x, y, tiles_group)
            elif level[y][x] == '!':
                new_purpose = Purpose('purpose', x, y, purpose_group)

            # elif level[y][x] == '#':
            #     Tile('wall', x, y, tiles_group)

    return new_player, new_purpose, x, y


def generate_level_2(level):
    global tiles_group, player_group, purpose_group, enemy_group, cloud_group

    new_player, new_enemy, new_purpose, x, y = None, None, None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '!':
                new_purpose = Purpose('purpose2', x, y, purpose_group)
            elif level[y][x] == '@':
                new_player = Player('player2', x, y, player_group)
            elif level[y][x] == '+':
                Tile('sky', x, y, tiles_group)
                Tile('clouds', x, y, tiles_group)

            # elif level[y][x] == '#':
            #     Tile('wall', x, y, tiles_group)
    return new_player, new_enemy, new_purpose, x, y


def generate_level_3(level):
    global tiles_group, player_group, purpose_group, enemy_group

    new_player, new_purpose, x, y = None, None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '+':
                Tile('the_moon', x, y, tiles_group)
            elif level[y][x] == '!':
                new_purpose = Purpose('purpose3', x, y, purpose_group)
            elif level[y][x] == '@':
                new_player = Player('player3', x, y, player_group)
            # elif level[y][x] == '#':
            #     Tile('wall', x, y, tiles_group)
    return new_player, new_purpose, x, y


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
                    if pygame.sprite.spritecollideany(player, box_group):
                        player.move_up()
                elif event.key == pygame.K_UP:
                    player.move_up()
                    if pygame.sprite.spritecollideany(player, box_group):
                        player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    if pygame.sprite.spritecollideany(player, box_group):
                        player.move_right()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    if pygame.sprite.spritecollideany(player, box_group):
                        player.move_left()

        camera.update(player)
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

        # if not pygame.sprite.groupcollide(player_group, enemy_group, False, False):
        #     screen.fill((0, 0, 0))
        #     all_sprites.draw(screen)
        #     tiles_group.draw(screen)
        #     player_group.draw(screen)
        #     purpose_group.draw(screen)
        #     enemy_group.draw(screen)
        # else:
        #     gameover = pygame.transform.scale(load_image('dead.jpg'), size)
        #     screen.blit(gameover, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)


def play_level_2():

    player, enemy, purpose, x, y = generate_level_2(load_level('map2.txt'))

    global tiles_group, player_group, purpose_group, box_group, cloud_group
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
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_up()
                elif event.key == pygame.K_UP:
                    player.move_up()
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_right()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_left()

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        if not pygame.sprite.collide_rect(player, purpose):
            screen.fill((191, 194, 193))
            cloud_group.draw(screen)
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
        else:
            cloud_group.empty()
            all_sprites.empty()
            tiles_group.empty()
            player_group.empty()
            purpose_group.empty()
            enemy_group.empty()
            return

        if not pygame.sprite.groupcollide(player_group, enemy_group, False, False):
            screen.fill((191, 194, 193))
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            purpose_group.draw(screen)
            enemy_group.draw(screen)
        else:
            gameover = pygame.transform.scale(load_image('dead.jpg'), size)
            screen.blit(gameover, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)


def play_level_3():
    player, purpose, x, y = generate_level_3(load_level('map3.txt'))

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
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_up()
                elif event.key == pygame.K_UP:
                    player.move_up()
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_right()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    # if pygame.sprite.spritecollideany(player, box_group):
                    #     player.move_left()

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        if not pygame.sprite.collide_rect(player, purpose):
            screen.fill((150, 159, 170))
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

        # if not pygame.sprite.groupcollide(player_group, enemy_group, False, False):
        #     screen.fill((191, 194, 193))
        #     all_sprites.draw(screen)
        #     tiles_group.draw(screen)
        #     player_group.draw(screen)
        #     purpose_group.draw(screen)
        #     enemy_group.draw(screen)
        # else:
        #     gameover = pygame.transform.scale(load_image('dead.jpg'), size)
        #     screen.blit(gameover, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size, 0, 32)

tile_images = {
    'wall': load_image('tree.png'),
    'grass': load_image('grass.png'),
    'clouds': load_image('cloud.png'),
    'sky': load_image('sky.png'),
    'empty5': load_image('sky1.png'),
    'the_moon': load_image('the_moon.png')
}

player_image = {
    'player': load_image('cat.png'),
    'player2': load_image('airballon.png'),
    'player3': load_image('cat2.png')
}

enemy_image = load_image('enemy1.png')

purpose_image = {
    'purpose': load_image('purpose1.png'),
    'purpose2': load_image('purpose2.png'),
    'purpose3': load_image('purpose3.png')
}

tile_width = tile_height = 50

clock = pygame.time.Clock()
camera = Camera()

while True:
    start_screen()
    play_level()
    play_level_2()
    play_level_3()


