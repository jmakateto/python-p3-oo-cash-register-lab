#!/usr/bin/env python3

import unittest
from cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.register = CashRegister()

    def test_add_item(self):
        self.register.add_item("Item1", 10.0, 2)
        self.assertEqual(self.register.total, 20.0)

    def test_calculate_discount(self):
        self.register.add_item("Item1", 10.0, 2)
        self.register.calculate_discount(10)
        self.assertEqual(self.register.total, 18.0)

    def test_void_last_transaction(self):
        self.register.add_item("Item1", 10.0, 2)
        self.register.void_last_transaction()
        self.assertEqual(self.register.total, 0)

if __name__ == '__main__':
    unittest.main()
