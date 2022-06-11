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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Your name is too long")

        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_increment(self, another_value):
        return self.price + self.__price * another_value

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

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f'''
        Hello Someone.
        We have {self.name} {self.quantity} times.
        RRegards...
        
        Goodness Mbakara
                '''

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
