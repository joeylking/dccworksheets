from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_product(self, product):
        self.shopping_cart.add_product(product)

    def view_products(self):
        print(f"{self.name}'s products: ")
        for product in self.shopping_cart.products:
            print(product.name)