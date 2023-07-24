#!/usr/bin/env python3

class CashRegister:
  # pass
  def __init__(self, discount=0):
    self.items = []
    self.total = 0
    self.discount = discount

  def add_item(self, item, price, quantity=1):
    self.total += quantity * price
    self.last_item = item
    self.last_price = price
    self.last_quantity = quantity

    for i in range(quantity):
      self.items.append(item)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = int(self.total - self.total*self.discount/100)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    for i in range(self.last_quantity):
      self.items.pop()
    self.total = self.total - self.last_price * self.last_quantity

