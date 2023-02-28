import pygame
import random
import os

pygame.init()

screen = pygame.display.set_mode((500,1000))
	
def main():
	land=pygame.image.load('mainland.png')
	land2=pygame.image.load('mainland.png')
	land3=pygame.image.load('mainland.png')
	trees=[pygame.image.load('tree.png'),pygame.image.load('stree.png'),pygame.image.load('bigtree.png')]

	dino=(pygame.image.load('dinosour.png'),pygame.image.load('dinosour1.png'))
	landx=0

	treex=1000
	treex2=1200
	treex3=1400
	treex4=1600
	dino_x=100
	dino_y=690
	d=0
	dd=1
	try:
		hI=open('highscore.txt','r')
		hi=hI.read()
	except :
		hi=0
	
	jump=False
	v=[4,5,4,4,4,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0]
	
	
	m=0
	neg=-1
	p=1
	fps=90
	fpsclock=pygame.time.Clock()
	treex_=750
	
	rdm=random.randint(-50,40)
	rdm2=random.randint(200,400)
	
	li=[]	
	def treeloop():
		for i in range(0,2):
			tx=random.randint(0,2)
			li.append(tx)	
			print(li)
	treeloop()
	
	li2=[]	
	def treeloop2():
		for i in range(0,2):
			tx2=random.randint(0,2)
			li2.append(tx2)	
	treeloop2()
	print(li2)
	li3=[]	
	def treeloop3():
		for i in range(0,1):
			tx3=random.randint(0,2)
			li3.append(tx3)	
	treeloop3()
	
	li4=[]	
	def treeloop4():
		for i in range(0,1):
			tx4=random.randint(0,2)
			li4.append(tx4)	
	treeloop4()
	
	global score
	score=0
	change=2
	aaa=0

	font=pygame.font.Font('freesansbold.ttf',20)
	game_over=False
	scorechange=1/12
	pause=False
	collision=False
	treey=676
	high_score=font.render('hI:'+str(hi),True,(0,0,0))	
	newhi=font.render('NEW HIGH SCORE',True,(255,0,0))

	def A_tree():
		
			screen.blit(trees[li[0]],(treex,treey))
	def B_tree():
			screen.blit(trees[li2[0]],(treex2,treey))
	def C_tree():
			screen.blit(trees[li3[0]],(treex3,treey))
	def D_tree():
			screen.blit(trees[li4[0]],(treex4,treey))
			
	
			
	def dinoimg():
	
		screen.blit(dino[x],(dino_x,dino_y))
	
	def mainland():
		
		screen.blit(land,(landx,700))	
		screen.blit(land2,(land2_x,700))
		screen.blit(land3,(land3_x,700))	
	
	def score_num():
			screen.blit(text,(200,200))	
			
	def gameover():
		screen.blit(game_o,(200,500))
	def high_s():
		screen.blit(high_score,(10,300))	
	
			
	running=True
	
	while running:
		fpsclock.tick(fps)
		
		score+=scorechange
			
				
		treex-=change
		treex2-=change
		treex3-=change
		treex4-=change
				
		landx-=change
				
		d+=1
				#for land
		land2_x=landx+520
		land3_x=land2_x+520
			
		if land2_x == 0:
				landx=0
					
				#for trees
			
				
		treex2_=treex_+rdm
		treex3_=treex2_+rdm2
		
		
	
	
		screen.fill((255,255,255))
		
		text=font.render('score:'+str(int(score)),True,(0,0,0))
		

					
		if not(pause):
			if jump:
				
				m += p
				r=v[m]
			
				yj=neg*r
				dino_y += yj
		if m>36:
			p= -1
			neg= 1	
		if m<=0:
			jump=False
			m=0
			neg= -1	
			p=1
			dino_y=690
			
		if d>=19:
			d=-1
		x=d //10	
	
		A_tree()
		B_tree()
		C_tree()
		D_tree()
		#tree repeator
		if treex<-70:
			treex=800
			li.clear()
			treeloop()
		if treex2<-70:
			treex2=800
			li2.clear()
			treeloop2()
		if treex3<-70:
			treex3=800
			li3.clear()
			treeloop3()
		if treex4<-70:
			treex4=800
			li4.clear()
			treeloop4()
		
			
		game_o=font.render('GAME OVER\n score:'+str(int(score)),True,(0,0,0))
		
		if collision:
			gameover()
			if int(score)>int(hi):
				screen.blit(newhi,(240,600))
			game_over=True
			
		
		if game_over:
			change=0
			scorechange=0		
			d=0
			pause=True
		
		#collision detector
		if dino_x > treex-20 and dino_x < treex+44 and dino_y > treey:
			collision=True
		if dino_x > treex2-20 and dino_x < treex2+44 and dino_y > treey:
			collision=True
		if dino_x > treex3-20 and dino_x < treex3+44 and dino_y > treey:
			collision=True
		if dino_x > treex4-20 and dino_x < treex4+44 and dino_y > treey:
			collision=True	
		
		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				running=False
				pygame.quit()
				
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_SPACE:
					jump=True
					if game_over:
						score_saved=score
						print(score_saved)
						if score_saved > int(hi) :
							file=open('highscore.txt','w')
							file.write(str(int(score_saved)))
							file.close()
						main()
					
		score_num()
		high_s()
		dinoimg()
		mainland()
	
		pygame.display.update()	



main()


