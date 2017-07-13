import unittest
import os, sys


class TestPropInfo(unittest.TestCase):
    def setUp(self):
        self.pi = model.PropInfo(0, "a", 10, 100, [1])

    def test_get_house_cost(self):
        self.assertEqual(100, self.pi.get_house_cost())

    def test_get_rent(self):
        self.assertEqual(1, self.pi.get_rent(0))

class TestRailInfo(unittest.TestCase):
    def setUp(self):
        self.ri = model.RailInfo(0, "a", 10, {1:25, 2:50, 3:100, 4:200})

    def test_get_rent(self):
        self.assertEqual(self.ri.get_rent(1), 25)
        self.assertEqual(self.ri.get_rent(2), 50)
        self.assertEqual(self.ri.get_rent(3), 100)
        self.assertEqual(self.ri.get_rent(4), 200)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = model.Game()

    def test_basic(self):
        self.game.play()

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.g = model.Game()
        self.b = model.Board(self.g)

    def test_get_position_info(self):
        i = self.b.get_position_info(1)
        self.assertEqual(i.position, 1)
        self.assertEqual(i.name, "Mediterranean Avenue")
        self.assertEqual(i.cost, 60)
        self.assertEqual(i.house_cost, 50)
        self.assertEqual(i.rent[0], 2)

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from model import model
    unittest.main()
