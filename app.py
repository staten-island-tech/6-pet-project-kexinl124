class Pet:
    def __init__(self, name, money, inventory,foodx):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.foodx = foodx
        
        
    def buy(self, item):
        self.inventory.append(item)
        print(Coke.__dict__)
       
    feels=50
    def feel(self,feels): 
        if Coke.buy != "cookie":
            feels -= 10
            feels = self.feels
            print(f"Coke is {self.feels}% happy")
        else:
            feels += 10
            feels = self.feels
            print(f"Coke is {self.feels}% happy")
    
    def food(self,item):
        self.inventory.append(item)
        print(Coke.__dict__)

    def eaT(self,food):
        hunger += 5
        print(f"You fed Coke {food}, hunger increased, {hunger}")
    
    

Coke = Pet("Coke", 150, ["Potion"],"fish")
Coke.buy({"cookie"})
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





