from tkinter import *
from tkinter import ttk


window = Tk()
window.title('Employee Registration')
window.geometry('700x500')

frame = Frame(window)
frame.pack()

# Primeira parte
user_info_frame = LabelFrame(frame, text='User Info')
user_info_frame.grid(row=0, column=0, padx=15, pady=20, sticky=W)

# Pegar informacoes do funcionario
name = Label(user_info_frame, text='Nome :')
name.grid(row=0, column=0, padx=15, pady=10, sticky=W)

name = Entry(user_info_frame)
name.grid(row=0, column=1, padx=15, pady=10, sticky=W)

age = Label(user_info_frame, text='Idade :')
age.grid(row=0, column=2, padx=5, pady=10, sticky=W)

age = Entry(user_info_frame)
age.grid(row=0, column=3, padx=15, pady=10, sticky=W)

ident = Label(user_info_frame, text='ID :')
ident.grid(row=1, column=0, padx=15, pady=10, sticky=W)

ident = Entry(user_info_frame)
ident.grid(row=1, column=1, padx=15, pady=10, sticky=W)

role = Label(user_info_frame, text='Funcao :')
role.grid(row=1, column=2, padx=5, pady=10, sticky=W)

role = Entry(user_info_frame)
role.grid(row=1, column=3, padx=15, pady=10, sticky=W)

# Botao para cada opcao
clean_bt = Button(user_info_frame, text='Apagar informacoes')
clean_bt.grid(row=2, column=0, padx=15, pady=10)

change_bt = Button(user_info_frame, text='Alterar Usuarior')
change_bt.grid(row=2, column=1, padx=15, pady=10)

delete_bt = Button(user_info_frame, text='Deletar Usuario')
delete_bt.grid(row=2, column=2, padx=15, pady=10)

search_bt = Button(user_info_frame, text='Buscar Usuario')
search_bt.grid(row=2, column=3, padx=15, pady=10)

# Segunda parte
show_info_frame = LabelFrame(frame, text='View users information')
show_info_frame.grid(row=1, column=0, padx=15, pady=20, sticky=W)

client_list = ttk.Treeview(show_info_frame, columns=('Name', 'Age', 'Ident', 'Role'))
client_list.grid(row=0, column=0, padx=10, columnspan=1, pady=10,sticky=W)

client_list.heading("#0", text="")
client_list.column("#0", width=0, stretch=NO)
client_list.heading("#1", text='Name')
client_list.column("#1", width=140)
client_list.heading("#2", text='Age')
client_list.column("#2", width=140)
client_list.heading("#3", text='Ident')
client_list.column("#3", width=140)
client_list.heading("#4", text='Role')
client_list.column("#4", width=140)

window.mainloop()
