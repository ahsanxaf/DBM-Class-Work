import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Student Records")

columns = ('s_id', 's_name', 's_degree', 's_session')
data = [
    [1, 'Ahsan', 'BSIT', 2018],
    [2, 'Usman', 'BSCS', 2020],
    [3, 'Ali', 'BBA', 2021]
]

tree = ttk.Treeview(root)
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
scrollbar.grid(row=0, column=1, sticky='ns')
root.mainloop()
