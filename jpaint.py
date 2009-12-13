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

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Jpaint")
screen.fill(white);

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
			if event.key == pygame.K_f:
				radius = 40
				screen = pygame.display.set_mode((1020,760), FULLSCREEN)
				screen.fill(white)
			if event.key == K_d:
				radius = 25
				screen = pygame.display.set_mode((640,480))
				screen.fill(white)
			if event.key == K_c:
				screen.fill(white)
				font = pygame.font.Font(None, 100)
				text = font.render("Author: Joel", 1, black)
				textpos = text.get_rect()
				textpos.centerx = screen.get_rect().centerx
				textpos.centery = screen.get_rect().centery
				screen.blit(text, textpos)
				
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
