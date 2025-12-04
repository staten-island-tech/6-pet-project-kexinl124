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
    
    # def food(self,food):
    #     self.foods.append(food)
    #     print(Coke.__dict__)

    def hungry(self):
        if self.hunger >= 50 and self.hunger <= 100:
            print(f"{self.name} is not hungry, it's hunger level is at {self.hunger}%")
        elif self.hunger < 50:
            print(f"You should feed {self.name}, it's hungry, its hungry level is at {self.hunger}%")
        else:
            print(f"Stop feeding {self.name}, it's obese, its hungry level is at {self.hunger}%")
    
    def feed (self,foods):
        while self.hunger < 50:
            eat = input(f"What do you want to feed Coke?Here are the choices {self.foods}")
            if eat not in Coke.food:
                print("Sadly, you don't have that food. You will have to go shopping!") 
            else:
                self.hunger+=10
                print(f"You fed Coke {foods}, it's hunger level {self.hunger}")
        

Coke = Pet("Coke", 150, ["Potion"],["apple","cookie"], 50)










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





