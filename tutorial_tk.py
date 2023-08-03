#%%
# import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3 


# Cria a janela, mas logo em seguida a fecha
root = Tk()

# Classe das funcionalidade dos botões
class Funcs():
    # Limpa os campos das entrys especificadas
    def limpa_tela(self):
        # Nome destas entrys deve estar igual as entrys da def widgets
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    # Conecta bd
    def conecta_bd(self):
  
    
        # Conecta ao bd clientes
        self.conn = sqlite3.connect('clientes.db')
        # Variável resume a função do sqlite3 ?
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')
    # desconecta bd
    def desconecta_bd(self):
    
    
        self.conn.close(); print('Desconectando ao banco de dados')
    # Cria o bd
    def montaTabelas(self):


        # Executa a função que executa o bd, e printa o status
        self.conecta_bd()


        ### Criar tabela, ou o bd
        # Cria uma tabela clientes caso ñ exista
        # cod como primary key (?)
        # nome_cliente do tipo CHAR com 40 caracteres e ñ pode ser nula
        # telefone tipo inteiro com 20 caracteres
        # cidade tipo char com 40 caracteres
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)

        # Commit para validar essa info no bd
        self.conn.commit(); print('Banco de dados criado')
        
        # Executa a função que desconecta o banco de dados
        self.desconecta_bd()


# A classe Application pode utilizar as funções da classe Funcs
class Application(Funcs):
    # Inicialização
    def __init__(self):
        # Isso aq ñ sei o que significa, nem esse self
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()

        # Coloca a abertura de janela em loop para que se possa interagir com ela
        root.mainloop()
    # Função para criar as configurações de tela
    def tela(self):
        # Cria um título para a janela
        self.root.title("Criação de scratchpads utilizando a ferramenta SOELIST")
        
        # Define a cor de fundo para a janela
        # Cores tkinter que ele entende (ggl)
        self.root.configure(background= '#1e3743')

        # Geometria da janela responsiva
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        # Máximo e mínimo de responsividade
        self.root.maxsize(width= 900, height=700)
        self.root.minsize(width=500, height=400)
    # Criação de frames da tela (subdivisões)
    def frames_da_tela(self):




        # Configurações do frame, bd é o border, bg é a cor do interior do border
        # # high são as configurações de borda
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', 
                             highlightbackground="#759fe6", highlightthickness=3)

        # place pack grid método de alocação dos objetos na tela
        # relx = 1 totalmente a direita | relx = 0 totalmente a esquerda
        # relwidth largura do frame | relheight altura do frame
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)

        # Esse frame começará na metade da janela, rely = 0.5
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', 
                             highlightbackground="#759fe6", highlightthickness=3)

        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)
    # Ctrl + ; comenta a seleção
    def widgets_frame1(self):


        # Especifica em qual frame o botão estará lotado
        # bd -> tipo de borda, e é um inteiro
        # bg -> cor do botão, cores padrão ñ são mt confortáveis, utilizar hexadecimal
        # dg -> Cor do texto do botão
        # font('nome da fonte', tamanho da fonte, 'itálico')
        # command executa os comandos dentro da função self.limpa_tela
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        # Sem fonte e estilização, levels dos frames e imputs dos botões posterior
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.6, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely = 0.1, relwidth = 0.1, relheight = 0.15)


        # Criação da label e entrada do código
        # Novamente, deve-se espevificar o frame onde esta label estará
        # bg define a cor da label, ai o texto ñ fica 'destacado'
        # fg é a cor da fonte das labels
        self.lb_codigo = Label(self.frame_1, text = "Código", bg = '#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx = 0.05, rely = 0.05)

        # Criando a enry (imput)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.05, rely = 0.15, relwidth=0.08)


        self.lb_nome = Label(self.frame_1, text = "Nome", bg = '#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx = 0.05, rely = 0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely = 0.45, relwidth=0.8)


        self.lb_telefone = Label(self.frame_1, text = "Telefone", bg = '#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx = 0.05, rely = 0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx = 0.05, rely = 0.7, relwidth=0.4)


        self.lb_cidade = Label(self.frame_1, text = "Cidade", bg = '#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx = 0.5, rely = 0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx = 0.5, rely = 0.7, relwidth=0.4)
    # Criação da lista de pre-view    
    def lista_frame2(self):


        # Especifica qual frame, tamanho vertical e colunas da tabela de pre-view
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        
        # Especifica o nome de cada coluna
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        # Isso aq é meio confuso, divide o número 500 nas proporções de cada coluna
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        # Posições rlativas deescritas no widgets
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Definição do scroll da lista, define o frame e a orientação vertical
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        # Atribui o scroll criado a listaCli
        self.listaCli.configure(yscroll=self.scrollLista.set)
        # Posição relativa do scroll
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

Application()

# Continuar na aula 9 do cidadão