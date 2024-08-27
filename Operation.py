#Creating a function to validate the user input
def correct_u_input():
    true = True 
    while true == True:
        try:
            u_input = int(input("Enter the One of the Options to Continue: "))
            if u_input < 1 or u_input > 4:
                print("Please Enter a Valid Number(1-4)!!")
            else:
                true = False  

        except(ValueError):
            print("Please Enter a Valid Number!!")
    print("\n")
    return u_input

#Creating a function to validate the customer's name
def correct_u_name():
    while True:
        cust_name = input("Enter the Name of the Customer: ")
        if cust_name.isnumeric():
            print("Please Enter a Valid Name!!")
        else:
            break
    return cust_name

#Creating a function to validate the customer's number
def correct_u_number():
    while True:
        cust_number = input("Enter the Phone Number of the Customer: ")
        if not cust_number.isnumeric():
            print("Please Enter a Valid Phone Number!!")
        else:
            break
    return cust_number     

#Creating a function to validate the input laptop S.N
def correct_sn(laptop_details):

    while True:
        user_sn = input("Please Enter the Laptop S.N of the Laptop you would like to purchase: ")
        print("\n")
        if user_sn.isnumeric():
            user_sn = int(user_sn)
            if user_sn==0:
                print("Please Enter a Valid Laptop S.N !!")
                print("\n")
                continue
            if user_sn <= 0 or user_sn > len(laptop_details):
                print("Please Enter a Valid Laptop S.N !!")
                print("\n")
                continue
            if int(laptop_details[int(user_sn)][3])<=0:
                print("We don't have Enough Laptops in Stock. Sorry for the Inconvenience.")
                print("\n")
                continue
            if user_sn==0:
                    print("Please Enter a Valid Laptop S.N !!")
                    print("\n")
                    continue
            if user_sn <= 0 or user_sn > len(laptop_details):
                    print("Please Enter a Valid Laptop S.N !!")
                    print("\n")
                    continue
            user_sn = int(user_sn)
            while user_sn <= 0 or user_sn > len(laptop_details):
                print("Please Enter a Valid Laptop S.N !!")
                print("\n")
                while True:
                    user_sn = input("Please Enter the Laptop S.N of the Laptop you would like to purchase:")
                    print("\n")
                    if user_sn==0:
                        print("Please Enter a Valid Laptop S.N !!")
                        print("\n")
                        continue
                    print("\n")
                    if user_sn.isnumeric():
                        user_sn = int(user_sn)
                        while int(laptop_details[user_sn][3])<=0:
                            print("We don't have Enough Laptops in Stock. Sorry for the Inconvenience.")
                            print("\n")
                            user_sn = int(input("Please Enter the Laptop S.N of the Laptop you would like to purchase: "))
                            print("\n")
                            if user_sn==0:
                                print("Please Enter a Valid Laptop S.N !!")
                                print("\n")
                                continue
                            while  not user_sn.isnumeric():
                                print("Please Enter a Numeric Value for Laptop S.N !!")
                                print("\n")
                                user_sn = input("Please Enter the Laptop S.N of the Laptop you would like to purchase:  ")
                                print("\n")
                                if user_sn==0:
                                    print("Please Enter a Valid Laptop S.N !!")
                                    print("\n")
                                    continue
            user_sn = int(user_sn)
            break
        else:

            print("Please Enter a Valid Laptop S.N !!")
            print("\n") 
    return user_sn


#Creating a function to validate the input quantity
def correct_quantity(laptop_details, user_sn):
    laptop_quantity = laptop_details[user_sn][3]
    while True:
        try:
            user_quantity = int(input("How many Laptops would you like to Purchase: "))
            if user_quantity > int(laptop_quantity):
                print("We don't have Enough Laptops in Stock. Sorry for the Inconvenience.")
                #buy_more = False
                user_quantity = int(input("How many Laptops would you like to Purchase: "))
            else:
                break
            if user_quantity <= 0 :
                print("Please Enter a Valid Quantity!!")
            else:
                break

        except(ValueError):
            print("Please Enter a Valid Quantity!!")
    return user_quantity

#creating a function of the items to be added into the bill 
def itemsInBill(laptop_details, user_sn, user_quantity, purchasedLaptops):
    laptop_name = laptop_details[user_sn][0]
    user_quantity = user_quantity
    company = laptop_details[user_sn][1]
    unit_price = laptop_details[user_sn][2]
    selected_laptop_price = laptop_details[user_sn][2].replace ("$", " ")
    total_cost = int(user_quantity) * int(selected_laptop_price)
    purchasedLaptops.append([laptop_name, company, user_quantity, unit_price, selected_laptop_price, total_cost])
    a = 1
    return laptop_name, user_quantity, company, unit_price, selected_laptop_price, total_cost, purchasedLaptops, a

#Creating a function to validate the distributor's name
def correct_distri_name():
    while True:
        distri_name = input("Enter the Name of the Distributor: ")
        if distri_name.isnumeric():
            print("Please Enter a Valid Name!!")
        else:
            break
    return distri_name     

#Creating a function to validate the S.N of the laptop to purchase
def correct_sn2():
    while True:
        try:
            user_sn = int(input("Please Enter the S.N of the Laptop you Would Like to Purchase: "))
            if user_sn < 1 or user_sn > 5:
                print("Please Enter a Valid Laptop ID!!") 
            else:
                 break
        except(ValueError):
            print("Please Enter a Valid S.N")   
    return user_sn

#Creating a function to validate the quantity of laptops to be purchased
def correct_quantity2(laptop_details, user_sn):
    while True:
        try:
            user_quantity = int(input("How many Laptops would you like to Purchase: "))
            break
        except(ValueError):
            print("Please Enter a Valid Quantity!!")

    return user_quantity
