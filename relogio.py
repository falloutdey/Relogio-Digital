from tkinter import *
from time import *

janela = Tk()
janela.title('Relógio com Python')
janela['bg'] = 'black'
janela.geometry('700x500')
janela.resizable(False, False)
texto = Label(janela, font = ('Montserrat', 65), fg = 'red', pady=220,bg='black')

def horario():
    hora = strftime('%H:%M:%S')
    texto.config(text = hora)
    texto.after(1000, horario)

texto.pack(anchor='center')
horario()

mainloop()
