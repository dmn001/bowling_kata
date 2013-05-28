class Game(object):
	def __init__(self):
		self.__rolls = []

	def isSpare(self, firstInFrame):
		return self.__rolls[firstInFrame] + self.__rolls[firstInFrame+1] == 10

	def isStrike(self, firstInFrame):
		return self.__rolls[firstInFrame] == 10

	def nextTwoBallsForStrike(self, firstInFrame):
		return self.__rolls[firstInFrame+1] + self.__rolls[firstInFrame+2]

	def nextBallForSpare(self, firstInFrame):
		return self.__rolls[firstInFrame+2]

	def twoBallsInFrame(self, firstInFrame):
		return self.__rolls[firstInFrame] + self.__rolls[firstInFrame+1]

	def roll(self, pins):
		self.__rolls.append(pins)
	
	def score(self):
		score = 0
		firstInFrame = 0
		for frame in range(10):
			if self.isStrike(firstInFrame):
				score += 10 + self.nextTwoBallsForStrike(firstInFrame)
				firstInFrame += 1
			elif self.isSpare(firstInFrame):
				score += 10 + self.nextBallForSpare(firstInFrame)
				firstInFrame += 2
			else:
				score += self.twoBallsInFrame(firstInFrame)
				firstInFrame += 2
			
		return score

