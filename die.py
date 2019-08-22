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
			self.players.append([0, 1])
	def reset(self) :
		for i in self.players :
			i = [0, 1]
		self.victor = False
	def turn(self) :
		for i in self.players :
			print('Player' )
			for x in dice.len() :
				dice[x].roll()
			results = [dice[1].check(), dice[2].check(), dice[3].check(), dice[1].check() + dice[2].check(), dice[1].check() + dice[2].check() + dice[3].check(), dice[1].check() +
dice[3].check(), dice[2].check() + dice[3].check()]
			while i[1] + i[2] in results :
				i[1] += i[2]
				if i[1] == 12 : i[2] = -1
				if i[1] == 1 and i[2] == -1 :
					selfvictor = self.players.index(i)
					return
	def check(self) :
		return self.victor



