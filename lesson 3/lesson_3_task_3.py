from address import Address
from Mailing import Mailing

to_address = Address(630123, "Novosibirsk", "Lenina", "12", 345)
from_address = Address(177654, "Moscow", "Pushkina", "132б", 15)

to_address.toAddress()
from_address.fromAddress()

Mailing1 = Mailing(to_address, from_address, 500, '098755689455')
Mailing1.whatMailing()

def tracking():
    print("Отправление ", Mailing1.track, "из ", from_address.index, from_address.city, from_address.street, from_address.house, "-", from_address.appt, "в ", to_address.index, to_address.city, to_address.street, to_address.house, "-", to_address.appt, ". Стоимость ", Mailing1.cost, " рублей.")
tracking()
