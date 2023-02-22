import sqlite3
import qrcode

def Show_Menu():
    print("1 = Show")
    print("2 = Add")
    print("3 = Edit")
    print("4 = Remove")
    print("5 = Serch")
    print("6 = Buy")
    print("7 = QR_code")
    print("8 = Exit")

def Load_Database():
    global Connection
    global my_cursor

    Connection = sqlite3.connect("Assignment 21/store/store_db.db")
    my_cursor = Connection.cursor()

def Show_List():
    result = my_cursor.execute("SELECT * FROM products")
    products = result.fetchall()
    for product in products:
        print(product)

def Add_New(new_name,new_price,new_count):
    my_cursor.execute(f"INSERT INTO products(name,price,count) VALUES('{new_name}','{new_price}','{new_count}')")
    Connection.commit()

def Edit(change,change2,change3):
    my_cursor.execute(f"UPDATE products SET {change} = {change2} WHERE name = '{change3}'")
    Connection.commit()

def Remove(product_name):
    my_cursor.execute(f"DELETE FROM products WHERE name = '{product_name}'")
    Connection.commit()

def Serch(product_name):
    result = my_cursor.execute(f"SELECT * FROM Products WHERE name = '{product_name}'")
    product = result.fetchall()
    for i in product:
        return(i)

def Buy(product_name,count):
    print(Serch(product_name))
    my_cursor.execute(f"UPDATE Products SET count = count - {count} WHERE name = '{product_name}'")
    print(Serch(product_name))
    Connection.commit()

def QR_code(product_name):
    product = Serch(product_name)
    img = qrcode.make(product)
    img.save("product_QR_code.png")

Load_Database()
while True:
    Show_Menu()
    choice = int(input())

    if choice == 1:
        Show_List()
    
    elif choice == 2:
        new_name = input("enter a name : ")
        new_price = int(input("enter a price : "))
        new_count = float(input("enter a count : "))
        Add_New(new_name,new_price,new_count)
    
    elif choice == 3:
        change = input("What do you want to change?")
        change2 = input("What should I change it to?")
        change3 = input("What is the name of the product you want to change?")
        Edit(change,change2,change3)
    
    elif choice == 4:
        product_name = input("enter product name: ")
        Remove(product_name)
    
    elif choice == 5:    
        product_name = input("enter product name: ")
        Serch(product_name)
    
    elif choice == 6:
        product_name = input("enter product name: ")
        count = input("How many do you want to buy?")
        Buy(product_name,count)

    elif choice == 7:
        product_name = input("enter name: ")
        QR_code(product_name)

    elif choice == 8:
        exit(0)