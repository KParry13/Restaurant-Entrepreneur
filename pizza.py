from order import Order

class Pizza:
    def __init__(self, crust, sauce, topping) -> None:
        self.crust = crust
        self.sauce = sauce
        self.topping = topping
        super().__init__()