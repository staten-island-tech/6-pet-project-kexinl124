class Pet:
    def __init__(self, name, money, inventory,foods, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.foods = foods
        self.hunger = hunger

    def buy(self, item):
        self.inventory.append(item)
        print(Coke.__dict__)
    
    def food(self,item):
        self.inventory.append(item)
        print(Coke.__dict__)

    def hungry(self,food):
        hunger = 50
        eat = input("What do you want to feed Coke?")
        hunger+=10
        print(f"You fed Coke {food}, hunger level {hunger}")
        if eat not in Coke.food:
            print("Sadly Coke does not have that food at home. You will have to go shopping!") 

Coke = Pet("Coke", 150, ["Potion"],"fish", 50)
Coke.food("fish")
Coke.food("cucumber")
Coke.food("hot pot")








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





