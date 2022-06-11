from Items import Item


class Keyboard(Item):
    def __init__(self, name: str, price: float):
        #call to super to have access to all attributes and methods from the parent class Item

        super().__init__(name, price)