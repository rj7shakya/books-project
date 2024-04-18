import psycopg2
from tkinter import messagebox
connection = psycopg2.connect(
            host='localhost',
            database='xyz',
            user='test',
            password='test123'
        )


# authors
def insert_author(id,name):
  try:
    cursor = connection.cursor()
    cursor.execute(f"insert into author values({id},'{name}')")
    connection.commit()
    cursor.close()
    return True
    
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False  

def get_authors():
  cursor = connection.cursor()
  cursor.execute("select * from author")
  rows = cursor.fetchall()
  cursor.close()
  return rows
  
def delete_author(id):
  try:
    cursor = connection.cursor()
    cursor.execute(f"delete from author where id = {id}")
    connection.commit()
    cursor.close()
    return True
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False
  
  
  
# books
def insert_book(id,name,author_id):
  try:
    cursor = connection.cursor()
    cursor.execute(f"""insert into books(id,book,author_id) 
                   values({id},'{name}',{author_id})""")
    connection.commit()
    cursor.close()
    return True
    
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False
  
def get_books():
  cursor = connection.cursor()
  cursor.execute(f"""select books.id, books.book as book_name, 
                author.name as author_name
                from books inner join author 
                on books.author_id = author.id;""")
  rows = cursor.fetchall()
  cursor.close()
  return rows

def delete_book(id):
  try:
    cursor = connection.cursor()
    cursor.execute(f"delete from books where id = {id}")
    connection.commit()
    cursor.close()
    return True
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False