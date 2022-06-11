from Items import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        #call to super to have access to all attributes and methods from the parent class Item
        #run validations to received arguments
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"broken phones{broken_phones} is not greater or equal to zero"

        #assign to self objects
        self.broken_phones = broken_phones
