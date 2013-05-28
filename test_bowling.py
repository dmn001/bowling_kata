import unittest
from bowling import Game
 
class BowlingTest(unittest.TestCase):
   
   def rollMany(self, n, pins):
      for i in range(n):
         self.g.roll(pins)

   def setUp(self):
      self.g = Game()

   def test_canRoll(self):
      self.g.roll(0)

   def test_gutterGame(self):
      self.rollMany(20,0)
      self.assertEqual(0, self.g.score())

   def test_allOnes(self):
      self.rollMany(20,1)
      self.assertEqual(20, self.g.score())



if __name__ == "__main__":
	unittest.main()
