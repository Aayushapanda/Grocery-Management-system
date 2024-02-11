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
items = []
while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to the supermarket------------------')
    print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
    choice = input('Enter the number of your choice : ')
#-----------------1. View all products avalable in the Super Market---------------------
    if choice == '1' :
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
    if choice == '2' :
        print('------------------Add items------------------')
        print('To add an item fill in the form')
        print("Enter name")
        name=str(input())
        print("Enter Unit of measure")
        uom1=str(input())
        print("Enter price")
        pri=str(input())
        print("Enter quantity")
        qty=str(input())
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        
        cursor = cnx.cursor()
        
        cnx.cursor().execute("INSERT INTO `grocery`.`itemtable` ( productname, uom, price, quantity) VALUES ( '"+name+"', '"+uom1+"', '"+pri+"', '"+qty+"');")
        cnx.commit()
        cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
        cursor = cnx.cursor()
        sqlite_select_query = """SELECT * from grocery.itemtable"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("id name unit of measure price quantity")
        for row in records:
            print( row[0], end='   ')
            print(row[1], end='   ')
            print( row[2], end='   ')
            print ( row[3], end='   ')
            print ( row[4], end='   ')
            print('')
        
#-----------------3. for Customer to Purchase products from the Super Market--------------------
    if choice == '3' :
            print('------------------purchase items------------------')
            cnx = mysql.connector.connect(host='localhost',
                                         database='grocery',
                                         user='root',
                                         password='Rootpw1234!')
 
            cursor = cnx.cursor()

            sqlite_select_query = """SELECT * from grocery.itemtable"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print (records)
            print("Id Item Unit of measure")
            amount=int(0)
            for row in records:
                
                print( row[0], end=' ')
                print(row[1], end=' ')
                print( row[2], end=' ')
                print ( row[3], end=' ')
                print ( row[4], end=' ')
                print ("enter quantity", end=' ')
                x=int(input())
                print('')
                amount+=x*int(row[3])
           
                if ( row[4]<x):
                    print('item out of stock.')
                    break
            print(amount)
#-----------------4. for Customer to search the availbility of products in the Super Market--------------------
    if choice == '4' :
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
        print(sqlite_select_query)
        print(records)
        print( "id", end='\t')
        print( "Product", end='\t')
        print( "unit", end='\t')
        print( "price", end='\t')
        print( "quantity", end='\t')
        print("")
        print("-------------------------------------------")









                
#-----------------for the admin to Change or Modify product details available in the Super Market-------------            
    if choice == '5' :
        print('------------------edit items------------------')
        item_name = input('Enter the name of the item that you want to edit : ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('Price $ : '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                print(item)
            else:
                print('Item not found')
                
    if choice == '6' :
        print('------------------exited------------------')
        break

    if(choice!=1 or 2 or 3 or 4 or 5 or 6): 
         print('You entered an invalid option')
