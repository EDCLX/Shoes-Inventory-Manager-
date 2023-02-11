
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
       
    def get_cost(self):
        return self.cost
        

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.product} from {self.country} with code {self.code} costs £{self.cost} and there are {self.quantity} in stock.\n"


#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
# this function will read everything in the file and get all ready for the next functions
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            next(f) #skip the first line
            for line in f:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                cost = float(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

    except:
        print("An error ocurred when reading the file.")

                

 # this functions allows you to add a new shoe to the data base   
def capture_shoes():
    print("Fill as follow:\n")
    print("_" * 50 + "\n")
    country = input("Enter the country of origin: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity: "))
    print("_" * 50 + "\n")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)


#prints the whole data base with a string already set 
def view_all():
    for shoe in shoe_list:
        print(shoe.__str__())

def re_stock():
    #get the min quantity value in the data base 
    low_stock = min(shoe.quantity for shoe in shoe_list)
    shoes_to_restock = [shoe for shoe in shoe_list if shoe.quantity == low_stock]
    for shoe in shoes_to_restock:
        print(f"{shoe.product} with code {shoe.code} has the lowest stock with {shoe.quantity} units.")
        #ask the user quantity to add
        add_shoes = int(input("Enter the quantity to add: \n"))
        shoe.quantity += add_shoes
        print("Stock added\n")
        #update the file with the new info
        try:
            with open("inventory.txt", "w") as f:
                for shoe in shoe_list:
                    f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n") 
        except:
            print("An error ocurred updating the file")
            
# ask the user for the shoe code and prints out the info 
def search_shoe():
    code = input("Enter the code of the shoe to search for: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            break
    else:
        print("Wrong code, shoe not found")
    
#gets the stock value in £ per shoe
def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} with code {shoe.code} has a total value of £{value}\n")

# gets the shoe with max  stock quantity and prints it with a sale message 
def highest_qty():
    highest_quantity = max(shoe.quantity for shoe in shoe_list)
    highest_quantity = [shoe for shoe in shoe_list if shoe.quantity == highest_quantity]
    for shoe in highest_quantity:
        print(f"{shoe.product} with code {shoe.code} has the highest stock with {shoe.quantity} it should be put for sale.\n")

    
    

#==========Main Menu=============
print("\n\n")
print("*" * 60 + "\n")
print("\t\tWELCOME TO THE SHOE STORE")
print("*" * 60 + "\n")
# this function get all ready for the menu
read_shoes_data()
while True:
    print("Please select an option: ")
    print("1. Capture shoe data")
    print("2. View all shoes")
    print("3. Restock lowest quantity shoe")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Determine highest quantity shoe")
    print("7. Exit")

    user_choice = input("\nEnter your choice: ")

    
    if user_choice == "1":
        capture_shoes()
    elif user_choice == "2":
        view_all()
    elif user_choice == "3":
        re_stock()
    elif user_choice == "4":
        search_shoe()
    elif user_choice == "5":
        value_per_item()
    elif user_choice == "6":
        highest_qty()
    elif user_choice == "7":
        print("Good bye!")
        break
    else:
        print("Invalid choice, try again")

    