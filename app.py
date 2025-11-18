class pet:
    def __init__(self, name, money, inventory,emotion,food):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.emotion = emotion
        self.food = food

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def eat(self,):
        self.

Coke = pet("Coke", 150, ["Potion"],"Happy")

Coke.buy({"title": "Sword", "attack": 10000000000})
print(Coke.__dict__)





