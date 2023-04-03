from abc import ABC, abstractmethod


class Cart:
    def __init__(self):
        self.cart = {}

    def add_item_in_cart(self, item, quantity):
        self.cart.setdefault(item, {'quantity': 0,
                                    'price': item.price})
        self.cart[item]['quantity'] += quantity

    def remove_item_from_cart(self, item):
        self.cart.pop(item)

    def get_total_price(self):
        return sum([item['quantity'] * item['price'] for item in self.cart.values()])


class Item:
    def __init__(self, name, item_type, price):
        self.name = name
        self.item_type = item_type
        self.discount: Discount = self.get_discount()
        self.price = self.get_price(price)

    def get_discount(self):
        return DiscountForDrinks() if self.item_type == 'Drink' else DiscountForAll()

    def get_price(self, price):
        return self.discount.set_discount(price)


class Discount(ABC):
    @abstractmethod
    def set_discount(self, price):
        pass


class DiscountForAll(Discount):
    def set_discount(self, price):
        return price - (price * 0.05)


class DiscountForDrinks(Discount):
    def set_discount(self, price):
        return price - (price * 0.10)


if __name__ == '__main__':
    cart = Cart()
    banana = Item('Banana', 'Fruit', 10)
    apple_juice = Item('Apple', 'Drink', 20)

    cart.add_item_in_cart(banana, 3)
    cart.add_item_in_cart(apple_juice, 2)

    print(f'Общая сумма продуктов: {cart.get_total_price()}р')
