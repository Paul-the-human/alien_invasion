import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


class Test:
    param = 1
    param2 = 3


class Test2:
    a = "bruce_lee"


def test1():
    a = Test()
    a.param2 = 2
    return a.param


def run_game():
    # Инициализирует игру и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
