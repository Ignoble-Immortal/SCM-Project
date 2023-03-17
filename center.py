import pygame
from sys import exit#Basically AllCommand of python
from random import randint
pygame.init()#Initializes all of pygame

#Intro
player_stand=pygame.image.load('Graphics\Player\stand1.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

game_name=text_font.render('Vader',False,'Red')
game_name_rect=game_name.get_rect(center=(400,80))

game_message=text_font.render('Press space to run',False,'Red')
game_message_rect=game_message.get_rect(center=(400,320))
