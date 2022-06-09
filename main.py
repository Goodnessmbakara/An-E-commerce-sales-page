import csv


class Item:
    # the pay rate after 20% discount
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
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
                price=int
                (item.get('price')),
                quantity=int(item.get('quantity')),

            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.all)
