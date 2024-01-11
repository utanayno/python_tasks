from address import Address
class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def whatMailing(self):
        print(self.from_address, self.to_address, self.cost, self.track)
    
    #не понимаю, как сделать, чтобы данные в to_address, from_address брались из класса Address