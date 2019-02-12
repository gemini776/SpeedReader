#speedreader version 1.1

#setup

import pygame
import sys
import os
import time


pygame.font.init()
screen = pygame.display.set_mode((1000,800))
background = (0,0,0)
screen.fill((background))
myfont = pygame.font.Font(None, 125)

#main function
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		pygame.quit(); sys.exit()

if event.type == pygame.KEYDOWN:
	if event.key == ord('q'):
		pygame.quit()
		sys.exit()

f = open(r"/home/boss/Projects/speedread/textdrop.txt", encoding = 'utf-8')

for line in f:
	for word in line.split():
		text = myfont.render(word,1,(255,0,0))

		screen.blit(text, (100,300))
		pygame.display.update()

		#300 wpm
		time.sleep(0.2)
		screen.fill((background))
		pygame.display.update()

pygame.display.quit
