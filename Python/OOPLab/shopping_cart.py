from product import Product

class ShoppingCart:
    def __init__(self):
        self.products = []

    def get_total(self):
        prices = []
        for product in self.products:
            prices.append(product.price)
        cart_total = sum(prices)
        print(f"Your total is ${cart_total}")
        return cart_total

    def add_product(self, new_product):
        self.products.append(new_product)
        print(f"{new_product.name} added to shopping cart!")

    def empty_cart(self):
        self.products.clear()
        print("All products removed from cart!")
