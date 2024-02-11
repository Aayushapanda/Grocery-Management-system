#-----------------------------------------------------------------------------------------
#    Project on Grocery Management                                                  |
#    Author - Aayush Panda                                                                 |
#    Aditya English Medium School                                                      |
#    CBSE Class XII                                                                             |
#    Section B                                                                                       |
#    Roll Number 02                                                                             |
#-----------------------------------------------------------------------------------------
#--------------Header Section with all definitions of functions -------------------------
import mysql.connector
import sqlite3

#-----------------1. View all products avalable in the Super Market---------------------
def view_products():
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        cursor = cnx.cursor()
        sqlite_select_query = """SELECT * from grocery.itemtable"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print( "id", end='\t')
        print( "Product", end='\t')
        print( "unit", end='\t')
        print( "price", end='\t')
        print( "quantity", end='\t')
        print("")
        print("-------------------------------------------")
        for row in records:
            print( row[0], end='\t')
            print(row[1], end='\t')
            print( row[2], end='\t')
            print ( row[3], end='\t')
            print ( row[4], end='\t')
            print('')

#-----------------2. Add new products for Sale in the Super Market--------------------
def add_products():
        print('------------------Add items------------------')
        print('To add an item fill in the form')
        print("Enter name")
        name=str(input())
        print("Enter Unit of measure")
        uom=str(input())
        print("Enter price")
        price=str(input())
        print("Enter quantity")
        qty=str(input())
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        
        cursor = cnx.cursor()
        
        cnx.cursor().execute("INSERT INTO `grocery`.`itemtable` ( productname, uom, price, quantity)       VALUES ( '"+name+"', '"+uom+"', '"+price+"', '"+qty+"');")
        cnx.commit()
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        cursor = cnx.cursor()
        sqlite_select_query = """SELECT * from grocery.itemtable"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print( "id", end='\t')
        print( "Product", end='\t')
        print( "unit", end='\t')
        print( "price", end='\t')
        print( "quantity", end='\t')
        print("")
        print("-------------------------------------------")

        for row in records:
            print( row[0], end='\t')
            print(row[1], end='\t')
            print( row[2], end='\t')
            print ( row[3], end='\t')
            print ( row[4], end='\t')
            print('')
        
#-----------------3. for Customer to Purchase products from the Super Market--------------------
def purchase_products():
            print('------------------Purchase Products------------------')
            cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
            cursor = cnx.cursor()

            sqlite_select_query = """SELECT * from grocery.itemtable"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print( "id", end='\t')
            print( "Product", end='\t')
            print( "unit", end='\t')
            print( "price", end='\t')
            print('')
            amount=int(0)
            for row in records:
                print( row[0], end='\t')
                print(row[1], end='\t')
                print( row[2], end='\t')
                print ( row[3], end='\t')
                print ("enter quantity", end=' ')
                x=int(input())
                print('')
                amount+=x*int(row[3])
           
                if ( row[4]<x):
                    print('item out of stock.')
                    break
            print ("your total bill amount is Rs." +str(amount))
            print ("Please pay this amount at the checkout counter")       

#-----------------4. for Customer to search the availbility of products in the Super Market--------------------
def search_product():
        print('------------------Enter item to be searched------------------')
        
        find_item = str(input())
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        cursor1 = cnx.cursor()
        sqlite_select_query = "SELECT * from grocery.itemtable where productname = '"+find_item+"'"
        cursor1.execute(sqlite_select_query)
        records = cursor1.fetchall()
        if len(records) !=0:
            
            print( "id", end='\t')
            print( "Product", end='\t')
            print( "unit", end='\t')
            print( "price", end='\t')
            print( "quantity", end='\t')
            print("")
            print("-------------------------------------------")
            print(records)
        else:
            print("Product Not Available")
        
#-----------------for the admin to Change or Modify product details available in the Super Market-------------            
def edit_product():
        print('------------------edit items------------------')
        print('Enter the name of the item that you want to edit : ')
        edit_item = str(input())
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        cursor1 = cnx.cursor()
        sqlite_select_query = "SELECT * from grocery.itemtable where productname = '"+edit_item+"'"
        cursor1.execute(sqlite_select_query)
        records = cursor1.fetchall()
        if len(records) !=0:
            print( "id", end='\t')
            print( "Product", end='\t')
            print( "unit", end='\t')
            print( "price", end='\t')
            print( "quantity", end='\t')
            print("")
            print("-------------------------------------------")
            print(records)
            print('Enter the new price : ', end=' ')
            price_item = str(input())
            print('Enter the new quantity : ', end=' ')
            quantity_item = str(input())
            
            cursor2 = cnx.cursor()
            sqlite_modify_query = "UPDATE grocery.itemtable SET price = '"+price_item+"', quantity = '"+quantity_item+"' where productname = '"+edit_item+"'"
            cursor2.execute(sqlite_modify_query)
            cnx.commit()
            cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
            cursor = cnx.cursor()
            sqlite_select_query = """SELECT * from grocery.itemtable"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print( "id", end='\t')
            print( "Product", end='\t')
            print( "unit", end='\t')
            print( "price", end='\t')
            print( "quantity", end='\t')
            print("")
            print("-------------------------------------------")

            for row in records:
                print( row[0], end='\t')
                print(row[1], end='\t')
                print( row[2], end='\t')
                print ( row[3], end='\t')
                print ( row[4], end='\t')
                print('')
        

        else:
            print("Product Not Available")
        

                
#----------------- Main Section for grocery management-----------------------                

while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to the supermarket------------------')
    print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
    choice = int(input('Enter the number of your choice : '))

    if choice == 1 :
        view_products()
    if choice == 2 :
        add_products()
    if choice == 3 :
        purchase_products()
    if choice == 4 :
        search_product()
    if choice == 5 :
        edit_product()
    if choice == 6 :
        print('------------------exited------------------')
        break
    if(choice >6 or choice <1): 
         print('You entered an invalid option')

#----------------- End of Main Section for grocery management---------------------                

