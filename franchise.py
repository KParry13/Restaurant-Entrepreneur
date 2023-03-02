# As a developer, I want to create a Franchise class with a place_order() method that will:
#   ask a user what food they would like to order
#   call the static OrderFactory.create_order() method to instantiate an order object.
#   call the logger.log_transaction() method to log the order to the log.txt file
from OrderFactory import OrderFactory
from logger import logger
class Franchise:

    def __init__(self, number):
        self.location_number = number
        
    def place_order(self):
        order = input("Welcome to Francesco Italiano! What are you hungry for? Type '1' for pizza, '2' for pasta, '3' Salad")
        print(f"You have chosen {order}.")

        all_orders = OrderFactory.create_order(order)
        logger.log_transaction(all_orders, self.location_number)

