#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        
        self.items = []  # To store items 
        self.discount = 0  # To store the discount percentage
        self.total = 0  # To store the total price

    def add_item(self, item_name, price, quantity):
        
        item = (item_name, price, quantity)
        self.items.append(item)
        self.total += price * quantity

    def calculate_discount(self, discount_percentage):
        
        self.discount = discount_percentage
        discount_amount = (discount_percentage / 100) * self.total
        self.total -= discount_amount

    def void_last_transaction(self):
        
        if self.items:
            item_name, price, quantity = self.items.pop()
            self.total -= price * quantity
