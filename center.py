import pygame
from sys import exit#Basically AllCommand of python
from random import randint
pygame.init()#Initializes all of pygame

def display_score():
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    score_surf=text_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect=score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5

            if obstacle_rect.bottom==300: screen.blit(snail_surf,obstacle_rect)
            else: screen.blit(fly_surf,obstacle_rect)
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

#Big Surface
sky_surface=pygame.image.load('Graphics\sky1.png').convert()
ground_surface=pygame.image.load('Graphics\ground1.png').convert()

#Mob
snail1=pygame.image.load('Graphics\Snail\snail1.png').convert_alpha()
snail2=pygame.image.load('Graphics\Snail\snail2.png').convert_alpha()
snail_frames=[snail1,snail2]
snail_index=0
snail_surf=snail_frames[snail_index]

fly1=pygame.image.load('Graphics\Fly\Fly1.png').convert_alpha()
fly2=pygame.image.load('Graphics\Fly\Fly2.png').convert_alpha()
fly_frames=[fly1,fly2]
fly_index=0
fly_surf=fly_frames[fly_index]

obstacle_rect_list=[]
#Player
player_walk1=pygame.image.load('Graphics\Player\walk1.png').convert_alpha()
player_walk2=pygame.image.load('Graphics\Player\walk2.png').convert_alpha()
player_walk=[player_walk1,player_walk2]
player_index=0
player_jump=pygame.image.load('Graphics\Player\jump1.png').convert_alpha()
player_surf=player_walk[player_index]
player_rect=player_surf.get_rect(midbottom=(80,300))
player_gravity=0
#Intro
player_stand=pygame.image.load('Graphics\Player\stand1.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

game_name=text_font.render('Vader',False,'Red')
game_name_rect=game_name.get_rect(center=(400,80))

game_message=text_font.render('Press space to run',False,'Red')
game_message_rect=game_message.get_rect(center=(400,320))

#timer
obstacle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer,200)

