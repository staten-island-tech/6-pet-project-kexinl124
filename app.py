class pet:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Coke = pet("Coke", 150, ["Potion"])

Coke.buy({"title": "Sword", "attack": 34})
print(Coke.__dict__)