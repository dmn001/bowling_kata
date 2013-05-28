class Game(object):
	def __init__(self):
		self.__rolls = []

	def isSpare(self, firstInFrame):
		if self.__rolls[firstInFrame] + self.__rolls[firstInFrame+1] == 10:
			return 1
		else:
			return 0

	def roll(self, pins):
		self.__rolls.append(pins)
	
	def score(self):
		score = 0
		firstInFrame = 0
		for frame in range(10):
			if self.isSpare(firstInFrame):
				score += 10 + self.__rolls[firstInFrame+2]
			else:
				score += self.__rolls[firstInFrame] + self.__rolls[firstInFrame+1]
			firstInFrame += 2
		return score

