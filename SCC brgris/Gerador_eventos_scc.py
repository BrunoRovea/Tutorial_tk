#%%
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:54:41 2023

@author: brgris
"""
import tkinter as tk
from tkinter import filedialog, Entry, Label
import pandas as pd
import os

import sys
print(sys.executable)
caminho_arquivo_selecionado = ""  # Variável global para armazenar o caminho do arquivo

 
def obter_caminho():
    global caminho_arquivo_selecionado
    caminho_arquivo_selecionado = filedialog.askopenfilename(filetypes=[('Arquivos Excel', '*.xlsx')])
    campo_caminho.delete(0, tk.END)
    campo_caminho.insert(tk.END, caminho_arquivo_selecionado)
    print(caminho_arquivo_selecionado)
#    janela.destroy()
#    janela.quit()

def executar():
    global cenario_aux
    caminho_arquivo = caminho_arquivo_selecionado
    cenario = pd.read_excel(caminho_arquivo)  # realiza a leitura dos arquivos .xlsx
    cenario_aux = cenario.copy()
    cenario_aux['Element'] = cenario_aux['Element'].astype(str)
    cenario_aux['msg'] = cenario_aux['msg'].astype(str)
    cenario_aux =  cenario_aux.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    cenario_aux.loc[cenario_aux['Info'] != 'MvMoment', 'mensagem'] = 'TA,' + cenario_aux['B1'] + ',' + cenario_aux['B2'] + ',' + cenario_aux['B3'] + ',' + cenario_aux['Element'] + ',' + cenario_aux['Info'] + ',' + '\nsta ' + cenario_aux['msg']+ ' tra'
    cenario_aux.loc[cenario_aux['Info'] == 'MvMoment', 'mensagem'] = 'TA,' + cenario_aux['B1'] + ',' + cenario_aux['B2'] + ',' + cenario_aux['B3'] + ',' + cenario_aux['Element'] + ',' + cenario_aux['Info'] + ',' + '\nval '+cenario_aux['msg'] + ' tra'
    output_filename = os.path.splitext(caminho_arquivo)[0] + '.txt'
    caminho_result.delete(0, "end")
    caminho_result.insert(0, caminho_arquivo)
    cenario_aux['mensagem'].to_csv(output_filename, sep='\t',  index=False, header=False)
    with open(output_filename, 'r', encoding='utf-8') as f:
         content = f.read()
    with open(output_filename, 'w', encoding='utf-8') as f:
         f.write(content.replace('"', ''))

 

def display_result():
    display=cenario_aux
    max_lengths =  display.astype(str).applymap(len).max()

# Step 2: Convert each element in the DataFrame to a string
    display =  display.astype(str)

# Step 3: Pad each string to the left with spaces to match the maximum size
    for col in  display.columns:
        display[col] =  display[col].apply(lambda x: x.ljust(max_lengths[col]))

    # Clear the text widget
    campo_result.delete(1.0, "end")
    # Insert the DataFrame into the text widget
    campo_result.insert("end", display.to_string(index=False,justify='left'))


def close_window():
    janela.destroy()
    janela.quit()

janela = tk.Tk()
janela.title("Gerador de Eventos SCC")
janela.geometry("800x500")

# Campo para exibir o caminho do arquivo
campo_caminho = tk.Entry(janela, width=50)
campo_caminho.pack(pady=10)

# Botão para obter o caminho do arquivo
botao_obter = tk.Button(janela, text="Selecionar Arquivo (.xlsx)", command=obter_caminho, width=20)
botao_obter.pack(pady=5)


# Botão para executar o código
botao_executar = tk.Button(janela, text="Executar", command=executar, width=20)
botao_executar.pack(pady=5)

display_button = tk.Button(janela, text="Pré Visualização", command=display_result, width=20)
display_button.pack(pady=10)

# Campo para mostrar o resultado

campo_result = tk.Text(janela, height=10, width=100)
campo_result.pack(pady=10)
scrollbar_x = tk.Scrollbar(janela, orient="horizontal", command=campo_result.xview)
scrollbar_x.pack(fill="x")

    # Configure the text widget to use the horizontal scrollbar
campo_result.configure(xscrollcommand=scrollbar_x.set)

font_family = 'Consolas'
font_size = 10
campo_result.configure(font=(font_family, font_size))
campo_result.configure(wrap="none")

descricao_label = Label(janela, text="O arquivo de saída está salvo em:")
descricao_label.pack(pady=5)

caminho_result = Entry(janela, width=50)
caminho_result.pack(pady=10)

close_button = tk.Button(janela, text="Fechar", command=close_window, width=20)
close_button.pack(pady=10)

janela.mainloop()
# %%
