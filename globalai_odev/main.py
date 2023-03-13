import csv
from datetime import datetime


class Pizza:
    def __init__(self, price, description):
        self.__price = price
        self.component = None
        self.__description = description
    
    
    def get_cost(self):
        if self.component is None:
            return self.__price
        else:
            return self.__price + self.component.get_cost()

    def get_description(self):
        if self.component is None:
            return self.__description
        else:
            return self.__description + " - " + self.component.get_description()
    
    def set_component(self, sos):
        self.component = sos
    

class Klasik(Pizza):
    def __init__(self, price, description):
        super().__init__(price, description)


class Turk(Pizza):
    def __init__(self, price, description):
        super().__init__(price, description)


class Margarita(Pizza):
    def __init__(self, price, description):
        super().__init__(price, description)


class Sade(Pizza):
    def __init__(self, price, description):
        super().__init__(price, description)




class Sos:
    def __init__(self, price, desc) -> None:
        self.price = price
        self.desc = desc


    def get_cost(self):
        return self.price

    def get_description(self):
        return self.desc

class Zeytin(Sos):
    def __init__(self, price) -> None:
        super().__init__(price, "Zeytin")


class Mantar(Sos):
    def __init__(self, price) -> None:
        super().__init__(price, "Mantarlar")

class KeciPeyniri(Sos):
    def __init__(self, price) -> None:
        super().__init__(price, "Keci Peyniri")

class Et(Sos):
    def __init__(self, price) -> None:
        super().__init__(price, "Et")

class Sogan(Sos):
    def __init__(self, price) -> None:
        super().__init__(price, "Sogan")

class Misir(Sos):
    def __init__(self, price) -> None:
        super().__init__(price, "Misir")

def get_menu():
    # Opening file
    menu_file = open('menu.txt', 'r', encoding='utf-8')

    for line in menu_file:
        print(line.strip())


def select_order():
    print ("D&A Pizza'ya Hoşgeldiniz...")
    pizza_selection = int(input("Lütfen menüden istediğiniz pizzanın numarasını seçiniz: "))

    if pizza_selection == 1:
        uretilen_pizza = Klasik(120, "Klasik Pizza: Domates sos , sosis, mısır, mantar")
    
    elif pizza_selection == 2:
        uretilen_pizza = Margarita(110, "Margarita: Domates sos, mozzarella peyniri, fesleğen yaprakları,parmesan peyniri")

    elif pizza_selection == 3:
        uretilen_pizza = Turk(175, "Turk: Domates sos, sucuk, dana jambon, dana bacon, sosis, mısır, zeytin mozzarella peyniri, parmesan peyniri")

    elif pizza_selection == 4:
        uretilen_pizza = Sade(95, "Sade: Domates sos, mozzarella peyniri, roka yaprakları")

    else:
        print("Seçtiğiniz numara menümüzde bulunmamaktadır. Lütfen tekrar seçim yapınız.")
        uretilen_pizza = None
    

    sos_selection = int(input("İstediğiniz sos numarasını seçiniz: "))


    if sos_selection == 11:
        eklenen_sos = Zeytin(10)
    
    elif sos_selection == 12:
        eklenen_sos = Mantar(15)

    elif sos_selection == 13:
        eklenen_sos = KeciPeyniri(18)

    elif sos_selection == 14:
        eklenen_sos = Et(20)

    elif sos_selection == 15:
        eklenen_sos = Sogan(7)

    elif sos_selection == 16:
        eklenen_sos = Misir(9)

    else:
        print("Seçilen sos menümüzde bulunmamaktadır.Lütfen tekrar seçim yapınız.")
        eklenen_sos = None
    
    return uretilen_pizza, eklenen_sos

def add_order(order_record):
 
    with open(r'orders_database.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(order_record)
    
    return True

if __name__ == '__main__':

    
    get_menu()
    
    flag = True
    while flag:
        uretilen_pizza, eklenen_sos = select_order()
        if uretilen_pizza is not None:
            flag = False
    
    uretilen_pizza.set_component(eklenen_sos)

    cost = uretilen_pizza.get_cost()

    print ("Pizzanızın toplam fiyatı :", cost)

    customer_name = input("Adınız: ")
    customer_tc = input("TC Numaranız: ")
    customer_credit_card = input("Kredi Kartı Numaranız: ")
    credit_card_pin = input("Kredi Kartı Şifreniz: ")
    order_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    order_desc = uretilen_pizza.get_description()

    record = [customer_name, customer_tc, customer_credit_card, credit_card_pin, order_date, order_desc]

    order_res= add_order(record)

    if order_res == True:
        print("Siparisiniz en kısa zamanda teslim edilecek. Bizi tercih ettiğiniz için teşekkür ederiz.", record)
    
    else:
        print("Siparisiniz Kayit Edilemedi", record)

