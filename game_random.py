import time
import sys
from random import randint
class Snakegame:
	def __init__(self,name,name1):
		self.pos=0
		self.pos1=0
		self.name=name
		self.name1=name1
		self.game(self.name,self.name1)
	def snake(self,pos):
		self.pos=pos
		if self.pos==17:
			print('\tSnake bite')
			return 7
		elif self.pos==54:
			print('\tSnake bite')
			return 34
		elif self.pos==62:
			print('\tSnake bite')
			return 19
		elif self.pos==64:
			print('\tSnake bite')
			return 60
		elif self.pos==83:
			print('\tSnake bite')
			return 51
		elif self.pos==99:
			print('\tSnake bite')
			return 10
		else:
			return self.pos
	def ladder(self,pos):
		self.pos=pos
		if self.pos==12:
			print('\tladder')
			return 36
		elif self.pos==29:
			print('\tladder')
			return 66
		elif self.pos==41:
			print('\tladder')
			return 58
		elif self.pos==69:
			print('\tladder')
			return 88
		elif self.pos==73:
			print('\tladder')
			return 93
		else:
			return self.pos
	def game(self,name,name1):
		self.name=name
		self.name1=name1
		while(self.pos!=100 and self.pos1!=100):
			self.a=randint(1,6)
			print('\tdice for {} :'.format(self.name),self.a)
			if self.pos+self.a>100:
				print('\tSpin again\n')
			elif self.pos+self.a==100:
				print('\tCongratulations {} you win'.format(self.name))
				break
			else:
				self.pos+=self.a
				self.pos=self.snake(self.pos)
				self.pos=self.ladder(self.pos)
				print('\tposition:',self.pos)
				print()
			time.sleep(2)
			self.b=randint(1,6)
			print('\tdice for {} :'.format(self.name1),self.b)
			if self.pos1+self.b>100:
				print('\tSpin again\n')
			elif self.pos1+self.b==100:
				print('\tCongratulations {} you win'.format(self.name1))
				break
			else:
				self.pos1+=self.b
				self.pos1=self.snake(self.pos1)
				self.pos1=self.ladder(self.pos1)
				print('\tposition:',self.pos1)
				print()
opt=input('Do you want to play the snake game?(Y for Yes and N for no):').lower()
if opt=='y':
	name=input('\tEnter name of Player 1: ')
	name1=input('\tEnter name of Player 2: ')
	print()
	s=Snakegame(name,name1)
else:
	print('\tThank you')
	time.sleep(10)
	sys.exit()