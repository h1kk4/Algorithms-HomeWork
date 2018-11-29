from menu import Menu


class Promo():
    def __init__(self, kind, products, discount, count=1):
        self._kind = kind
        self._products = products
        self._discount = discount

    def getInfo(self):
        print("kind =", self._kind, "products =", self._products, "discount =", self._discount)

    @property
    def kind(self):
        return self._kind

    @property
    def products(self):
        return self._products

    @property
    def discount(self):
        return self._discount


class Promo_Menu(Menu):
    """docstring for Promo_Menu"""

    def __init__(self, name, price, calories):
        super().__init__(name, price, calories)

    def getInfo(self):
        print("promo_products =", self._name, "promo_price =", self._price, "promo_calories =", self._calories)
