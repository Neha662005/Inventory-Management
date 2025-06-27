#importing datetime from datetime
from datetime import datetime
#importing read module and write module
import read
import write

#defining a function to display inventory data
def display_inventory(inventory):
    #printing a line of underscores for visual separation
    print("_" * 70)
    #printing column headers for inventory display including both cost and selling price
    print("id \t name \t\t brand \t\t qty \t Price \t origin")
    #printing another line of underscores for visual separation
    print("_" * 70)
    #looping through each item in the inventory dictionary
    for key, value in inventory.items():
        #printing product ID without a new line
        print(key, end="\t")
        #printing product name without a new line
        print(value[0], end="\t")
        #printing brand name without a new line
        print(value[1], end="\t")
        #printing quantity available without a new line
        print(value[2], end="\t")
        #calculating selling price as 200% of cost price
        Price = int(value[3]) * 2
        #printing selling price without a new line
        print(Price, end="\t")
        #printing product origin and moving to next line
        print(value[4])
    #printing final line of underscores for visual separation
    print("_" * 70)

#defining a sell function
def sell(inventory):
    #taking input for their name
    customer_name = input("Customer name: ")
    #taking input for their phone number
    phone_number = input("Please enter your phone number: ")
    #creating empty list having variable name selling_items
    selling_items = []
    #setting value of total as 0
    total = 0
    #setting value of delivery_charege as 0
    delivery_charge = 0
    #setting selling_loop as true
    selling_loop = True

    while selling_loop:
        #displaying inventory by calling display_inventory(inventory) function
        display_inventory(inventory)
        #using try_except for default input
        try:
            #taking input from user for the product id they want to buy
            product_id = int(input("Enter product ID: "))
            #using if condition fro checking the product_id
            if product_id <= 0 or product_id > len(inventory):
                print("Invalid product ID!")
                continue
        #if the try block didnot work then displaying error message
        except:
            print("Invalid input for product ID! Please enter a number.")
            continue

        #using try_except for default input
        try:
            #taking input for no. of quantity and converting it into int datatype 
            quantity = input("Quantity to buy: ")
            product_quantity = int(quantity)

        except ValueError:
            #printing appropriate message if the try block didnot run or catches error
            print("Invalid input for quantity! Please enter a number.")
            continue

        #Displaying available stock
        stock = int(inventory[product_id][2])
        #Calculating free items based on policy of buy 3 get 1 free
        free_items = product_quantity // 3
        #calculating total quantity by adding product quantity and free items
        total_qty = product_quantity + free_items

        #setting if condition for calculating stock
        if product_quantity <= 0 or total_qty > stock:
            print("Insufficient stock.")
            continue

        print("Hello,", customer_name, "We have Buy 3 Get 1 free offer. You received", free_items, "items for free.")
        print("-" * 20, "Thank you! Visit us again!", "-" * 20)


        inventory[product_id][2] = str(stock - total_qty)
        #calculating price by multiplying price by 2 and converting in int datatype
        price = int(inventory[product_id][3]) * 2
        #calculating sub total
        sub_total = product_quantity * price
        #updating total cost
        total += sub_total

        #adding purchase item details in selling_items list
        selling_items.append((inventory[product_id][0], inventory[product_id][1], product_quantity, free_items, price, sub_total))

        # Handling the "Add more items" question properly
        while True:
            #taking input from user if they want to have more item
            more = input("Add more items? (y/n): ")
            #If customer choose else than y as option the loop will break
            if more.lower() == 'y':
                selling_loop = True
                break
            elif more.lower() == 'n':
                selling_loop = False
                break
            else:
                print("Please enter 'y' or 'n'")

    #asking for input if customer want delivery serviceor not
    delivery = input("Do you want delivery service for Rs. 500 extra? (y/n): ")
    #if the input from user is equals to equals to y then delivery charge will add
    if delivery.lower() == 'y' or 'yes':
        delivery_charge = 500
    #if the input from user is else that y as option then delivery change will remain 0
    else: 
        delivery_charge = 0
    #Calculating total by adding delivery charge 
    total = total + delivery_charge

    #reading current bill no. and increamenting by 1
    bill_no = read.read_bill_no() + 1
    #saving new bill no.
    write.write_bill_no(bill_no)

    #creating filename for bill
    filename = "bill_" + str(bill_no) + ".txt"
    lines = [
        "-------WeCare Wholesale--------",
        "   Kamalpokhari, Kathmandu",
        "  Bill No.: " + str(bill_no),
        "-------Tax Invoice ------",
        "Date: " + str(datetime.today()),
        "Customer: " + customer_name,
        "Phone: " + phone_number,
        "Items Purchased:"
    ]

    #adding items details
    for item in selling_items:
        line = "Product: " + item[0] + " | Brand: " + item[1] + " | Qty: " + str(item[2]) + " + " + str(item[3]) + " free | Unit Price: " + str(item[4]) + " | Subtotal: " + str(item[5])
        lines.append(line)

    #adding final bill details
    lines.append("Delivery Charge: " + str(delivery_charge))
    lines.append("Total: Rs. " + str(total))
    lines.append("Thank you! Visit Us again!!")

    #saving bills as file
    write.write_individual_bill(filename, lines)

    #Storing billing record in collective file
    allbill = ["\nBill No. : " + str(bill_no), "Customer: " + customer_name + " | Phone: " + phone_number]
    for item in selling_items:
        allbill.append("Product: " + item[0] + " | Qty: " + str(item[2]) + " + " + str(item[3]) + " free | Subtotal: " + str(item[5]))
    allbill.append("Total: Rs. " + str(total))
    allbill.append("-" * 40)

    #appending bill summary to collective record
    write.append_to_all_bills(allbill)

    #confirming sell success
    print("Selling is successful. Bill written to", filename)
    #updating inventory data
    write.write_inventory(inventory)

#defining a restock function
def restock(inventory):
    #asking input for vendor's name
    vendor_name = input("Enter Vendor's name: ")
    #asking input for vendor's phoone number
    phone_number = input("Please enter your phone number: ")
    #creating empty list as restocking_items
    restocking_items = []
    #Setting value of total as 0
    total = 0
    #setting restocking_loop as true
    restocking_loop = True

    while restocking_loop:
        #displaying inventory by calling display_inventory(inventory) function
        display_inventory(inventory)
        #using try-except for default value
        try:
            #asking input for product id
            product_id = int(input("Enter product ID: "))
            #Using if condition for checking valid product id
            if product_id <= 0 or product_id > len(inventory):
                print("Invalid product ID!")
                continue

        #if the try block gets an error then except block will run and will display messsage
        except:
            print("Invalid input for product ID! Please enter a number.")
            continue

        #using try-except for checking value for new-qty and new_price
        try:
            #taking input from user for new quantity
            new_qty = int(input("Enter quantity to add: "))
            #taking input from user for new_price
            new_price = int(input("Enter new cost price: "))

        #if try block didnot run or get an error then except block will display  message
        except:
            print("Invalid input! Please enter numbers for quantity and price.")
            continue

        #adding the new quantity and converting it back to a string datatype for consistency
        inventory[product_id][2] = str(int(inventory[product_id][2]) + new_qty)
        #Updating the price of product in inventory and converting it into string datatype for storage
        inventory[product_id][3] = str(new_price)

        #calculating subtotal by multiplying new quantity and new price
        subtotal = new_qty * new_price
        #updating total value
        total += subtotal
        #appending updated records in restocking_items
        restocking_items.append((inventory[product_id][0], inventory[product_id][1], new_qty, new_price, subtotal))

        #taking input from user if they want to have more item
        more = input("Add more items? (y/n): ")
        #If customer choose else than y or yes as option the loop will break
        if more.lower() == 'y':
            restocking_loop = True

        #If customer choose y as option the loop will continue
        else:
            restocking_loop = False
  
    #reading current bill no. and increamenting by 1
    bill_no = read.read_bill_no() + 1
    #saving new bill no.
    write.write_bill_no(bill_no)

    #creating filename for bill
    filename = "bill_" + str(bill_no) + ".txt"
    lines = [
        "-------WeCare Wholesale--------",
        "   Kamalpokhari, Kathmandu",
        "  Bill No.: " + str(bill_no),
        "-------Tax Invoice ------",
        "Date: " + str(datetime.today()),
        "Vendor: " + vendor_name,
        "Phone: " + phone_number,
        "Items Purchased:"
    ]

    #adding items details
    for item in restocking_items:
        lines.append("Product: " + item[0] + " | Brand: " + item[1] + " | Qty: " + str(item[2]) + " | Price: " + str(item[3]) + " | Subtotal: " + str(item[4]))

    #adding final bill details
    lines.append("Total: Rs. " + str(total))
    lines.append("Thank you! Visit Us again!!")
    write.write_individual_bill(filename, lines)

    #Storing billing record in collective file
    allbill = ["\nBill No.: " + str(bill_no), "Vendor: " + vendor_name + " | Phone: " + phone_number]
    for item in restocking_items:
        allbill.append("Product: " + item[0] + " | Qty: " + str(item[2]) + " | Subtotal: " + str(item[4]))
    allbill.append("Total: Rs. " + str(total))
    allbill.append("-" * 40)

    #appending bill summary to collective record
    write.append_to_all_bills(allbill)

    #confirming sell success
    print("Restock items successful. Bill written to", filename)
    #updating inventory data
    write.write_inventory(inventory)
