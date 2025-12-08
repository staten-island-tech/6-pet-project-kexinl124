class Pet:
    def __init__(self, name,inventory,feed, feeling, hunger,living):
        self.name = name
        self.inventory = inventory
        self.feeling = feeling
        self.hunger = hunger
        self.feed = feed
        self.living = living
        living = True
        self.happiness = 50
        self.hunger = 50

    def activites (self, choice):
        choice = input("What would you want to with Coke? buy? feed? play? ignore?").lower
        if choice == "feed":
            feed = input( "what food would you like to feed Coke?")
            print(feed)
        if choice == "ignore":
            self.happiness -=10
            print(f"{self.name} happiness level is at {self.happiness}")
        
        


    def buy(self, item):
        self.inventory.append(item)
        print(Coke.__dict__)
    
    # def food(self,food):
    #     self.foods.append(food)
    #     print(Coke.__dict__)
    
    def hungry(self, feed):
        feed = input("what food would you feed Coke?")
        if feed in self.inventory:
            self.hunger -= 10
        else:
            print("Item not founded!")
        if self.hunger >= 50 and self.hunger <= 100:
            print(f"{self.name} is hungry, it's hunger level is at {self.hunger}%")
        elif self.hunger < 50 and self.hunger >= 0:
            print(f"You should stop feeding {self.name}, it is not hungry, its hungry level is at {self.hunger}%")
        elif self.hunger < 0:
            print(f"{self.name} is dead, its hungry level is at {self.hunger}%")
            self.living = False
        else:
            print(f"{self.name} is dead, its hungry level at {self.hunger}%")
            self.living = False
        if 
    
    
        

Coke = Pet("Coke", ["apple","cookie"], "feed", "feeling", "hunger level:", "living")
print(Coke.__dict__)










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





