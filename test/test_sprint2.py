import unittest
import main

class TestCosme(unittest.TestCase):

    def setUp(self):
        self.vending_machine = main.VendingMachine()


    def test_100から1000円までのお金を受け付けるようにする(self):
        self.vending_machine.enter(10)
        self.assertEqual(self.vending_machine.personal_array, [10])
        self.vending_machine.enter(50)
        self.assertEqual(self.vending_machine.personal_array, [10,50])
        self.vending_machine.enter(100)
        self.assertEqual(self.vending_machine.personal_array, [10,50,100])
        self.vending_machine.enter(500)
        self.assertEqual(self.vending_machine.personal_array, [10,50,100,500])
        self.vending_machine.enter(1000)
        self.assertEqual(self.vending_machine.personal_array, [10, 50, 100, 500,1000])


    def test_お金を保持する(self):
        self.vending_machine.enter(10)
        self.vending_machine.enter(50)
        self.vending_machine.enter(100)
        self.assertEqual(self.vending_machine.money_sum(), sum([10, 50, 100]))
        self.vending_machine.clear()
        self.vending_machine.enter(10)
        self.vending_machine.enter(50)
        self.vending_machine.enter(100)
        self.assertEqual(self.vending_machine.money_sum(), sum([10, 50, 100]))


    def test_複数の商品を準備する(self):
        self.assertEqual(self.vending_machine.goods, ["化粧水","日焼け止め","口紅"])