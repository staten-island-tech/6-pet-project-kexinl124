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

    def eat(self,item):
        self.inventory.append(item)
        print(self.inventory)
    
    def hunger(self,item):
        self.inventory.append(item)
        print(self.inventory)

Coke = pet("Coke", 150, ["Potion"],"Happy","cookie")

Coke.buy({"title": "Sword", "attack": 10000000000})
print(Coke.__dict__)

Coke.eat({"title": "Cookie"})
print(Coke.__dict__)

Coke.hunger({"percent":"10%"})
print(Coke.__dict__)

# class pet:
#     def __init__(self, name, atk):
#         self.name = name
#         self.atk = atk
    
#     def display_info(self):
#         return f"User: {self.name}, Level: {self.atk}"





