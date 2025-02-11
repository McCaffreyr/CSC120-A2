from typing import Optional

#computer class
class Computer:

    #initializing attributes of the computer
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, 
                 memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # storing information about a specific computer, 
    def comp_info(self, description:str):
        print("This computer is a", description)

    # updating a computer's price
    def update_price(self, newprice:float):
        self.price = newprice
        print("This computer is now", newprice, "dollars.")
        
    # updating a computer's OS
    def update_os(self, new_os: str):
        self.operating_system = new_os
        print("The operating system is now", new_os)

#computer resale shop class
class ResaleShop:

    #list to contain all the computers in the store
    inventory: list

    #initializing attributes of the store
    def __init__(self):
        self.inventory = []

    #prints out the store's inventory
    def print_inven(self):
        if self.inventory:
            for item in self.inventory:
                print(f"Item ID: {self.inventory.index(item)} : {item.description}")
        else:
            print("No inventory to display.")

    # buying a computer (add to inventory), 
    def buy(self, computer: Computer):
        print("Bought", computer.description)
        self.inventory.append(computer)
        print("Added to inventory.")

     # #selling a computer (remove from inventory)
    def sell(self, computer: Computer):
        if computer in self.inventory:
            print(f"Item ID: {self.inventory.index(computer)} : {computer.description}")
            self.inventory.remove(computer)
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.")

    #updates the price of a computer based on when it was made
    #optionally updates a computer's operating system
    def refurb(self, computer: Computer, new_os: Optional[str] = None):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
            if new_os:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", computer.description, "not found. Please select another item to refurbish.")

def main():

    #creating an instance of the Computer class
    comp1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    #creating an instance of the ResaleShop class
    shop1 = ResaleShop()

    #testing the computer Class
    comp1.comp_info(comp1.description)
    comp1.update_price(50)
    comp1.update_os(15.5)

    #buying a computer
    shop1.buy(comp1)

    #to see the impact of refurbishing a computer
    print(vars(comp1))
    shop1.refurb(comp1)
    print(vars(comp1))
    
    #selling a computer
    shop1.sell(comp1)

if __name__ == "__main__":
    main()

