import pygame
import sys
from  pygame.sprite import Group

from src.settings import Mysettings
from src.ship import Ship
from src.alien import Alien
import src.game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Mysettings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    alien = Alien(ai_settings,screen)

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,alien,bullets)


run_game()
