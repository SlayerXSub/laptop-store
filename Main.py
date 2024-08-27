import sys
import Operation
import Read
import Write
from datetime import datetime

now = datetime.now()
DateAndTime = now.strftime("%w") + "-" + now.strftime("%B") + "-" + now.strftime("%Y") + " " + now.strftime("%H") + "-" + now.strftime("%M") + "-" + now.strftime("%S") 


def main():
   
    loop = True
    while loop == True:
        print("|   Enter 1 to View the Available Laptops   |")
        print("|         Enter 2 to Sell Laptop/s          |")
        print("|       Enter 3 to Purchase Laptop/s        |")
        print("|        Enter 4 to Exit the System.        |")
        
        print("\n")
        lap_sn=1
        laptop_details={}
        laptop_details, lap_sn, readFile = Read.laptopDetails(laptop_details,lap_sn)

        u_input = Operation.correct_u_input()
        if u_input == 1:
            Read.showLaptops()

            

        elif u_input == 2:
            
            #Checking for Valid Name
            cust_name = Operation.correct_u_name()
            #Checking for Valid Phone Number
            cust_no = Operation.correct_u_number()
            purchasedLaptops = []
            buy_more = True 
            while buy_more == True:
                Read.showLaptops()
            #Checking for Valid SN
                user_sn = Operation.correct_sn(laptop_details)
            
                #Checking for Valid Quantity
                user_quantity = Operation.correct_quantity(laptop_details, user_sn)

                
                Write.change_quantity(laptop_details,user_sn,user_quantity)
                

                #Laptops purchased by the customer
                laptop_name, user_quantity, company, unit_price, selected_laptop_price, total_cost, purchasedLaptops, a = Operation.itemsInBill(laptop_details, user_sn, user_quantity, purchasedLaptops)
                more_laptops = input("Do you want to purchase more laptops? (Y/N) ").upper()
                print("\n")
                if more_laptops == "Y":
                    buy_more = True
                else: 
                    total = 0 
                    shipCost = 50
                    for i in purchasedLaptops:
                        total += int(i[5])
                    cost_with_shipcost = total + shipCost
                    a = 1
                    Write.PrintBill(DateAndTime, cust_name, cust_no, purchasedLaptops, shipCost, cost_with_shipcost, a )
                    Write.PrintBillInFile(DateAndTime, cust_name, cust_no, purchasedLaptops, shipCost, cost_with_shipcost, a )
                    buy_more = False

                    
        elif u_input == 3:

            #Checking for Valid Distributor Name
            distri_name = Operation.correct_distri_name()

            soldLaptops = []
            sell_more= True
            while sell_more == True:
                Read.showLaptops()
                user_sn = Operation.correct_sn2()
                user_quantity = Operation.correct_quantity2(laptop_details, user_sn)
                Write.change_quantity_sell(laptop_details,user_sn, user_quantity)
                laptop_name, user_quantity, company, unit_price, selected_laptop_price, total_cost, soldLaptops, a = Operation.itemsInBill(laptop_details, user_sn, user_quantity, soldLaptops)
                more_laptops = input("Do you want to purchase more laptops? (Y/N) ").upper()
                print("\n")
                if more_laptops == "Y":
                    sell_more = True
                else: 
                    total = 0 
                    VAT=13/100
                    for i in soldLaptops:
                        total += int(i[5])
                    VAT_amt=total*VAT
                    cost_with_VAT = total + VAT_amt
                    a = 1
                    Write.PrintBillPurchase(DateAndTime, distri_name, soldLaptops, VAT_amt, cost_with_VAT, a )
                    Write.PrintBillInFilePurchase(DateAndTime, distri_name, soldLaptops, VAT_amt, cost_with_VAT, a )
                    buy_more = False
        elif u_input == 4:
            print("Thank you for using the program!")
            sys.exit(0)
        else:
            print("Invalid input! Please Try again!")

main()
