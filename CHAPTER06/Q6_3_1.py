class Nigiri:
    def show_attributes(self):
        print("top: {}". format(self.top))
        print("topping: {}". format(self.topping))
        print("price: {}". format(self.price))


class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}". format(self.topping))


K1 = Katsuo()
K1.show_attributes()
