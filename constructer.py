class Suzuki:
    carname = "maruthi 800"
    def __init__(self,name,colour,price):
        self.colour = colour
        self.price = price
        self.name = name



sam = Suzuki("sam","red",230000)
print(sam.__dict__)
#vihaan= Suzuki()
#print(sam)
