from tkinter import *
from tkinter import ttk,messagebox
from db import insert_author,get_authors,delete_author

def author_setup(root,gotoBooks):
	tree = ttk.Treeview(root,columns=('a','b'))
	tree['show'] = 'headings'
	tree.heading('a',text='id')
	tree.heading('b',text='name')
	tree.column('a',width=40,anchor=CENTER)
	tree.column('b',width=100,anchor=CENTER)
	tree.place(x=140,y=10)
	data = get_authors()
	for id,name in data:
		tree.insert("",END,values=(id,name))

	r1 = Frame(root)

	# add section
	l1 = Label(r1,text='Author id')
	l1.pack()
	e1 = Entry(r1,width=12)
	e1.pack()

	l2 = Label(r1,text='Author name')
	l2.pack()
	e2 = Entry(r1,width=12)
	e2.pack()

	def onAdd():
		res = insert_author(e1.get(),e2.get())
		if res:
			tree.insert("",END,values=(e1.get(),e2.get()))
			e1.delete(0,END)
			e2.delete(0,END)
		
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
				resp = delete_author(values[0])
				if resp:
					tree.delete(selected)
			

	b1= Button(r1,text='Delete',command=onDelete)
	b1.pack()

	r1.place(x=10,y=10)

	b2 = Button(root,text="Go to Books",command=gotoBooks)
	b2.pack(side='bottom')