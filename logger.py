# As a developer, I want to create a Logger class with a log_transaction() method 
#       that will accept an Order object and store number and:
#       Increase the Logger’s transaction_count by one
#       Add the price of the Order object to the Logger’s daily_sales
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
        
class Logger:
    def __init__(self, number, sales) -> None:
        self.transaction_count = number
        self.daily_sales = sales


    def log_transaction(self, Order, number):
        
         
         
         
         
         
    def write_to_file(message):
        file = open("log.txt", "a")
        file.write (message)
        file.close()

    write_to_file("!/n")
        