import os
import sys

import pygame

FPS = 100
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def terminate():
    pygame.quit()


sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_screen():
    intro_text = ["Home", "", "Правила игры",
                  "Ваша задача состоит в том, чтобы", "различным образом передвигать элементы",
                  "для получения комбинации из трёх одинаковых.",
                  # будут ли комбинации из большего количества?                  "После этого использованные фигуры исчезают,",
                  "а на их место падают верхние."]
    fon = pygame.transform.scale(load_image('fon1.jpg'), (width, height))
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


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.flip()
clock.tick(FPS)
