class Game(object):
	def __init__(self):
		self.__rolls = []

	def roll(self, pins):
		self.__rolls.append(pins)
	
	def score(self):
		score = 0
		i = 0
		for frame in range(10):
			score += self.__rolls[i] + self.__rolls[i+1]
			i += 2
		return score

		