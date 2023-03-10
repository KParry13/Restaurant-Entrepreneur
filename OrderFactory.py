# As a developer, I want to create an Order Factory class with a static create_order method
# As a developer, I want to utilize a Factory Pattern in the create_order() method 
#         to instantiate instances of the three different Order child classes.
# This method should accept a string as a parameter (ex “Pizza”) 
#         and return the corresponding type of Order child class instantiation (ex Pizza() )
from pizza import Pizza
from pasta import Pasta
from salad import Salad
class OrderFactory:
    
    @staticmethod
    def create_order(choice):
        if choice == "1":
            return Pizza()
        elif choice == "2":
            return Pasta()
        elif choice == "3":
            return Salad ()
        
    

