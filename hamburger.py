class Hamburger:
    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

class BasitHamburger(Hamburger):
    def get_cost(self):
        return 100
    
    def get_ingredients(self):
        return "Köfte,Ekmek"
    
class HamburgerDecorator(Hamburger):
    def __init__(self,hamburger):
        self.hamburger = hamburger

    def get_cost(self):
        return self.hamburger.get_cost()
    
    def get_ingredients(self):
        return self.hamburger.get_ingredients()
    
class Peynirli (HamburgerDecorator):
    def __init__(self,hamburger):
        super().__init__(hamburger)

    def get_cost(self):
        return super().get_cost() + 8
    
    def get_ingredients(self):
        return super().get_ingredients() + ",Peynir"
    
class SosluHamburger(HamburgerDecorator):
    def __init__(self,hamburger):
        super().__init__(hamburger)

    def get_cost(self):
        return super().get_cost() + 5
    
    def get_ingredients(self):
        return super().get_ingredients() + ",Sos"
    
class KaramelizeSoğanHamburger(HamburgerDecorator):
    def __init__(self,hamburger):
        super().__init__(hamburger)

    def get_cost(self):
        return super().get_cost() + 10
    
    def get_ingredients(self):
        return super().get_ingredients() + ",Karamelize Soğan"
    
class Kola(HamburgerDecorator):
    def __init__(self,hamburger):
        super().__init__(hamburger)

    def get_cost(self):
        return super().get_cost() + 25
    
    def get_ingredients(self):
        return super().get_ingredients() + ",Kola"
    
class Salata(HamburgerDecorator):
    def __init__(self,hamburger):
        super().__init__(hamburger)

    def get_cost(self):
        return super().get_cost() + 30
    
    def get_ingredients(self):
        return super().get_ingredients() + ",Salata"
    
class Sogan(HamburgerDecorator):
    def __init__(self,hamburger):
        super().__init__(hamburger)

    def get_cost(self):
        return super().get_cost() + 2
    
    def get_ingredients(self):
        return super().get_ingredients() + ",Sogan"
    
def yazdir(hamburger):
    print("İçindekiler: {}".format(hamburger.get_ingredients()))
    print("Fiyat: {}".format(hamburger.get_cost()))


# Örnek kullanım
basit_hamburger = BasitHamburger()
yazdir(basit_hamburger)

peynirli_hamburger = Peynirli(basit_hamburger)
yazdir(peynirli_hamburger)

soslu_hamburger = SosluHamburger(basit_hamburger)
yazdir(soslu_hamburger)

karamelize_soğan_hamburger = KaramelizeSoğanHamburger(basit_hamburger)
yazdir(karamelize_soğan_hamburger)

kola_salata_sogan_hamburger = Sogan(Salata(Kola(basit_hamburger)))
yazdir(kola_salata_sogan_hamburger)

kola_soğan_hamburger = Sogan(Kola(basit_hamburger))
yazdir(kola_soğan_hamburger)
