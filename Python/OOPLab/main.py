from customer import Customer
from product import Product

# from alarm_clock import AlarmClock

# new_clock = AlarmClock()

# new_clock.display_time()
# new_clock.set_time()
# new_clock.display_alarm_time()
# new_clock.set_alarm()

carlos = Customer("Carlos")
cecilia = Customer("Cecilia")

usb = Product("USB drive", 30, "Computer stuff")
tshirt = Product("Oddly fitting white T-shirt", 45, "Clothing")
coffee = Product("Super special coffee", 60, "Groceries")
hat = Product("Baseball cap", 15, "Clothing")

print(carlos.name)
print(cecilia.name)

carlos.add_product(tshirt)
carlos.add_product(hat)
cecilia.add_product(usb)
cecilia.add_product(coffee)

carlos.view_products()
cecilia.view_products()

carlos.shopping_cart.get_total()
cecilia.shopping_cart.get_total()

carlos.shopping_cart.empty_cart()
cecilia.shopping_cart.empty_cart()

carlos.view_products()
cecilia.view_products()