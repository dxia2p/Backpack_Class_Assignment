class Backpack:
    __items = []
    open = False
    def __init__(self, color, size):
        self.color = color
        self.size = size
    
    def openBag(self):
        print("BAG OPENED")
        self.open = True
    def closeBag(self):
        print("BAG CLOSED")
        self.open = False
    def putin(self, item):
        if open:
            self.__items.append(item)
            print(f"{item} added to {self.color} {self.size} backpack")
        else:
            print("Backpack is not open")
    def takeout(self, item):
        if item in self.__items and self.open:
            self.__items.remove(item)
            print(f"{item} removed from {self.color} {self.size} backpack")
        else:
            print("Backpack is not open or item is not in backpack")

smallBlueBackpack = Backpack("blue", "small")
mediumRedBackpack = Backpack("red", "medium")
largeGreenBackpack = Backpack("green", "large")

backpacks = [smallBlueBackpack, mediumRedBackpack, largeGreenBackpack]
for b in backpacks:
    b.openBag()
    b.putin("lunch")
    b.putin("jacket")
    b.closeBag()
    b.openBag()
    b.takeout("jacket")
    b.closeBag()
