
import pygame
import math
import socket

class BoxesGame():
	

	def __init__(self):
		#pass
		#1

		pygame.init()
		self.score1=0
		#self.score_me=str(self.score1)
		self.score2=0
		#self.score_ot=str(self.score2)
		self.flip=1
		
		
		

		width, height = 420, 570
		
		self.boardh = [[False for x in range(7)] for y in range(7)]
		self.boardv = [[False for x in range(6)] for y in range(8)]
		#for x in range(7):
			#for y in range(6):
				#board[x][y]=0
		w, h = 6,7
		self.matrix = [[0 for x in range(w)] for y in range(h)]
		#for y in range(7):
			#for x in range(6):
				#self.matrix[y][x]=y+x
		#print(Matrix)
		#2
		
		#initialize the screen
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Boxes_by_rajat")
		#3
		self.initGraphics()
		#drawBoard()
		#4
		#initialize pygame clock
		self.clock=pygame.time.Clock()
		

	
	def initGraphics(self):
		self.normallinev=pygame.image.load("green.png")
		self.normallineh=pygame.transform.rotate(pygame.image.load("green.png"), -90)
		self.bar_donev=pygame.image.load("red.png")
		self.bar_doneh=pygame.transform.rotate(pygame.image.load("red.png"), -90)
		self.hoverlinev=pygame.image.load("yellow.png")
		self.hoverlineh=pygame.transform.rotate(pygame.image.load("yellow.png"), -90)
		self.your_turn=pygame.image.load("Your_Turn.png")
		self.me_red=pygame.image.load("me_red.png")
		self.me_yellow=pygame.image.load("me_yellow.png")
		self.me=pygame.image.load("light_pink.png")
		self.other=pygame.image.load("light_purple.png")
		self.back=pygame.image.load("purple.png")

	def drawBoard(self):
		for x in range(7):
			for y in range(7):
				if not self.boardh[y][x]:
					self.screen.blit(self.normallineh, [(x)*69, (y)*69+5])
				else:
					self.screen.blit(self.bar_doneh, [(x)*69, (y)*69+5])
			for x in range(6):
				for y in range(8):
					if not self.boardv[y][x]:
						self.screen.blit(self.normallinev, [(x)*69+5, (y)*69])
					else:
						self.screen.blit(self.bar_donev, [(x)*69+5, (y)*69])
		#game background and colored boxes
		for y in range(7):
			for x in range(6):
				#self.matrix[y][x]=y+x
				if self.matrix[y][x]==0:
					self.screen.blit(self.back,[(x)*69+6,(y)*69+6])
				elif self.matrix[y][x]==1:
					self.screen.blit(self.me,[(x)*69+6,(y)*69+6])
				elif self.matrix[y][x]==2:
					self.screen.blit(self.other,[(x)*69+6,(y)*69+6])

		

		self.score_me=str(self.score1)
		self.score_ot=str(self.score2)

		self.screen.blit(self.your_turn,[10,500])
		if self.flip==1:
			#self.screen.blit(self.me_red,[170,500])
			self.screen.blit(self.me_red,[7,540])     # here is the change 1
		elif self.flip==2:
			self.screen.blit(self.me_yellow,[175,540])
		#self.screen.blit(self.me_yellow,[170,500])
		font = pygame.font.Font(None,36)
		text = font.render("ME",1,(255,255,255))
		self.screen.blit(text,[36,542])
		text = font.render("ME ::",1,(10,10,240))
		self.screen.blit(text,[39,540])
		#score of mine
		text = font.render(self.score_me,1,(10,10,240))
		self.screen.blit(text,[105,540])
		
		text = font.render("OTHER",1,(255,255,255))
		self.screen.blit(text,[207,542])
		text = font.render("OTHER ::",1,(10,10,240))
		self.screen.blit(text,[210,540])
		#score of other player
		#text = font.render("20",1,(10,10,240))
		text = font.render(self.score_ot,1,(10,10,240))
		self.screen.blit(text,[327,540])


	def update(self):
		#sleep to make the game 60 fps
		self.clock.tick(60)
		#clear the screen
		self.screen.fill(0)
		self.drawBoard()
		#self.boardh[0][0]=True
		for event in pygame.event.get():
			#quit if the quit button was pressed
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				#print("button pressed")
				mouse=pygame.mouse.get_pos()
				if mouse[0]<=420 and mouse[1]<=488:
					mousex=mouse[0]//69
					mousey=mouse[1]//69
					self.buttonpressed(mouse,mousex,mousey)

		#update the screen
		
		mouse=pygame.mouse.get_pos()
		if mouse[0]<=420 and mouse[1]<=488:
			mousex=mouse[0]//69
			mousey=mouse[1]//69
			#print(mousex,mousey)
			#print(mouse)
			#gameover=0
			self.hoverover(mouse,mousex,mousey)		
		pygame.display.flip()
	
	def hoverover(self,mouse,mousex,mousey):
		#print(mouse[0]%69,mouse[1]%69)
		#print("hoverover")
		hovx=mouse[0]%69
		hovy=mouse[1]%69
		if hovx<5 and hovy>5:
			if self.boardh[mousey][mousex]==False:
				self.screen.blit(self.hoverlineh,[(mousex)*69,(mousey)*69+5])

		elif hovx>5 and hovy<5:
			if self.boardv[mousey][mousex]==False:
				self.screen.blit(self.hoverlinev,[(mousex)*69+5,(mousey)*69])
		elif hovx>5 and hovy>5:
			hovx-=37
			hovy-=37
			#if hovx>0 and hovy>0 and hovx<hovy:
			#	if self.boardv[mousey+1][mousex]==False:
			#		self.screen.blit(self.hoverlinev,[(mousex)*69+5,(mousey+1)*69])
			hovxx=hovx
			hovyy=hovy
			if hovx<0:
				hovxx=(-hovx)
			if hovy<0:
				hovyy=-hovy
			if hovxx<hovyy: #or hovx<(-hovy) or (-hovx)<(-hovy) or (-hovx)<(hovy):
				if (hovx>0 and hovy>0) or (hovx<0 and hovy>0):
					if self.boardv[mousey+1][mousex]==False:
						self.screen.blit(self.hoverlinev,[(mousex)*69+5,(mousey+1)*69])
				else:
					if self.boardv[mousey][mousex]==False:
						self.screen.blit(self.hoverlinev,[(mousex)*69+5,(mousey)*69])
			else:#if hovx>hovy or hovx>(-hovy) or (-hovx)>(-hovy) or (-hovx)>(hovy):
				if (hovx>0 and hovy>0) or (hovx>0 and hovy<0):
					if self.boardh[mousey][mousex+1]==False:
						self.screen.blit(self.hoverlineh,[(mousex+1)*69,(mousey)*69+5])
				else:
					if self.boardh[mousey][mousex]==False:
						self.screen.blit(self.hoverlineh,[(mousex)*69,(mousey)*69+5])
	
	
	def checkh(self,flip,mousey,mousex):
		#print(mousey,mousex)
		if mousex==0:
			#print(mousex)
			if self.boardh[mousey][mousex+1]==True and self.boardv[mousey][mousex]==True and self.boardv[mousey+1][mousex]==True:
				#print(self.boardh[mousey][mousex+1])
				#print(self.boardv[mousey][mousex])
				#print(self.boardv[mousey+1][mousex])
				if flip==1:
					self.matrix[mousey][mousex]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey][mousex]=2
					self.score2=self.score2+10
		elif mousex>0 and mousex<6:
			if self.boardh[mousey][mousex+1]==True and self.boardv[mousey][mousex]==True and self.boardv[mousey+1][mousex]==True:
				if flip==1:
					self.matrix[mousey][mousex]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey][mousex]=2
					self.score2=self.score2+10
			if self.boardh[mousey][mousex-1]==True and self.boardv[mousey][mousex-1]==True and self.boardv[mousey+1][mousex-1]==True:
				if flip==1:
					self.matrix[mousey][mousex-1]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey][mousex-1]=2
					self.score2=self.score2+10
		if mousex==6:
			#print(mousex)
			#print(self.boardh[mousey][mousex-1])
			#print(self.boardv[mousey][mousex-1])
			#print(self.boardv[mousey+1][mousex-1])
			if self.boardh[mousey][mousex-1]==True and self.boardv[mousey][mousex-1]==True and self.boardv[mousey+1][mousex-1]==True:
				
				if flip==1:
					self.matrix[mousey][mousex-1]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey][mousex-1]=2
					self.score2=self.score2+10
			
	def checkv(self,flip,mousey,mousex):
		#print(mousey,mousex)
		if mousey==0:
			#print(mousey)
			if self.boardv[mousey+1][mousex]==True and self.boardh[mousey][mousex]==True and self.boardh[mousey][mousex+1]==True:
				#print(self.boardh[mousey][mousex+1])
				#print(self.boardv[mousey][mousex])
				#print(self.boardv[mousey+1][mousex])
				if flip==1:
					self.matrix[mousey][mousex]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey][mousex]=2
					self.score2=self.score2+10
		elif mousey>0 and mousey<7:
			if self.boardv[mousey+1][mousex]==True and self.boardh[mousey][mousex]==True and self.boardh[mousey][mousex+1]==True:
				if flip==1:
					self.matrix[mousey][mousex]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey][mousex]=2
					self.score2=self.score2+10
			if self.boardv[mousey-1][mousex]==True and self.boardh[mousey-1][mousex]==True and self.boardh[mousey-1][mousex+1]==True:
				if flip==1:
					self.matrix[mousey-1][mousex]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey-1][mousex]=2
					self.score2=self.score2+10
		if mousey==7:
			#print(mousex)
			#print(self.boardh[mousey][mousex-1])
			#print(self.boardv[mousey][mousex-1])
			#print(self.boardv[mousey+1][mousex-1])
			if self.boardv[mousey-1][mousex]==True and self.boardh[mousey-1][mousex]==True and self.boardh[mousey-1][mousex+1]==True:
				
				if flip==1:
					self.matrix[mousey-1][mousex]=1
					self.score1=self.score1+10
				if flip==2:
					self.matrix[mousey-1][mousex]=2
					self.score2=self.score2+10

	def buttonpressed(self,mouse,mousex,mousey):
		#print(mouse[0]%69,mouse[1]%69)
		#print("hoverover")
		hovx=mouse[0]%69
		hovy=mouse[1]%69
		if hovx<5 and hovy>5:
			if self.boardh[mousey][mousex]==False:
				#print(mousey,mousex)
				self.boardh[mousey][mousex]=True
				if self.flip==1:
					self.score1=self.score1+1
					self.checkh(self.flip,mousey,mousex)
					self.flip=2
					#sqcheck(1,mousey,mousex)					
				elif self.flip==2:
					self.score2=self.score2+1
					self.checkh(self.flip,mousey,mousex)
					self.flip=1
				
		elif hovx>5 and hovy<5:
			if self.boardv[mousey][mousex]==False:
				self.boardv[mousey][mousex]=True
				#self.score1=self.score1+1
				if self.flip==1:
					self.score1=self.score1+1
					self.checkv(self.flip,mousey,mousex)
					self.flip=2
				elif self.flip==2:
					self.score2=self.score2+1
					self.checkv(self.flip,mousey,mousex)
					self.flip=1
				
		elif hovx>5 and hovy>5:
			hovx-=37
			hovy-=37
			#if hovx>0 and hovy>0 and hovx<hovy:
			#	if self.boardv[mousey+1][mousex]==False:
			#		self.screen.blit(self.hoverlinev,[(mousex)*69+5,(mousey+1)*69])
			hovxx=hovx
			hovyy=hovy
			if hovx<0:
				hovxx=(-hovx)
			if hovy<0:
				hovyy=-hovy
			if hovxx<hovyy: #or hovx<(-hovy) or (-hovx)<(-hovy) or (-hovx)<(hovy):
				if (hovx>0 and hovy>0) or (hovx<0 and hovy>0):
					if self.boardv[mousey+1][mousex]==False:
						self.boardv[mousey+1][mousex]=True
						#self.score1=self.score1+1
						if self.flip==1:
							self.score1=self.score1+1
							self.checkv(self.flip,mousey+1,mousex)
							self.flip=2
						elif self.flip==2:
							self.score2=self.score2+1
							self.checkv(self.flip,mousey+1,mousex)
							self.flip=1
						#self.check(mousey+1,mousex)
				else:
					if self.boardv[mousey][mousex]==False:
						self.boardv[mousey][mousex]=True
						#self.score1=self.score1+1
						if self.flip==1:
							self.score1=self.score1+1
							self.checkv(self.flip,mousey,mousex)
							self.flip=2
						elif self.flip==2:
							self.score2=self.score2+1
							self.checkv(self.flip,mousey,mousex)
							self.flip=1
						#self.check(mousey,mousex)
			else:#if hovx>hovy or hovx>(-hovy) or (-hovx)>(-hovy) or (-hovx)>(hovy):
				if (hovx>0 and hovy>0) or (hovx>0 and hovy<0):
					if self.boardh[mousey][mousex+1]==False:
						self.boardh[mousey][mousex+1]=True
						#self.score1=self.score1+1
						if self.flip==1:
							self.score1=self.score1+1
							self.checkh(self.flip,mousey,mousex+1)
							self.flip=2
						elif self.flip==2:
							self.score2=self.score2+1
							self.checkh(self.flip,mousey,mousex+1)
							self.flip=1
						#self.check(mousey,mousex+1)
				else:
					if self.boardh[mousey][mousex]==False:
						self.boardh[mousey][mousex]=True
						#self.score1=self.score1+1
						if self.flip==1:
							self.score1=self.score1+1
							self.checkh(self.flip,mousey,mousex)
							self.flip=2
						elif self.flip==2:
							self.score2=self.score2+1
							self.checkh(self.flip,mousey,mousex)
							self.flip=1
						#self.check(mousey,mousex)
		self.score_me=str(self.score1)
		font = pygame.font.Font(None,36)
		text = font.render(self.score_me,1,(10,10,240))
		self.screen.blit(text,[327,540])

		self.won()

	def won(self):
		summ=0
		
		for i in range(7):
			for j in range(6):
				if self.matrix[i][j]>0:
					summ=summ+1
		#print(summ)
		if summ==42:
			if self.score1>self.score2:
				print("PLAYER 1 WON")
			elif self.score1<self.score2:
				print("PLAYER 2 WON")
			else:
				print("game draw")

############### START OF PROGRAM ##############

bg = BoxesGame() #__init__ is called right here
while 1:
	bg.update()
