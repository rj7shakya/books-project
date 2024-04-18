from tkinter import *
from author import author_setup
from books import book_setup

root = Tk()
books = Frame(root)
authors = Frame(root)

books.place(x=0,y=0,relheight=1,relwidth=1)
authors.place(x=0,y=0,relheight=1,relwidth=1)
books.lift()

author_setup(authors,lambda :books.lift())
book_setup(books,lambda :authors.lift())

root.geometry('320x300')
root.mainloop()


