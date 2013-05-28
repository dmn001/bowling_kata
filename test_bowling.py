import unittest
from bowling import Game
 
class BowlingTest(unittest.TestCase):
   
   def rollMany(self, n, pins):
      for i in range(n):
         self.g.roll(pins)

   def rollSpare(self):
      self.g.roll(5)
      self.g.roll(5)

   def rollStrike(self):
      self.g.roll(10)

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

   def test_oneStrike(self):
      self.rollStrike()
      self.g.roll(3)
      self.g.roll(4)
      self.rollMany(17, 0)
      self.assertEqual(24, self.g.score())

   def test_perfectGame(self):
      self.rollMany(12, 10)
      self.assertEqual(300, self.g.score())

if __name__ == "__main__":
	unittest.main()
