# As a developer, I want to create a Logger class with a log_transaction() method 
#       that will accept an Order object and store number and:
#           Increase the Logger’s transaction_count by one
#           Add the price of the Order object to the Logger’s daily_sales

#       Open the log.txt file
#       Write a well-formatted message to the log.txt file containing the 
#           current transaction count, 
#           the name of the dish ordered, 
#           the store it was ordered from, 
#           the price of the item, 
#           and the combined daily income.
#       Close the log.txt file.

# As a developer, I want to use the Singleton pattern (as shown in the Design Patterns Demo repo)
#    to create a single instance of a Logger object inside the logger.py file 
#    and import this instance into the Franchise class to be shared by all instantiations.
from order import Order
from franchise import Franchise

class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, store_number):
        Order.dish_name and store_number()
        self.transaction_count += 1
        self.daily_sales = Order.price + self.daily_sales

        file = open("log.txt", "a")
        file.write (f"TRX#{self.transaction_count}: {Order.dish_name} at location {Franchise.location_number} - ${Order.price}. Total:${self.daily_sales}\n")
        file.close()

logger = Logger()
    
        