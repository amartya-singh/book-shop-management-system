import data_handle
import os

def billing():
    bill = 0
    choice = "y"
    import sqlite3
    books = sqlite3.connect('books.db')
    curbooks = books.cursor()
    

    while choice=='y' or choice=='Y':
        book_name = input("Enter name of the book which is to be bought: ")
        sql = "SELECT price from books_detail WHERE title = '"+book_name+"';"
        qty = input("Enter the number of units you want to buy: ")
    
        curbooks.execute(sql)
        price=max(curbooks.fetchone())
        price=int(price)
        quantity=int(qty)
    
        bill=(price*quantity)+bill        

        choice = input("Do you want to buy more books Y or N: ")
        
    
    books.close()
    print(bill)
    input()
    os.system('cls')
    home()


def home():
    print("Please enter a valid choice:")
    print("1: To view details of the available books")
    print("2: To checkout with books")
    print("3: To add new book")
    print("4: To update existing details of the book")
    print("5: To create database with name books.db [for first time use only]")

    c = input("Enter Your Choice: ")
    choice= int(c)
    if choice==1:
        data_handle.view()
    elif choice==2:
        billing()
    elif choice==3:
        data_handle.insert()
    elif choice==4:
        data_handle.update()
    elif choice==5:
        data_handle.create()
    else:
        print("Enter a valid choice")

    
    

    
    
