#importa as bibliotecas necessárias para dentro do código
import serial
import tkinter as tk
from tkinter import *

def LeituraSerial():
    print("Função acessada")
    #Função de tratamento de erros
    try:
        #inicializa a comunicação com a porta serial ('PORTA SERIAL', 'VELOCIDADE DE COMUNICAÇÃO')
        ser = serial.Serial('COM3', 9600)

        #lê e armazena tudo o que está escrito em uma mesma linha na porta serial
        valor_recebido = ser.readline()

        #fecha a comunicação serial
        ser.close()

    #caso a lógica executada dentro do 'try' tenha algum erro é executado esse bloco
    except:
        print("Erro ao inicializar porta serial")
        valor_recebido = "Erro"

    #Cria uma variável que exibirá o que foi lido na porta serial
    RetornoLeituraSerial = Label(janela, text=valor_recebido)
    RetornoLeituraSerial.place(x=200,y=100)

#cria uma janela Tkinter
janela = tk.Tk()

#define parâmetros de largura e altura da janela
janela.geometry("1300x700+0+0")

#Cria um botão que chamará a função LeituraSerial ao ser clicado
LerPortaSerial = Button(janela, text="Ler porta serial", command=LeituraSerial)
LerPortaSerial.place(x=100, y=100)

#Cria um loop na janela para ela não ser fechada automaticamente
janela.mainloop()
