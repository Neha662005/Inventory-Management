#importing read and operations module
import read
import operations

#setting loop as true
loop = True
#reading inventory data using read_inventory function
inventory = read.read_inventory()

#Setting the loop condition when loop equals equals to true
while loop == True:
    #printing option 1 as sell
    print("1 : Sell")
    #printing option 2 as Make Purchase
    print("2 : Make Purchase")
    #printing option 3 as Display Produc Stock"
    print("3 : Display Product Stock")
    #printing option 4 as Exit
    print("4 : Exit")

    #Using try-except conditon for default input
    try:
        #Asking input for user as choice
        choice = int(input("Enter your choice: "))

        #Setting condition when choice equals equals to 1 run operation.py modules sell(inventory) function
        if choice == 1:
            operations.sell(inventory)

        #Setting condition when choice equals equals to 2 run operation.py modules restock(inventory) function
        elif choice == 2:
            operations.restock(inventory)
        
        #Setting condition when choice equals equals to 3 run operation.py modules  display_inventory(inventory) function
        elif choice == 3:
            operations.display_inventory(inventory)

        #Setting condition when choice equals equals to 4 displaying proper message and breaking the loop by setting loop = false
        elif choice == 4: 
            print("Thank you! Visit Us again!!")
            loop = False

        #Setting else condition by displaying a proper message for choosing onlly option from 1 to 4
        else:
            print("Invalid choice. Please select a number from 1 to 4.")
    
    #If try block dosenot work then displaying a proper message asking user for valid number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
