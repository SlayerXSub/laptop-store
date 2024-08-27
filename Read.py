#Creating a function for all the laptops info in a dictionary
def laptopDetails(laptop_details , lap_sn):
    readFile = open("laptops.txt","r")
    for line_to_read_file in readFile:
        line_to_read_file = line_to_read_file.replace("\n", "")
        laptop_details.update({lap_sn: line_to_read_file.split(",")})
        lap_sn = lap_sn + 1
    readFile.close()
    return laptop_details, lap_sn, readFile

#Creating a function to display all the laptops available and their info
def showLaptops():
      
    print("-------------------------------------------------------------------------------------------------------------------")
    print("S.N    |    Laptop Name    |    Company    |    Price    |    In Stock    |    Processor    |    Graphics Card")
    print("-------------------------------------------------------------------------------------------------------------------")
    print ("\n")
    file = open("laptops.txt", "r")
    a=1
    for line in file:
        print (a, "\t    " + line.replace(",", "\t"))
        a = a + 1
        print ("-------------------------------------------------------------------------------------------------------------------") 
        
        print ("\n")
    file.close()
