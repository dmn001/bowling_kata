import unittest
from bowling import Game
 
class BowlingTest(unittest.TestCase):
   
   def rollMany(self, n, pins):
      for i in range(n):
         self.g.roll(pins)

   def rollSpare(self):
      self.g.roll(5)
      self.g.roll(5)

   def setUp(self):
      self.g = Game()

   def test_gutterGame(self):
      self.rollMany(20,0)
      self.assertEqual(0, self.g.score())

   def test_allOnes(self):
      self.rollMany(20,1)
      self.assertEqual(20, self.g.score())

   def test_oneSpare(self):
      self.rollSpare()
      self.g.roll(3)
      self.rollMany(17, 0)
      self.assertEqual(16, self.g.score())

if __name__ == "__main__":
	unittest.main()
