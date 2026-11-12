class ShoppingCart :
    def __init__(self , items : list) :
        self.items = items

    # Controls len(cart)
    def __len__(self):
        return len(self.items)

    # Controls print(cart)
    def __str__(self):
        return f"Bleh Bleh items len : {len(self.items)}"

cart = ShoppingCart(["Apple", "Banana", "Milk"])

print(len(cart))  # Output: 3 (Python automatically calls __len__)
print(cart)       # Output: Shopping Cart containing 3 items. (Calls __str__)