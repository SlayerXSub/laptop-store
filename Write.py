#Creating a function to change the quantity after purchasing
def change_quantity(laptop_details,user_sn,user_quantity):
    laptop_details[user_sn][3] = int(laptop_details[user_sn][3])-int(user_quantity)
    file = open("laptops.txt", "w")
    for components in laptop_details.values():
        file.write(str(components[0]) + "," + str(components[1]) + "," + str(components[2]) + "," + str(components[3]) + "," + str(components[4]) + "," + str(components[5]))

        file.write("\n")
    file.close()

#Creating a function to change the quantity after selling  
def change_quantity_sell(laptop_details,user_sn,user_quantity):
    laptop_details[user_sn][3] = int(laptop_details[user_sn][3])+int(user_quantity)
    file = open("laptops.txt", "w")
    for components in laptop_details.values():
        file.write(str(components[0]) + "," + str(components[1]) + "," + str(components[2]) + "," + str(components[3]) + "," + str(components[4]) + "," + str(components[5]))

        file.write("\n")
    file.close()

#Creating a function to display the bill after selling
def PrintBill(DateAndTime, cust_name, cust_no, purchasedLaptops, shipCost, cost_with_shipcost, a ):
        print("\n")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("|\t\t \t \t \t \t \t \t \t \t                                       |")
        print("|\t \t \t \t \t \t     The Laptop Heaven NP   \t\t\t\t\t       |")       
        print("|\t                                                                                                               |")
        print("|\t \t \t \t \tBasundhara, Kathmandu | Phone No: 9860969268\t\t\t\t       |")
        print("|\t                                                                            \t                               |")

        print("|\t Date: \t "+str(DateAndTime),"                                                                                   \t               |")
        print("|\t Customer Name: " + cust_name ,  "                                                      \t                               |")
        print("|\t Contact Number:", cust_no, "                                                                                            |")

        print(" ----------------------------------------------------------------------------------------------------------------------")
        print("| S.N    |    Laptop Name    |    Company    |    Quantity   |   Unit Price   |    Total Price   |")
        print(" ----------------------------------------------------------------------------------------------------------------------")
        for i in purchasedLaptops:
            print("|  ", a, "\t\t", i[0],"", i[1], "\t\t", i[2], "\t", i[3], "\t$", i[5])
            a = a + 1
        print("|                                                            |  Shipping Cost : $ 50                                    |")
        print("|                                                            |  Final Price   : $", str(cost_with_shipcost),"                                |")
        print ("-----------------------------------------------------------------------------------------------------------------------") 

#Creating a function to display the bill in a text file after selling
def PrintBillInFile(DateAndTime, cust_name, cust_no, purchasedLaptops, shipCost, cost_with_shipcost, a ):
    file = open(str(cust_name)+ "-" +str(DateAndTime) + ".txt", "w")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------")
    file.write("|\t\t \t \t \t \t \t \t \t \t                                       |")
    file.write("|\t \t \t \t \t \t     The Laptop Heaven NP   \t\t\t\t\t       |")       
    file.write("|\t                                                                                                               |")
    file.write("|\t \t \t \t \tBasundhara, Kathmandu | Phone No: 9860969268\t\t\t\t       |")
    file.write("|\t                                                                            \t                               |")

    file.write("|\t Date: \t "+ str(DateAndTime)+"                                                                                   \t               |")
    file.write("|\t Customer Name: " + cust_name+ "                                                      \t                               |")
    file.write("|\t Contact Number:"+cust_no+ "                                                                                            |")

    file.write(" ----------------------------------------------------------------------------------------------------------------------")
    file.write("| S.N    |    Laptop Name    |    Company    |    Quantity   |   Unit Price   |    Total Price   |")
    file.write(" ----------------------------------------------------------------------------------------------------------------------")
    for i in purchasedLaptops:
        file.write(str(a)+ "    "+ str(i[0])+ "    "+ str(i[1])+ "    "+ str(i[2])+ "    "+str(i[3])+ "    "+str(i[5]))
        a = a + 1
    file.write("|                                                            |  Shipping Cost : $ 50        |")
    file.write("|                                                            |  Final Price   : $" + str(cost_with_shipcost) + "                    |")
    file.write("-----------------------------------------------------------------------------------------------------------------------") 

#Creating a function to display the bill after purchasing
def PrintBillPurchase(DateAndTime, cust_name, purchasedLaptops, VAT_amt, cost_with_VAT, a ):
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("|\t\t \t \t \t \t \t \t \t \t                                       |")
    print("|\t \t \t \t \t \t     The Laptop Heaven NP   \t\t\t\t\t       |")       
    print("|\t                                                                                                               |")
    print("|\t \t \t \t \tBasundhara, Kathmandu | Phone No: 9860969268\t\t\t\t       |")
    print("|\t                                                                            \t                               |")

    print("|\t Date: \t "+str(DateAndTime),"                                                                                   \t               |")
    print("|\t Customer Name: " + cust_name ,  "                                                      \t                               |") 

    print(" ----------------------------------------------------------------------------------------------------------------------")
    print("| S.N    |    Laptop Name    |    Company    |    Quantity   |   Unit Price   |    Total Price   |")
    print(" ----------------------------------------------------------------------------------------------------------------------")
    for i in purchasedLaptops:
        print("|  ", a, "\t\t", i[0], "", i[1], "\t\t", i[2], "\t", i[3], "\t$", i[5],)
        a = a + 1
    print("|                                                            |  Shipping Cost : $"+str(VAT_amt),"          |")
    print("|                                                            |  Final Price   : $", str(cost_with_VAT),"                    |")
    print ("-----------------------------------------------------------------------------------------------------------------------") 

#Creating a function to display the bill in a text file after purchasing    
def PrintBillInFilePurchase(DateAndTime, distri_name,  purchasedLaptops, VAT_amt, cost_with_VAT, a ):
    file = open(str(distri_name)+ "-" +str(DateAndTime) + ".txt", "w")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------")
    file.write("|\t\t \t \t \t \t \t \t \t \t                                       |")
    file.write("|\t \t \t \t \t \t     The Laptop Heaven NP   \t\t\t\t\t       |")       
    file.write("|\t                                                                                                               |")
    file.write("|\t \t \t \t \tBasundhara, Kathmandu | Phone No: 9860969268\t\t\t\t       |")
    file.write("|\t                                                                            \t                               |")

    file.write("|\t Date: \t "+ str(DateAndTime)+"                                                                                   \t               |")
    file.write("|\t Customer Name: " + str(distri_name)+"                                                      \t                               |")      

    file.write(" ----------------------------------------------------------------------------------------------------------------------")
    file.write("| S.N    |    Laptop Name    |    Company    |    Quantity   |   Unit Price   |    Total Price   |")
    file.write(" ----------------------------------------------------------------------------------------------------------------------")
    for i in purchasedLaptops:
        file.write(str(a)+ "    "+ str(i[0])+ "    "+ str(i[1])+ "    "+ str(i[2])+ "    "+str(i[3])+ "    "+str(i[5]))
        a = a + 1
    file.write("|                                                            |   VAT Amount: "+str(VAT_amt)+"     |")
    file.write("|                                                            |   Final Price: "+str(cost_with_VAT)+"                    |")
    file.write("-----------------------------------------------------------------------------------------------------------------------") 
