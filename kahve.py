class Kahve:
    def __init__(self):
        self._kahve = "Kahve"

    def get_name(self):
        return self._kahve

    def hazirla(self):
        print("Kahve hazirlaniyor...")

    def get_cost(self):
        return 50

class KahveDecorator(Kahve):
    def __init__(self, kahve):
        self._kahve = kahve

    def get_name(self):
        return self._kahve.get_name()

    def hazirla(self):
        self._kahve.hazirla()

    def get_cost(self):
        return self._kahve.get_cost()

class Sut(KahveDecorator):
    def __init__(self, kahve):
        super().__init__(kahve)

    def get_name(self):
        return super().get_name() + ", Süt"

    def hazirla(self):
        super().hazirla()
        print("Süt ekleniyor...")

    def get_cost(self):
        return super().get_cost() + 5

class Seker(KahveDecorator):
    def __init__(self, kahve):
        super().__init__(kahve)

    def get_name(self):
        return super().get_name() + ", Şeker"

    def hazirla(self):
        super().hazirla()
        print("Şeker ekleniyor...")

    def get_cost(self):
        return super().get_cost() + 1

class Çikolata(KahveDecorator):
    def __init__(self, kahve):
        super().__init__(kahve)

    def get_name(self):
        return super().get_name() + ", Çikolata"

    def hazirla(self):
        super().hazirla()
        print("Çikolata ekleniyor...")

    def get_cost(self):
        return super().get_cost() + 7
    
class Karamel(KahveDecorator):
    def __init__(self, kahve):
        super().__init__(kahve)

    def get_name(self):
        return super().get_name() + ", Karamel"

    def hazirla(self):
        super().hazirla()
        print("Karamel ekleniyor...")

    def get_cost(self):
        return super().get_cost() + 7
    
class Vanilya(KahveDecorator):
    def __init__(self, kahve):
        super().__init__(kahve)

    def get_name(self):
        return super().get_name() + ", Vanilya"

    def hazirla(self):
        super().hazirla()
        print("Vanilya ekleniyor...")

    def get_cost(self):
        return super().get_cost() + 3
    
class BeyazÇikolata(KahveDecorator):
    def __init__(self, kahve):
        super().__init__(kahve)

    def get_name(self):
        return super().get_name() + ", Beyaz Çikolata"

    def hazirla(self):
        super().hazirla()
        print("Beyaz Çikolata ekleniyor...")

    def get_cost(self):
        return super().get_cost() + 7
    

def yazdir(kahve):
    print("İçindekiler: {}".format(kahve.get_name()))
    kahve.hazirla()
    print("Fiyat: {} TL".format(kahve.get_cost()))

if __name__ == "__main__":
    kahve = Kahve()

    cikolatali_kahve = Çikolata(kahve)
    yazdir(cikolatali_kahve)

    karamel_kahve = Karamel(kahve)
    yazdir(karamel_kahve)

    vanilyali_kahve = Vanilya(kahve)
    yazdir(vanilyali_kahve)

    sutlu_kahve = Sut(kahve)
    yazdir(sutlu_kahve)

    sekerli_kahve = Seker(kahve)
    yazdir(sekerli_kahve)

    karamelli_kahve = Karamel(Vanilya(Seker(Sut(kahve))))
    yazdir(karamelli_kahve)

    beyazçikolatali_kahve = BeyazÇikolata(Seker(Sut(kahve)))
    yazdir(beyazçikolatali_kahve)