import random
class Die :
	def __init__(self,  s = 6) :
		self.sides = s

	def roll(self) :
		self.value = random.randint(1, self.sides)

	def check(self) :
		return self.value



class Game :
	die1 = Die()
	die2 = Die()
	die3 = Die()
	players = []
	dice = [die1, die2, die3]
	victor = False

	def __init__(self, p = 6) :
		self.playernum = p
		for i in range(self.playernum) :
			self.players.append([0, 1, i])
	def reset(self) :
		for i in self.players :
			i = [0, 1]
		self.victor = False
	def turn(self) :
		for i in self.players :
			print('Player ' + str(i[2]) + ' turn')
			for x in self.dice :
				x.roll()
				print(x.check())
			results = [self.dice[0].check(), self.dice[1].check(), self.dice[2].check(), self.dice[0].check() + self.dice[1].check(), self.dice[0].check() + self.dice[1].check() + 
self.dice[2].check(), self.dice[0].check() + self.dice[2].check(), self.dice[1].check() + self.dice[2].check()]
			while i[0] + i[1] in results :
				i[0] += i[1]
				print('reached ' + str(i[0]))
				if i[0] == 12 : i[1] = -1
				if i[0] == 1 and i[1] == -1 :
					self.victor = i[2]
					return
	def check(self) :
		return self.victor

	def status(self) :
		output = 'Player Ranks\n'
		for i in self.players :
			output = output + str(i[2]) + ' at ' + str(i[0]) + ' going ' + str(i[1]) + '\n'
		return output

class MainRunner :

	def runGame(self) :
		game1 = False
		game1 = Game()
		while(not game1.check()):
			game1.turn()
		print(str(game1.check()) + ' won!')
		print(game1.status())
		game1.reset()


gamer = MainRunner()
x = '5'
while(not x == 'stop') :
	x = input()
	if x == 'game' : gamer.runGame()
