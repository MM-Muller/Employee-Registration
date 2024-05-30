from tkinter import *


window = Tk()
window.title('Employee Registration')
window.geometry('700x600')
# window.config(bg='white')

frame = Frame(window)
frame.pack()

user_info_frame = LabelFrame(frame, text='User Info')
user_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky=W)

first_name = Label(user_info_frame, text='Nome :')
first_name.grid(row=0, column=0, padx=15, pady=10, sticky=W)

# Pegar informacoes do funcionario
first_name = Entry(user_info_frame)
first_name.grid(row=0, column=1, padx=15, pady=10, sticky=W)

age = Label(user_info_frame, text='Idade :')
age.grid(row=0, column=2, padx=5, pady=10, sticky=W)

age = Entry(user_info_frame)
age.grid(row=0, column=3, padx=15, pady=10, sticky=W)

ident = Label(user_info_frame, text='ID :')
ident.grid(row=1, column=0, padx=15, pady=10, sticky=W)

ident = Entry(user_info_frame)
ident.grid(row=1, column=1, padx=15, pady=10, sticky=W)

teste = Label(user_info_frame, text='teste :')
teste.grid(row=1, column=2, padx=5, pady=10, sticky=W)

teste = Entry(user_info_frame)
teste.grid(row=1, column=3, padx=15, pady=10, sticky=W)

# Botao para cada opcao
clean_bt = Button(user_info_frame, text='Apagar informacoes')
clean_bt.grid(row=2, column=0, padx=15, pady=10)

change_bt = Button(user_info_frame, text='Alterar Usuarior')
change_bt.grid(row=2, column=1, padx=15, pady=10)

delete_bt = Button(user_info_frame, text='Deletar Usuario')
delete_bt.grid(row=2, column=2, padx=15, pady=10)

search_bt = Button(user_info_frame, text='Apagar informacoes')
search_bt.grid(row=2, column=3, padx=15, pady=10)

window.mainloop()
