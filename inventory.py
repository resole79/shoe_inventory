# Note: If you don't have "Tabulate" install
# 1. Please download "module" folder with "inventor.py"
# 2. Uncomment the following string "from module.tabulate import tabulate" and indent
# 3. Comment the following string "from tabulate import tabulate"

# from module.tabulate import tabulate

from tabulate import tabulate

# ========The beginning of the class==========
class Shoe:

    # Method __init__
    def __init__(self, country, code, product, cost, quantity):
        """In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity."""

        # Instance variable
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method __str__
    def __str__(self):
        """Add a code to returns a string representation of a class."""
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    # Method to return the cost of the shoe
    def get_cost(self):
        """Add the code to return the cost of the shoe in this method."""
        return self.cost

    # Method to return the quantity of the shoe
    def get_quantity(self):
        """Add the code to return the quantity of the shoes."""
        return self.quantity


# ==========Functions outside the class==============
# Function to create header of menu
def header_of_menu(message):
    header_menu = "╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗\n"
    header_menu += f"    {bold}{italic}{message}{endc}"
    header_menu += "╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝\n"

    return header_menu


# Function to check empy item
def check_empty(item_to_check):
    # "if" condition to check empty item
    if item_to_check == "":
        empty_check = True
    else:
        empty_check = False

    return empty_check


# Function to find a last newline from file
def find_newline():

    # Declare Variable
    is_newline = True

    try:
        # Open file
        with open(file, "r") as shoes_inventory_read:
            read_shoes = shoes_inventory_read.readlines()
            file_len = len(read_shoes) - 1

            # "if" condition to check newline in last line
            if read_shoes[file_len].find("\n") == -1:
                is_newline = False

    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)

    return is_newline


# Function to separate head and body from file
def head_body_separate():
    # Declare Variable
    head_of_list = ""
    body_of_list = []

    try:
        # Open file
        with open(file, "r") as shoes_inventory_read:
            # for cycle to read all line in file
            for i, shoe_line in enumerate(shoes_inventory_read):
                # "if" condition don't take header file
                if i != 0:
                    body_of_list.append(shoe_line.strip().split(","))
                else:
                    head_of_list = (shoe_line.strip().split(","))
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)

    return head_of_list, body_of_list


# Function to clean the string head of file
def clean_head(head_message):
    return f"{head_message}\n".replace("[", "").replace("'", "").replace("]", "").replace(" ", "")


# Function to find max, min value and index from items
def max_and_min_stock(list_of_product):
    # Declare variable
    qty_list = []
    maximum_stock = 0
    maximum_stock_index = 0
    minimum_stock = 0
    minimum_stock_index = 0

    # "for" cycle to read every product in list
    for i, product_list in enumerate(list_of_product):
        # append all quantity in new qty_list
        qty_list.append(int(product_list.quantity))
        # Find max, min and index value
        maximum_stock = max(qty_list)
        maximum_stock_index = qty_list.index(maximum_stock)
        minimum_stock = min(qty_list)
        minimum_stock_index = qty_list.index(minimum_stock)

    return maximum_stock, maximum_stock_index, minimum_stock, minimum_stock_index


# Function to add quantity in stock
def add_in_stock(list_to_restock, index_product, number_to_add):
    for i, product in enumerate(list_to_restock):
        if i == index_product:
            product.quantity = int(product.quantity) + number_to_add

    print(f"\n{green}{bold} Shoe has been update to shoes list.{endc}\n")


# Function to update the file
def update_file(outside_list):
    # Declare variable
    head_list, body_of_list = head_body_separate()
    # Cycle "for" to read every key from dict
    new_string_update = clean_head(head_list)
    for count, key_outside_list in enumerate(outside_list):
        # Replace character to write into the file
        new_string_update += f"{str(key_outside_list)}\n"
    # Call function "write_to_file"
    write_to_file(file, new_string_update, "w")


# Function to write inside the file {comment ready}
def write_to_file(file_to_write, msg_to_write, mode="a+"):
    # Open "file_to_write" and write inside
    with open(file_to_write, mode) as open_to_write:
        # "if" condition to check voice of menu
        if user_choice == "cs":
            if not find_newline():
                open_to_write.write(f"\n{msg_to_write.strip()}")
            else:
                open_to_write.write(f"{msg_to_write}")
        else:
            open_to_write.write(f"{msg_to_write}")


# Function to read shoes and populate Class Shoe
def read_shoes_data():
    """This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code."""

    # Declare Variable
    # =============Shoe list===========
    """The list will be used to store a list of objects of shoes."""
    shoe_list = []

    header_list, body_list = head_body_separate()
    # "for" cycle to read all line from body list
    for i, shoe_line in enumerate(body_list):
        # Add shoes inside the Shoe class
        country_shoe, code_shoe, product_shoe, cost_shoe, quantity_shoe = shoe_line
        shoe_list.append(Shoe(country_shoe, code_shoe, product_shoe, cost_shoe, quantity_shoe))

    return shoe_list


# Function to add shoe in Class Shoe
def capture_shoes(country_shoe, code_shoe, product_shoe, cost_shoe, quantity_shoe):
    """This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list."""

    shoe_to_insert = f"{country_shoe},{code_shoe},{product_shoe},{cost_shoe},{quantity_shoe}\n"

    # Call function "write_to_file"
    write_to_file(file, shoe_to_insert)

    # Call function read_shoes_data()
    read_shoes_data()


# Function to print out all list of product
def view_all():
    """This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module."""

    # Declare Variable
    head_list, body_of_list = head_body_separate()
    body_list = []

    # "for" cycle to read all product in "body_of_list"
    for i, body_line in enumerate(body_of_list):
        body_list.append(body_line)

    return head_list, body_list


# Function to restock the items
def re_stock(index=""):
    """This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe."""

    # Declare variable
    quantity_in_stock = 0
    body_stock_list = read_shoes_data()
    max_stock, indx_max_stock, min_stock, indx_min_stock = max_and_min_stock(body_stock_list)

    # "for" cycle to read all product
    for i, product in enumerate(body_stock_list):

        # "if" condition to check index value and voice of menu
        if i == indx_min_stock and user_choice == "r":
            print("\nYour product lowest quantity in stock is : ")
            print(f"{i}. {product.__str__()}\n")
        elif i == index and user_choice == "s":
            print("\nDo you want restock this item?")
            quantity_in_stock = product.quantity
            print(f"{i}. {product.__str__()}\n")

    # Ask user to choice from menu
    print("Please choice one following number from menu! (0 to exit)")
    restock_answer = "1. Add how many of this product you want."
    # "if" condition to check voice of menu
    if user_choice == "r":
        restock_answer += f"\n2. Add (+{min_stock}) to this product.\n"
    else:
        restock_answer += f"\n2. Add (+{quantity_in_stock}) to this product.\n"

    restock_answer = input(restock_answer)
    if restock_answer == "1":
        try:
            # Ask user to insert quantity to restock
            num_restock = int(input("Please, insert quantity you want add to your product : "))
            # "if" condition to check voice of menu
            if user_choice == "r":
                # call "add_in_stock" function
                add_in_stock(body_stock_list, indx_min_stock, num_restock)
            else:
                # call "add_in_stock" function
                add_in_stock(body_stock_list, index, num_restock)

        except Exception as exception:
            print(f"\n{red}{bold}Ⓔ {exception}{endc}\n")

    elif restock_answer == "2":
        # "if" condition to check voice of menu
        if user_choice == "r":
            # call "add_in_stock" function
            add_in_stock(body_stock_list, indx_min_stock, min_stock)
        else:
            # call "add_in_stock" function
            add_in_stock(body_stock_list, index, int(quantity_in_stock))

    elif restock_answer == "0":
        pass
    else:
        print(f"\n{red}{bold} Ⓔ Oops - incorrect input.{endc}\n")

    # Call "update_file" function
    update_file(body_stock_list)


# Function to search shoe by product code
def search_shoe(shoe_code):
    """This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed."""

    # Declare Variable
    research_shoes = read_shoes_data()
    count_search = 0

    # "for" cycle to read all product
    for i, shoe_to_research in enumerate(research_shoes):
        # "if" condition to check code of shoe
        if shoe_to_research.code == shoe_code:
            print("\nYour search result is : ")
            count_search += 1
            print(f"{i}. {shoe_to_research.__str__()}\n")

            # The task didn't ask to do
            # uncomment "re_stock(i)" and indent if you want to see
            # I think restock is better to do when you search an item
            # Call "re_stock" function
            # re_stock(i)

    if count_search == 0:
        print(f"\n{red}{bold}{italic}Ⓔ Sorry, I can't find the item you search.{endc}")


def value_per_item():
    """This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes."""

    # Declare variable
    value_of_head = "Value per Item"
    body_stock_list = read_shoes_data()
    item_value_head, item_value_body = head_body_separate()
    new_list_body = []

    for i, item_value in enumerate(body_stock_list):
        value_item_body = f"{item_value.__str__()},{int(item_value.quantity) * float(item_value.cost)}"
        # Create a new list to print in tabulate
        new_list_body.append(value_item_body.strip().split(","))

    # New head to print in tabulate
    new_list_head = f"{clean_head(item_value_head)},{value_of_head}".strip().split(",")

    return new_list_body, new_list_head


def highest_qty():
    """Write code to determine the product with the highest quantity and
    print this shoe as being for sale."""

    # Declare Variable
    body_stock_list = read_shoes_data()
    max_stock, indx_max_stock, min_stock, indx_min_stock = max_and_min_stock(body_stock_list)

    # "for" cycle to read all items
    for i, qty_highest in enumerate(body_stock_list):
        if i == indx_max_stock:
            print("\nYour product highest quantity in stock is : ")
            print(f"{i}. {qty_highest.__str__()}")
    print("\nWe can start to SOLD this shoes!\n")


# ==========Main Menu=============
"""Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!"""

# Declare Variable
file = "inventory.txt"

# Color use for program
green = "\u001b[32m"
red = "\u001b[31m"
bold = "\033[1m"
italic = "\033[3m"
revers = "\u001b[7m"
endc = '\033[0m'

# Menu
menu_message = "Welcome to Nike warehouse system!\n"
usage_message = header_of_menu(menu_message)
usage_message += "What would you like to do?\n"
usage_message += "_________________"
usage_message += "________________________________________________________________________________________\n"
usage_message += f"{green}(VA){endc}View All - {green}(CS){endc}Capture Shoes - {green}(R){endc}e-stock - "
usage_message += f"{green}(S){endc}earch - {green}(SS){endc}Sold Shoes - {green}(VI){endc}Value per Item - "
usage_message += f"{green}(E){endc}xit : "

while True:

    user_choice = input(usage_message).strip().lower()

    if user_choice == "va":
        # Header of menu
        menu_message = "ⓋⒶ View All\n"
        print(f"\n{header_of_menu(menu_message)}")

        head, body = view_all()
        # Call "tabulate" method
        print(tabulate(body, head, colalign=("left", "left", "left", "left", "left"), tablefmt="grid"))
        print()

    elif user_choice == "cs":
        # Header of menu
        menu_message = "ⒸⓈ Capture Shoe\n"
        print(f"\n{header_of_menu(menu_message)}")
        try:
            # Ask use to enter country, code, product, cost, quantity
            country_name = input("\nPlease, enter the country where the shoes is product : ").title()
            while check_empty(country_name):
                print(f"\n{red}{bold} Ⓔ Sorry, your country is empty.{endc}\n")
                country_name = input("\nPlease, enter the country where the shoes is product : ").title()

            code_product = input("Please, enter the code of the shoes : ").upper()
            while check_empty(code_product):
                print(f"\n{red}{bold} Ⓔ Sorry, your code is empty.{endc}\n")
                code_product = input("Please, enter the code of the shoes : ").upper()

            shoe_product = input("Please, enter the name of product : ").title()
            while check_empty(shoe_product):
                print(f"\n{red}{bold} Ⓔ Sorry, your product is empty.{endc}\n")
                shoe_product = input("Please, enter the name of product : ").title()

            cost_product = int(input("Please, enter the cost of the shoes : "))
            while check_empty(cost_product):
                print(f"\n{red}{bold} Ⓔ Sorry, your cost is empty.{endc}\n")
                cost_product = int(input("Please, enter the cost of the shoes : "))

            quantity_product = int(input("Please, enter the quantity of the shoes : "))
            while check_empty(quantity_product):
                print(f"\n{red}{bold} Ⓔ Sorry, your quantity is empty.{endc}\n")
                quantity_product = int(input("Please, enter the quantity of the shoes : "))

            # Call "capture_shoes" function
            capture_shoes(country_name, code_product, shoe_product, cost_product, quantity_product)

            print(f"\n{green}{bold} Shoe has been added to shoes list.{endc}\n")
        except ValueError as value_error:
            print(f"\n{red}{bold}Ⓔ{value_error}{endc}\n")

    elif user_choice == "r":
        # Header of menu
        menu_message = "Ⓡ Re-Stock\n"
        print(f"\n{header_of_menu(menu_message)}")

        # Call "re_stock" function
        re_stock()

    elif user_choice == "s":
        # Header of menu
        menu_message = "Ⓢ Search\n"
        print(f"\n{header_of_menu(menu_message)}")

        code_of_shoe = input("\nPlease, insert the product code of the item you want to see : ").upper()
        while check_empty(code_of_shoe):
            print(f"\n{red}{bold} Ⓔ Sorry, your cose of product is empty.{endc}\n")
            code_of_shoe = input("\nPlease, insert the product code of the item you want to see : ").upper()

        # Call "search_shoe" function
        search_shoe(code_of_shoe)

    elif user_choice == "ss":
        # Header of menu
        menu_message = "ⓈⓈ Sold Shoes\n"
        print(f"\n{header_of_menu(menu_message)}")

        # Call "highest_qty" function
        highest_qty()

    elif user_choice == "vi":
        # Header of menu
        menu_message = "ⓋⒾ Value per Item\n"
        print(f"\n{header_of_menu(menu_message)}")

        head_per_item, body_per_item = value_per_item()
        print()
        # Call "tabulate" method
        print(tabulate(head_per_item, body_per_item, colalign=("left", "left", "left", "left", "left", "left"), tablefmt="grid"))
        print()

    elif user_choice == "e":
        print("\nGoodbye\n")
        exit()

    else:
        print(f"\n{red}{bold} Ⓔ Oops - incorrect input.{endc}\n")
