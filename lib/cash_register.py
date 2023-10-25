#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction={}

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    self.items += [item] * quantity
    self.last_transaction.update({"item": item, "price": price*quantity})



  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * (1-self.discount/100))
      print(f'After the discount, the total comes to ${self.total}.')
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction["price"]
    self.items.remove(self.last_transaction['item'])
