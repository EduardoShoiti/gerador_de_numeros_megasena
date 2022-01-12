from tkinter import *
import gerar_num as gn

class App:
    def __init__(self, master):

        def mostrar_num():
            tx_numeros.delete(1.0, "end")
            tx_numeros.insert(1.0, gn.gerar())

        def copiar_para_area_de_transferencia():
            clip = Tk()
            clip.withdraw()
            clip.clipboard_clear()
            clip.clipboard_append(gn.megasena)
            clip.destroy()

        self.widget1 = Frame(master)
        self.widget1.pack()

        lb_Mega_Sena = Label(self.widget1, text="Gerador de Números")
        lb_Mega_Sena["font"] = ("Verdana", "15", "bold")
        lb_Mega_Sena.grid(column=0, row=0, pady=15)

        tx_numeros = Text(self.widget1, height=1, width=15)
        tx_numeros["font"] = ("Verdana", "13", "bold")
        tx_numeros.grid(column=0, row=1, pady=15)

        btn_Gerar = Button(self.widget1, text="GERAR", background="#000000", foreground="#ffffff", command=mostrar_num)
        btn_Gerar["font"] = ("Verdana", "14", "bold")
        btn_Gerar.grid(column=0, row=2, pady=15)

        btn_copiar = Button(self.widget1, text="Copiar Números", background="#248d27", foreground="#ffffff", command=copiar_para_area_de_transferencia)
        btn_copiar["font"] = ("Verdana", "14", "bold")
        btn_copiar.grid(column=0, row=3, pady=10)


root = Tk()
root.geometry('300x300')
root.title("Mega Sena")
root.resizable(0, 0)
App(root)
root.mainloop()