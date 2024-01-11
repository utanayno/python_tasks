class Address:
    def __init__(self, index, city, street, house, appt):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.appt = appt

    def toAddress(self):
        print(self.index, self.city, self.street, self.house, '-', self.appt)

    def fromAddress(self):
        print(self.index, self.city, self.street, self.house, '-', self.appt)
    
to_address = Address(630123, "Novosibirsk", "Lenina", "12", 345)
from_address = Address(177654, "Moscow", "Pushkina", "132б", 15)

to_address.toAddress()
from_address.fromAddress()

