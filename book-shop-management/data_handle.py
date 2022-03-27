import functions
import os
def create():
    import sqlite3
    books = sqlite3.connect('books.db')
    curbooks = books.cursor()
    
    sql=("CREATE TABLE books_detail (title TEXT (50) NOT NULL,author TEXT (50),price INTEGER);")

    try:
        curbooks.execute(sql)
        print("Database with name books.db having table named as books_detail created successfully")

    except:
        print ("Error in creation of new database")
        print ("Check if database with name books.db already exist")

    books.close()
    input()
    os.system('cls')
    functions.home()
    


def insert():
    import sqlite3
    books = sqlite3.connect('books.db')
    curbooks = books.cursor()

    book_title = str(input("Enter the title of the book: "))
    book_author = str(input("Enter the author of the book: "))
    book_price = int(input("Enter the price of the book: "))

    try:
        curbooks.execute("INSERT INTO books_detail (title, author, price) VALUES (?,?,?);",(book_title,book_author,book_price))
        books.commit()
        print ("Record inserted successfully")
    
    except:
        print ("Error in insertion operation")
        books.rollback()

    books.close()
    input()
    os.system('cls')
    functions.home()
    


def update():
    import sqlite3
    books = sqlite3.connect('books.db')

    book_name = input("Enter name of the book which is to be updated: ")
    sql = "SELECT * from books_detail WHERE title = '"+book_name+"';"
    curbooks = books.cursor()
    curbooks.execute(sql)
    record = curbooks.fetchone()
    
    print("Present details of the book are given below:")
    print(record)
    
    print("Enter new details to replace the above existing details:")
    a_name = str(input("Enter author of the book: "))
    cost = int(input("Enter price of the book: "))
    sql1 = "UPDATE books_detail SET author = '"+a_name+"' WHERE title = '"+book_name+"';"
    sql2 = "UPDATE books_detail SET price = '"+str(cost)+"' WHERE title = '"+book_name+"';"

    try:
        curbooks.execute(sql1)
        curbooks.execute(sql2)
        books.commit()
        print ("Record updated successfully")
    
    except:
        print ("Error in update operation")
        books.rollback()

    books.close()
    input()
    os.system('cls')
    functions.home()
    


def view():
    import sqlite3
    books = sqlite3.connect('books.db')

    book_name = input("Enter name of the book which is to be detailed: ")
    sql = "SELECT * from books_detail WHERE title = '"+book_name+"';"
    curbooks = books.cursor()
    curbooks.execute(sql)
    record = curbooks.fetchone()
    
    print("Present details of the book are given below:")
    print(record)

    books.close()
    input()
    os.system('cls')
    functions.home()
    

    
    
