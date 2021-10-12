from product import Product

# As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).

# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.

# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)

# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

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
