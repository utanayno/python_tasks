from smartphone import Smartphone

phone1 = Smartphone('nokia', 'M30', '+79222222262')
phone2 = Smartphone('iPhone', '14Pro', '+79222233383')
phone3 = Smartphone('Xiaomi', '120', '+79222266696')
phone4 = Smartphone('Samsung', '09', '+79222266676')
phone5 = Smartphone('One', '10', '+79222288888')

catalog = [phone1, phone2, phone3, phone4, phone5]

def sayAboutSmartphone():
    for i in catalog:
        print(i.brand, "-", i.model, "-", i.number)
sayAboutSmartphone()
