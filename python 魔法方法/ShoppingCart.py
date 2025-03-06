from typing import List

class ShoppingCart:
    def __init__(self,items:List[str]):
        self.items = items
    
    def __add__(self, another_cart):
        new_cart = ShoppingCart(self.items + another_cart.items)
        return new_cart
    
    def __str__(self):
        return f"cart({self.items})"
    
    def __len__(self):
        return len(self.items)
    
    def __call__(self, item):
        self.items.append(item)


cart1 = ShoppingCart(["apple","banana"])
cart2 = ShoppingCart(["orange","pear"])
# __add__
new_cart = cart1 + cart2
print(new_cart.items)

# __str__
print(cart1)

# __len__
print(len(cart1))

# __call__
cart1("orange")
print(cart1)

