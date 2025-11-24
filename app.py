class Pet:
    def __init__(self, name, money, inventory, feeling):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.feeling = feeling
        
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    
    def feel(self,item):
        self.inventory.append(item)
        print(self.inventory)

Coke = Pet("Coke", 150, ["Potion"], "netrual = 50%")
Coke.buy({"cookie"})
Coke.feel({"happy = 100%"})



# class pet:
#     def __init__(self, name, money, inventory,hungry):
#         self.name = name
#         self.money = money
#         self.inventory = inventory
#         self.hungry = hungry 

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)

#     def eat(self,item):
#         self.inventory.append(item)
#         print(self.inventory)
    
#     def hunger(self,item):
#         self.inventory.append(item)
#         print(self.inventory)

# Coke = pet("Coke", 150, ["Potion"],"netrual")

# Coke.buy({"title": "Sword", "attack": 10000000000})

# Coke.eat({"title": "Cookie"})
# emotion = "happy"

# Coke.hunger({"percent":"10%"})
# print(Coke.__dict__)

# class pet:
#     def __init__(self, name, atk):
#         self.name = name
#         self.atk = atk
    
#     def display_info(self):
#         return f"User: {self.name}, Level: {self.atk}"





