import tkinter as tk
import model as mdb
from tkinter import ttk

db = mdb.Database
db.connection(db)

root = tk.Tk()
root.title("Student Record")
root.geometry('800x500')

frameLeft = tk.Frame(root, height=200, width=250)
frameLeft.pack(side=tk.LEFT, fill=tk.Y)
# frame2 = tk.Frame(root, height=200, width=250)
# frame2.pack(side=tk.LEFT, fill=tk.X)
frame_right = tk.Frame(root, height=200, width=200)
frame_right.pack(side=tk.RIGHT, fill=tk.Y)
frame3 = tk.Frame(root, height=500, width=400)
frame3.pack(side=tk.TOP, fill=tk.Y)

label_id = tk.Label(frameLeft, text='Student ID:')
label_id.grid(row=0, column=0, padx=5, pady=10)
entry_id = tk.Entry(frameLeft, font=('Arial', 12))
entry_id.grid(row=0, column=1, padx=5)

label_name = tk.Label(frameLeft, text='Student Name:')
label_name.grid(row=1, column=0, padx=5, pady=10)
entry_name = tk.Entry(frameLeft, font=('Arial', 12))
entry_name.grid(row=1, column=1, padx=5)

label_degree = tk.Label(frameLeft, text='Degree:')
label_degree.grid(row=2, column=0, padx=5, pady=10)
entry_degree = tk.Entry(frameLeft, font=('Arial', 12))
entry_degree.grid(row=2, column=1, padx=5)

label_session = tk.Label(frameLeft, text='Session:')
label_session.grid(row=3, column=0, padx=5, pady=10)
entry_session = tk.Entry(frameLeft, font=('Arial', 12))
entry_session.grid(row=3, column=1, padx=5)

label_search = tk.Label(frame_right, text='Search Data by ID:')
label_search.grid(row=3, column=0, padx=5, pady=10)
entry_search = tk.Entry(frame_right, font=('Arial', 12))
entry_search.grid(row=3, column=1, padx=10)

####################################### BUTTONS ###################################################
search = tk.Button(frame_right, text='SEARCH', font=20, width=20, height=2, bg='green', fg='white',
                   command=lambda: searchData())
search.grid(row=4, column=1, padx=10)

update = tk.Button(frameLeft, text='UPDATE', font=20, width=20, height=2, bg='blue', fg='white',
                   command=lambda: updateData())
update.grid(row=6, column=0, padx=10)

add = tk.Button(frameLeft, text='ADD IN TREE', font=20, width=20, height=2, bg='yellow', fg='white',
                command=lambda: addRecordToTreeView())
add.grid(row=6, column=1, padx=10)

removeAll = tk.Button(frameLeft, text='REMOVE ALL', font=20, width=20, height=2, bg='red', fg='white',
                      command=lambda: removeAllRecord())
removeAll.grid(row=7, column=0, padx=10)

removeOne = tk.Button(frameLeft, text='REMOVE ONE', font=20, width=20, height=2, bg='#293949', fg='white',
                      command=lambda: removeOneRecord())
removeOne.grid(row=7, column=1, padx=10)

removeMany = tk.Button(frameLeft, text='REMOVE MANY', font=20, width=20, height=2, bg='cyan', fg='white',
                       command=lambda: removeManyRecords())
removeMany.grid(row=8, column=0, padx=10)

addToDB = tk.Button(frameLeft, text='ADD TO DATABASE', font=20, width=20, height=2, bg='brown', fg='white',
                       command=lambda: addIntoDatabase())
addToDB.grid(row=8, column=1, padx=10)

####################################### BUTTONS ###################################################

columns = ('s_id', 's_name', 's_degree', 's_session')
data = [
    [1, 'Ahsan', 'BSIT', 2018],
    [2, 'Usman', 'BSCS', 2020],
    [3, 'Ali', 'BBA', 2021]
]

tree = ttk.Treeview(frame3)
tree['columns'] = columns
tree.column('#0', width=0, stretch=tk.NO)
tree.column(columns[0], anchor=tk.CENTER, width=100)
tree.column(columns[1], anchor=tk.CENTER, width=100)
tree.column(columns[2], anchor=tk.CENTER, width=100)
tree.column(columns[3], anchor=tk.CENTER, width=100)

tree.heading('s_id', text='Student ID')
tree.heading('s_name', text='Student Name')
tree.heading('s_degree', text='Student Degree')
tree.heading('s_session', text='Student Session')

count = 0
for record in data:
    tree.insert(parent='', index='end', iid=count, values=(record[0], record[1], record[2], record[3]))
    count += 1

tree.grid(row=0, column=0, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)


def searchData():
    std_id = str(entry_search.get())
    data = db.getData(db, std_id)
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_degree.delete(0, tk.END)
    entry_session.delete(0, tk.END)
    entry_id.insert(0, data[0][0])
    entry_name.insert(0, data[0][1])
    entry_degree.insert(0, data[0][2])
    entry_session.insert(0, data[0][3])
    entry_search.delete(0, tk.END)


def updateData():
    std_id = str(entry_id.get())
    std_name = entry_name.get()
    std_degree = entry_degree.get()
    std_session = str(entry_session.get())
    db.updateData(db, std_id, std_name, std_degree, std_session)
    print("Updated Successfully")


def addIntoDatabase():
    std_id = str(entry_id.get())
    std_name = entry_name.get()
    std_degree = entry_degree.get()
    std_session = str(entry_session.get())
    db.insertData(db, std_id, std_name, std_degree, std_session)
    print("Data added successfully")


def addRecordToTreeView():
    global count
    tree.insert(parent='', index='end', iid=count,
                values=(entry_id.get(), entry_name.get(), entry_degree.get(), entry_session.get()))
    count += 1
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_degree.delete(0, tk.END)
    entry_session.delete(0, tk.END)


def removeAllRecord():
    for record in tree.get_children():
        tree.delete(record)


def removeOneRecord():
    tree.delete(tree.selection()[0])


def removeManyRecords():
    x = tree.selection()
    for record in x:
        tree.delete(record)


root.mainloop()
