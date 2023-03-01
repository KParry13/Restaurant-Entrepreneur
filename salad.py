from order import Order

class Salad:
    def __init__(self, dressing, topping) -> None:
        self.dressing = dressing
        self.topping = topping
        super().__init__()