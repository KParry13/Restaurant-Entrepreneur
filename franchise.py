# As a developer, I want to create a Franchise class with a place_order() method that will:
#   ask a user what food they would like to order
#   call the static OrderFactory.create_order() method to instantiate an order object.
#   call the logger.log_transaction() method to log the order to the log.txt file
from logger import Logger

class Franchise:

    def __init__(self, number):
        self.location_number = number
        
    def place_order(self):
        order = input("What can I get for you today? Pizza, Pasta, or Salad").lower
        print(f"You have chosen {order}.")
        pass
