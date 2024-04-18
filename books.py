from tkinter import *
from tkinter import ttk,messagebox
from db import get_books,insert_book,delete_book

def book_setup(root,gotoAuthors):
	tree = ttk.Treeview(root,columns=('a','b','c'))
	tree['show'] = 'headings'
	tree.heading('a',text='id')
	tree.heading('b',text='name')
	tree.heading('c',text='author')
	tree.column('a',width=40,anchor=CENTER)
	tree.column('b',width=60,anchor=CENTER)
	tree.column('c',width=60,anchor=CENTER)
	tree.place(x=140,y=10)
	# data = [(1,'A','ram'),(2,'B','shyam')]
	data = get_books()
	for id,name,author in data:
		tree.insert("",END,values=(id,name,author))

	r1 = Frame(root)

	# add section
	l1 = Label(r1,text='Book id')
	l1.pack()
	e1 = Entry(r1,width=12)
	e1.pack()

	l2 = Label(r1,text='Book name')
	l2.pack()
	e2 = Entry(r1,width=12)
	e2.pack()

	l3 = Label(r1,text='Author id')
	l3.pack()
	e3 = Entry(r1,width=12)
	e3.pack()

	def onAdd():
		res = insert_book(e1.get(),e2.get(),e3.get())
		if res:
			tree.insert("",END,values=get_books()[-1])
			e1.delete(0,END)
			e2.delete(0,END)
			e3.delete(0,END)
		
	b2= Button(r1,text='Add',command=onAdd)
	b2.pack()

	# delete button
	def onDelete():
		selected = tree.focus()
		if not selected:
			messagebox.askokcancel("a","No Item Selected!!")
		else:
			res = messagebox.askyesno("b","Are you sure you want to delete?")
			if res:
				values = tree.item(selected, "values")
				resp = delete_book(values[0])
				if resp:
					tree.delete(selected)
			

	b1= Button(r1,text='Delete',command=onDelete)
	b1.pack()

	r1.place(x=10,y=10)

	b2 = Button(root,text="Go to Authors",command=gotoAuthors)
	b2.pack(side='bottom')