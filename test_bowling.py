import unittest
from bowling import Game
 
class BowlingTest(unittest.TestCase):
   def setUp(self):
      self.g = Game()

   def test_canRoll(self):
      self.g.roll(0)

   def test_gutterGame(self):
      for i in range(20):
         self.g.roll(0)
      self.assertEqual(0, self.g.score())

   def test_allOnes(self):
      for i in range(20):
         self.g.roll(1)
      self.assertEqual(20, self.g.score())

if __name__ == "__main__":
	unittest.main()
