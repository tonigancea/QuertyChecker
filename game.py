import pygame
import sys
import os

LATIME = 800
INALTIME = 400

#IMPORT PICS

script_dir = os.path.dirname(__file__)

abs_start_path = os.path.join(script_dir, 'start.png')
start = pygame.image.load(abs_start_path)

abs_time3_path = os.path.join(script_dir, 'time3.png')
time3 = pygame.image.load(abs_time3_path)

abs_time2_path = os.path.join(script_dir, 'time2.png')
time2 = pygame.image.load(abs_time2_path)

abs_time1_path = os.path.join(script_dir, 'time1.png')
time1 = pygame.image.load(abs_time1_path)

abs_info_path = os.path.join(script_dir, 'info.png')
info = pygame.image.load(abs_info_path)

abs_info2_path = os.path.join(script_dir, 'info2.png')
info2 = pygame.image.load(abs_info2_path)

abs_yay_path = os.path.join(script_dir, 'yay.png')
yay = pygame.image.load(abs_yay_path)

abs_credits_path = os.path.join(script_dir, 'credits.png')
credits = pygame.image.load(abs_credits_path)

abs_continue_path = os.path.join(script_dir, 'continue.png')
continue_game = pygame.image.load(abs_continue_path)

abs_bonus_path = os.path.join(script_dir, 'bonus.png')
bonus = pygame.image.load(abs_bonus_path)

#ALEGERE CULORI

ALB = (230, 230, 230)
NEGRU = (36, 36, 36)
GRI = (127, 127, 127)
CULOARE_ELEMENTE = (155, 229, 112)
WRONG = (100, 0, 0)
RIGHT = (155, 229, 112)

#TITLE AND SIZE

ecran = pygame.display.set_mode((LATIME, INALTIME))
pygame.display.set_caption("Querty Checker")


fundal = pygame.Surface((LATIME, INALTIME))
fundal = fundal.convert()
fundal.fill(ALB)

#START

ecran.blit(start, (0, 0))
pygame.display.flip()
pygame.time.wait(3000)

#JOCUL INCEPE

ecran.blit(time3, (0, 0))
pygame.display.flip()
pygame.time.wait(1000)

ecran.blit(time2, (0, 0))
pygame.display.flip()
pygame.time.wait(1000)

ecran.blit(time1, (0, 0))
pygame.display.flip()
pygame.time.wait(1000)

#INFO

ecran.blit(info, (0, 0))
pygame.display.flip()
pygame.time.wait(5000)

merge_info = True

while merge_info:
	#CHECK FOR EXIT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	taste_apasate = pygame.key.get_pressed()
	
	if taste_apasate[pygame.K_RETURN]:
		break
	
	ecran.blit(info2, (0, 0))
	pygame.display.flip()
	

merge = True

while merge:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#CONDITII TASTE APASATE
	taste_apasate = pygame.key.get_pressed()
	
	if taste_apasate[pygame.K_2] and taste_apasate[pygame.K_r] and taste_apasate[pygame.K_d] and taste_apasate[pygame.K_z]:
		break
	
	if taste_apasate[pygame.K_1]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(0, 0, 100, 100))
	if taste_apasate[pygame.K_2]:
		pygame.draw.rect(fundal, RIGHT, pygame.Rect(100, 0, 100, 100))
	if taste_apasate[pygame.K_3]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(200, 0, 100, 100))
	if taste_apasate[pygame.K_4]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(300, 0, 95, 100))

	if taste_apasate[pygame.K_q]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(0, 100, 100, 100))
	if taste_apasate[pygame.K_w]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(100, 100, 100, 100))
	if taste_apasate[pygame.K_e]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(200, 100, 100, 100))
	if taste_apasate[pygame.K_r]:
		pygame.draw.rect(fundal, RIGHT, pygame.Rect(300, 100, 95, 100))
		
	if taste_apasate[pygame.K_a]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(0, 200, 100, 100))
	if taste_apasate[pygame.K_s]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(100, 200, 100, 100))
	if taste_apasate[pygame.K_d]:
		pygame.draw.rect(fundal, RIGHT, pygame.Rect(200, 200, 100, 100))
	if taste_apasate[pygame.K_f]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(300, 200, 95, 100))
		
	if taste_apasate[pygame.K_z]:
		pygame.draw.rect(fundal, RIGHT, pygame.Rect(0, 300, 100, 100))
	if taste_apasate[pygame.K_x]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(100, 300, 100, 100))
	if taste_apasate[pygame.K_c]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(200, 300, 100, 100))
	if taste_apasate[pygame.K_v]:
		pygame.draw.rect(fundal, WRONG, pygame.Rect(300, 300, 95, 100))

	pygame.display.flip()
	ecran.blit(fundal, (0, 0))
	
	#DESENARE FUNDAL
	
	#LINIA 1
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(0, 0, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(200, 0, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(400, 0, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(600, 0, 100, 100))
	
	pygame.draw.rect(fundal, ALB, pygame.Rect(100, 0, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(300, 0, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(500, 0, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(700, 0, 100, 100))
	
	#LINIA 2
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(100, 100, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(300, 100, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(500, 100, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(700, 100, 100, 100))
	
	pygame.draw.rect(fundal, ALB, pygame.Rect(0, 100, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(200, 100, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(400, 100, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(600, 100, 100, 100))
	
	#LINIA 3
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(0, 200, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(200, 200, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(400, 200, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(600, 200, 100, 100))
	
	pygame.draw.rect(fundal, ALB, pygame.Rect(100, 200, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(300, 200, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(500, 200, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(700, 200, 100, 100))
	
	#LINIA 4
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(100, 300, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(300, 300, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(500, 300, 100, 100))
	pygame.draw.rect(fundal, NEGRU, pygame.Rect(700, 300, 100, 100))
	
	pygame.draw.rect(fundal, ALB, pygame.Rect(0, 300, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(200, 300, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(400, 300, 100, 100))
	pygame.draw.rect(fundal, ALB, pygame.Rect(600, 300, 100, 100))
	
	
	#LINIE DEMARCATIE
	pygame.draw.rect(fundal, CULOARE_ELEMENTE, pygame.Rect(395, 0, 10, 400))
	
	#ELEMETE
	pygame.draw.circle(fundal, CULOARE_ELEMENTE, (550, 50), 25)
	pygame.draw.circle(fundal, CULOARE_ELEMENTE, (450, 350), 25)
	pygame.draw.circle(fundal, CULOARE_ELEMENTE, (750, 150), 25)
	pygame.draw.circle(fundal, CULOARE_ELEMENTE, (650, 250), 25)
	
merge2 = True

while merge2:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	ecran.blit(yay, (0, 0))
	pygame.display.flip()
	pygame.time.wait(5000)
	
	merge3 = True
	while merge3:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		#CONDITII TASTE APASATE 2
		taste_apasate2 = pygame.key.get_pressed()
	
		if taste_apasate2[pygame.K_ESCAPE]:
				
				#CREDITS
				ecran.blit(credits, (0, 0))
				pygame.display.flip()
				pygame.time.wait(5000)
				
				#EXIT
				pygame.quit()
				sys.exit()
				
		if taste_apasate2[pygame.K_m]:
				
				#BONUS
				ecran.blit(bonus, (0, 0))
				pygame.display.flip()
				pygame.time.wait(6000)
				
				#CREDITS
				ecran.blit(credits, (0, 0))
				pygame.display.flip()
				pygame.time.wait(5000)
				
				#EXIT
				pygame.quit()
				sys.exit()
				
		pygame.display.flip()
		ecran.blit(continue_game, (0, 0))