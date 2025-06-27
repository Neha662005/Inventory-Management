def read_inventory():
    """
    Reads the inventory from 'inventory.txt' file and returns it as a dictionary.
    Each product gets a unique ID starting from 1.
    File format: name,brand,quantity,price,origin per line
    Returns: dictionary {product_id: [name, brand, qty, price, origin]}
    """
    # Initialize an empty dictionary to store inventory items
    inventory = {}
    #opening the inventory file in read mode
    file = open("inventory.txt", "r")
    #read all lines from the file
    data = file.readlines()
    #closing the file
    file.close()

    #setting product id as 1
    product_id = 1
    for line in data:
        #remove the new line and seperate by comma
        line = line.replace("\n", "").split(",")
        #Storing the items in the inventory dictionary with a product id
        inventory[product_id] = line
        #increamenting the product id by 1 everytime
        product_id = product_id + 1
        #returns inventory dictionary
    return inventory

#defining read_bill_no()
def read_bill_no():
    """
    Reads the current bill number from 'bill_no.txt' file.
    File contains single integer value.
    Returns: integer representing last used bill number
    """
    #opening the bill_no. text file in read mode
    file = open("bill_no.txt", "r")
    #reading the bill no. and converting it into int datatype
    bill_no = int(file.read())
    #closing the file
    file.close()
    #returning bill_no
    return bill_no
