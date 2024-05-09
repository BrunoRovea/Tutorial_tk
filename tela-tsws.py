import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import datetime 

# Cria a janela, mas logo em seguida a fecha
root = Tk()

# Classe das funcionalidade dos botões
class Funcs():
    # Limpa os campos das entrys especificadas
    def limpa_tela(self):
        # Nome destas entrys deve estar igual as entrys da def widgets
        self.step_amount_entry.delete(0, END)
        self.filtro_entry.delete(0, END)
        self.dinicio_entry.delete(0, END)
        self.dfim_entry.delete(0, END)
        self.nomep_entry.delete(0, END)

    def conectTSWS(self):
        print('Conectado ao TSWS no modo desenvolvimento')

    def toogle_snapshot(self):
        print('Inicializando Snapshot')

    def buscar_evt(self):
        print('Buscando eventos')

    def export(self):
        print('Lista exportada')  

    def load_list(self):
        print('Lista carregada')

# A classe Application pode utilizar as funções da classe Funcs
class Application(Funcs):
    # Inicialização
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.lista_frame3()
        # Coloca a abertura de janela em loop para que seja possível interagir com ela
        root.mainloop()

    # Configurações da tela
    def tela(self):
        # Cria um título para a janela
        self.root.title("Busca de eventos TSWS")
        
        # Define a cor de fundo para a janela
        # Cores tkinter que ele entende (ggl)
        self.root.configure(background= '#1e3743')

        # Geometria da janela responsiva
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
   
    # Define os frames da janela   
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground="#759fe6", highlightthickness=3)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.66, relheight = 0.25)

        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground="#759fe6", highlightthickness=3)
        self.frame_2.place(relx = 0.70, rely = 0.02, relwidth = 0.28, relheight = 0.25)
            
        self.frame_3 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground="#759fe6", highlightthickness=3)
        self.frame_3.place(relx = 0.02, rely = 0.28, relwidth = 0.96, relheight = 0.70)

    def widgets_frame1(self):
        self.lb_filtro = Label(self.frame_1, text="Filtro", font=("Arial", 14), bg='#dfe3ee', fg='#107db2')
        self.lb_filtro.place(relx = 0.00, rely = 0.05)

        self.filtro_entry = Entry(self.frame_1)
        self.filtro_entry.place(relx = 0.17, rely = 0.072, relwidth=0.4, relheight=0.12)


        self.lb_inicio = Label(self.frame_1, text="Data de início", font=("Arial", 14), bg='#dfe3ee', fg='#107db2')
        self.lb_inicio.place(relx = 0.00, rely = 0.3)

        self.dinicio_entry = Entry(self.frame_1)
        self.dinicio_entry.place(relx = 0.17, rely = 0.315, relwidth=0.4, relheight=0.12)
        
        data_hora_atual = datetime.datetime.now() - datetime.timedelta(hours=24)

        self.dinicio_entry.insert(0, data_hora_atual.strftime('%d/%m/%Y %H:%M:%S'))



        self.lb_dfim = Label(self.frame_1, text="Data de fim", font=("Arial", 14), bg='#dfe3ee', fg='#107db2')
        self.lb_dfim.place(relx = 0.00, rely = 0.55)

        self.dfim_entry = Entry(self.frame_1)
        self.dfim_entry.place(relx = 0.17, rely = 0.565, relwidth=0.4, relheight=0.12)

        data_hora_atual = datetime.datetime.now() 

        self.dfim_entry.insert(0, data_hora_atual.strftime('%d/%m/%Y %H:%M:%S'))



        self.lb_step_amount = Label(self.frame_1, text="Step_amount", font=("Arial", 14), bg='#dfe3ee', fg='#107db2')
        self.lb_step_amount.place(relx = 0.59, rely = 0.05)

        self.step_amount_entry = Entry(self.frame_1)
        self.step_amount_entry.place(relx = 0.75, rely = 0.05, relwidth=0.2, relheight=0.12)



        # Botões
        self.bt_clear = Button(self.frame_1, text="Limpar", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_clear.place(relx=0.50, rely = 0.8, relwidth = 0.1, relheight = 0.15)



        self.bt_conect = Button(self.frame_1, text="Conectar ao TSWS", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.conectTSWS)
        self.bt_conect.place(relx=0.81, rely = 0.8, relwidth = 0.18, relheight = 0.15)



        self.bt_snapshot = Button(self.frame_1, text="Iniciar Snapshot", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.toogle_snapshot)
        self.bt_snapshot.place(relx=0.35, rely = 0.8, relwidth = 0.15, relheight = 0.15)

        self.snapshot_thread = None  # Thread para o loop de snapshot
        self.snapshot_running = False  # Variável de controle para o loop



        self.bt_buscar = Button(self.frame_1, text="Buscar Eventos", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.buscar_evt)
        self.bt_buscar.place(relx=0.0, rely = 0.8, relwidth = 0.15, relheight = 0.15)



        self.bt_get_list = Button(self.frame_1, text="Carregar Lista snap", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.load_list)
        self.bt_get_list.place(relx=0.15, rely = 0.8, relwidth = 0.2, relheight = 0.15)

    def widgets_frame2(self):

        self.lb_filtro = Label(self.frame_2, text="Nome da pesquisa", font=("Arial", 14), bg='#dfe3ee', fg='#107db2')
        self.lb_filtro.place(relx = 0.25, rely = 0.15)

        self.nomep_entry = Entry(self.frame_2)
        self.nomep_entry.place(relx = 0.05, rely = 0.35, relwidth=0.9, relheight=0.12)

        # Botão buscar e label export
        self.bt_buscar = Button(self.frame_2, text="Exportar .xlsx", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.export)
        self.bt_buscar.place(relx=0.3, rely = 0.55, relwidth = 0.4, relheight = 0.15)

    def lista_frame3(self):
        # Especifica qual frame, tamanho vertical e colunas da tabela de pre-view
        self.listaEvt = ttk.Treeview(self.frame_3, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
                
   
        # Posições rlativas deescritas no widgets
        self.listaEvt.place(relx=0.01, rely=0.020, relwidth=0.96, relheight=0.95)
        

        # Crie um scrollbar vertical
        scrollbar_vertical = ttk.Scrollbar(self.frame_3, orient="vertical", command=self.listaEvt.yview)
        scrollbar_vertical.pack(side="right", fill="y")

        # Associe o scrollbar vertical ao Treeview
        self.listaEvt.config(yscrollcommand=scrollbar_vertical.set)

if __name__ == "__main__":
    Application()
# %%