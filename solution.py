import random, csv, os
class Item:
	def __init__(self, type, bottom, top):
		self.type= type
		self.bottom= bottom
		self.top= top

class Table:
	def __init__(self):
		self.board= range(22)
		self.items= [Item("snake", 4, 13), Item("snake", 10, 17), Item("ladder", 15, 19), Item("ladder", 3, 11)]

def game():
	table= Table()
	turns= 0
	position= 0
	while position< len(table.board)- 1:
		dice= random.randint(1, 6)
		turns +=1
		position+= dice
		for item in table.items:
			if item.type == "snake" and position == item.top:
				position= item.bottom
			elif item.type == "ladder" and position == item.bottom:
				position= item.top
	return turns

def main():
	sum= 0
	maxv= 0
	minv= 0
	NTurns= []
	NGames= 1000
	for i in range(NGames):
		val= game()
		NTurns.append(val)
		sum+= val
		maxv= max(maxv, val)
		if minv ==0:
			minv= val
		else:
			minv= min(minv, val)
	#print NTurns
	#print sum*1.0/NGames
	#print minv
	#print maxv

	with open(os.path.join(os.getcwd(), "result.csv"), mode= 'w') as output:
		output_writer= csv.writer(output, delimiter= '	', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		output_writer.writerow(["Game", "Number of Turns", "", "Min", minv])
		output_writer.writerow(["1", NTurns[0], "", "Max", maxv])
		output_writer.writerow(["2", NTurns[1], "", "Average", sum*1.0/NGames])
		for i in range(2, 1000):
			output_writer.writerow([i+1, NTurns[i]])

if __name__ == '__main__':
	main()
