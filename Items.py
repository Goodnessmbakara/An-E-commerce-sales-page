import csv

class Item:
    # the pay rate after 20% discount
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #run validations to received arguments
        assert price >= 0, f"price{price} is not greater or equal to zero"
        assert quantity >= 0, f"quantity{quantity} is not greater or equal to zero"

        #assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),

            )
    @staticmethod
    def is_integer(num):
        #we will count out the floats that are .0
        if isinstance(num, float):
            #count out floats that are.0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.__class__.__name__}'{self.name}', {self.price}, {self.quantity})"
