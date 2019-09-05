import unittest
import main

class TestCosme(unittest.TestCase):

    def setUp(self):
        self.vending_machine = main.VendingMachine()

    def test_100円を入力すると化粧水と返す(self):
        self.assertEqual(self.vending_machine.enter(100), "現在100円が入っています")


    def test_100円１回入力すると保存する(self):
        self.vending_machine.enter(100)
        self.assertEqual(self.vending_machine.personal_array,[100])


    def test_100円２回入力すると保存する(self):
        self.vending_machine.enter(100)
        self.vending_machine.enter(100)
        self.assertEqual(self.vending_machine.personal_array,[100, 100])


    def test_100円２回入力した後90円入力しても無視する(self):
        self.vending_machine.enter(100)
        self.vending_machine.enter(100)
        self.vending_machine.enter(90)
        self.assertEqual(self.vending_machine.personal_array,[100, 100])


    def test_100円以外を入れると100円を入れてくださいと返す(self):
        self.assertEqual(self.vending_machine.enter(90), "他のお金を入れてください")


    def test_100円２回入力した後合計を計算する(self):
        self.vending_machine.enter(100)
        self.vending_machine.enter(100)
        self.assertEqual(self.vending_machine.money_sum(),sum([100, 100]))


if __name__ == '__main__':
    unittest.main()
