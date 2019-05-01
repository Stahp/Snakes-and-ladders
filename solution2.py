import random, turtle
from math import atan, degrees
class Item:
	def __init__(self, type, bottom, top):
		self.type= type
		self.bottom= bottom
		self.top= top

class Table:
	def __init__(self):
		self.board= range(22)
		self.items= [Item("snake", 4, 13), Item("snake", 10, 17), Item("ladder", 15, 19), Item("ladder", 3, 11)]
		self.dict= {}
		for i in range(1, 5):
			self.dict[i]= (-170 + 90* (i-1), -180)
			self.dict[8+i]= (-170 + 90* (i-1), 0)
			self.dict[16+i]= (-170 + 90* (i-1), 180)
		for i in range(1, 5):
			self.dict[4+i]= (100 - 90* (i-1), -90)
			self.dict[12+i]= (100 - 90* (i-1), 90)
		self.dict[0]= (-220, -245)
		self.dict[21]= (200, 245)

class My_Turtle:
	def __init__(self, start_pos, color):
		self.my_turtle= turtle.Turtle()
		self.my_turtle.shape("turtle")
		self.my_turtle.color(color)
		self.my_turtle.shapesize(2, 2)
		self.my_turtle.penup()
		self.my_turtle.speed("slow")
		self.my_turtle.setpos(start_pos)

	def move(self, end_pos):
		start_pos= self.my_turtle.pos()
		dy= end_pos[1] - start_pos[1]
		dx= end_pos[0] - start_pos[0]
		if dx > 0:
			alpha= degrees(atan(dy/dx))
		elif dx <0:
			alpha= 180+degrees(atan(dy/dx))
		else:
			if dy >0:
				alpha= 90
			else:
				alpha= -90
		self.my_turtle.settiltangle(alpha)
		self.my_turtle.setpos(end_pos)

class User:
	def __init__(self, trtl, pos, canplay):
		self.trtl= trtl
		self.pos= pos
		self.canplay= canplay

def game(start6= 0, end_exact= 0):
	table= Table()
	screen= turtle.Screen()
	screen.bgpic("snake.png")
	print("You are the Green Turtle")
	print("You are playing against the Red Turtle")

	canplay= True #for start6
	if start6== 1:
		canplay= False
	player= User(My_Turtle(table.dict[0], (0, 1, 0)), 0, canplay)
	computer= User(My_Turtle(table.dict[0], (1, 0, 0)), 0, canplay)

		
	actualplayer = player
	gameover= False
	#while player.pos< len(table.board)- 1 and computer.pos< len(table.board)- 1:
	while True:
		if actualplayer == player:
			print("Press Enter to Roll the Dice")
			input()
			dice= random.randint(1, 6)
			print("You rolled: "+ str(dice))
			print()
		else:
			dice= random.randint(1, 6)
			print("The computer rolled: "+ str(dice))
			print()

		if start6== 1:
			if actualplayer.canplay== False and dice ==6:
				actualplayer.canplay= True
		
		canmove= True #for end_exact

		if actualplayer.canplay:
			if end_exact== 1 and actualplayer.pos+ dice > 21:
				canmove= False
			if canmove:
				for i in range(dice):
					actualplayer.pos+= 1
					actualplayer.trtl.move(table.dict[actualplayer.pos])
					if actualplayer.pos== 21:
						gameover= True
						break
			if gameover:
				break
			for item in table.items:
				if item.type == "snake" and actualplayer.pos == item.top:
					actualplayer.pos= item.bottom
					actualplayer.trtl.move(table.dict[actualplayer.pos])
				elif item.type == "ladder" and actualplayer.pos == item.bottom:
					actualplayer.pos= item.top
					actualplayer.trtl.move(table.dict[actualplayer.pos])
		if actualplayer == player:
			actualplayer= computer
		else:
			actualplayer= player

	if actualplayer == player:
			print("You won !")
	else:
		print("The Computer Won !")
	print("Press Enter to end the game")
	input()


def main():
	game(1, 1)

if __name__ == '__main__':
	main()