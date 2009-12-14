# Program: Jpaint
# Author: Joel Moore
# License: GPLv3
# Version: 1.3

import pygame
from pygame.locals import *
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
userColor = (0,0,0)
go = True
draw = False
erase = False
radius = 25
color = black
(rx,ry) = (0,25)
(gx,gy) = (0,60)
(bx,by) = (0,95)
fileType = '.jpg'
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Jpaint")
screen.fill(white)

while go == True:
    for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				color = black
			if event.key == pygame.K_LEFT:
				color = red
			if event.key == pygame.K_UP:
				color = green
			if event.key == pygame.K_RIGHT:
				color = blue
			if event.key == K_c:
				screen.fill(white)
				font = pygame.font.Font(None, 100)
				text = font.render("Author: Joel", 1, black)
				textpos = text.get_rect()
				textpos.centerx = screen.get_rect().centerx
				textpos.centery = screen.get_rect().centery
				screen.blit(text, textpos)
			if event.key == K_s:
				saveName = raw_input('Save file: ')
				pygame.image.save(screen,saveName + fileType)
			if event.key == K_l:
				loadName = raw_input('Load file: ')
				userImage = pygame.sprite.Sprite()
				userImage.image = pygame.image.load(loadName + fileType).convert()
				userImage.rect = userImage.image.get_rect()
				userImage.rect.center = (640/2,481/2)
				screen.blit(userImage.image, userImage.rect)
				pygame.display.update()
				
		if pygame.mouse.get_pressed() == (1,0,0):
			(x,y) = pygame.mouse.get_pos()
			draw = True
			pygame.draw.circle(screen,color,(x,y),radius)

		if pygame.mouse.get_pressed() == (0,0,1):
			(x,y) = pygame.mouse.get_pos()
			erase = True
			pygame.draw.circle(screen,white,(x,y),radius)

		if pygame.mouse.get_pressed() == (0,1,0):
			screen.fill(white);

		if event.type == MOUSEBUTTONUP:
			draw = False
			erase = False

		if event.type == MOUSEMOTION:
			if draw:
				(x,y) = pygame.mouse.get_pos()
				pygame.draw.circle(screen,color,(x,y),radius)
				
		pygame.display.flip()

		if event.type == QUIT:
			go = False
