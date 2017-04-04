import pygame
from time import sleep

num = int(input("Enter a number of seconds. \n>>"))

pygame.display.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load("COWS.mp3")
pygame.mixer.music.play()

img = pygame.image.load("pic.png")
img = pygame.transform.scale(img, (300,300))

font = pygame.font.SysFont("trebuchetms", 40)
intro = font.render("Seconds left:", 1, (0, 0, 0))
label = font.render("Time's up!", 1, (255,0,0))

screen = pygame.display.set_mode((400, 400))
screen.fill([100, 255, 100])

while 1:
	screen.fill([100, 255, 100])
	screen.blit(intro, (1, 1))
	screen.blit(img, (30,100))
	seconds = font.render(str(num), 1, (0, 0, 0))
	screen.blit(seconds, (100, 40))
	pygame.display.update()
	pygame.display.flip()
	
	num-=1
	sleep(1)

	if num == 0:
		pygame.mixer.music.stop()
		screen.fill([100, 255, 100])
		screen.blit(img, (30, 100))
		screen.blit(label, (100, 40))
		pygame.display.update()
		break
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

while(1):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()