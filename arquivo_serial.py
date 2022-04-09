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
    RetornoLeituraSerial.place(x=740,y=112)
    RetornoLeituraSerial['bg'] = 'light blue'

def EnviarDados():
    print(EnviarDadosSerial.get())
    try:
        ser = serial.Serial('COM3', 9600)
        while True:
            ser.write(EnviarDadosSerial.get())
            if ser.inWaiting() > 0:
                ser.close()
                break
    except:
        print("Erro ao enviar mensagem")
        MensagemErroEnvio = Label(janela, text="Erro ao enviar mensagem para a porta serial")
        MensagemErroEnvio.place(x=550,y=230)
        MensagemErroEnvio['bg'] = 'light blue'


#cria uma janela Tkinter
janela = tk.Tk()
janela.title("Leitura e envio de dados para a porta Serial")
janela['bg'] = 'light blue'

#define parâmetros de largura e altura da janela
janela.geometry("1300x700+0+0")

TituloLerPortaSerial = Label(janela, text="Leitura da Porta Serial", font=('calibri 18'))
TituloLerPortaSerial.place(x=550, y=50)
TituloLerPortaSerial['bg'] = 'light blue'

#Cria um botão que chamará a função LeituraSerial ao ser clicado
LerPortaSerial = Button(janela, text="Ler porta serial", command=LeituraSerial, width=25)
LerPortaSerial.place(x=550, y=110)
LerPortaSerial['bg'] = '#00FF7F'

TituloEnviarDadosPortaSerial = Label(janela, text="Leitura da Porta Serial", font=('calibri 18'))
TituloEnviarDadosPortaSerial.place(x=550, y=50)
TituloEnviarDadosPortaSerial['bg'] = 'light blue'

EnviarDadosSerial = Entry(janela, width=25)
EnviarDadosSerial.place(x=550, y=200)

BotaoEnviarDadosSerial = Button(janela, text="Enviar dados", command=EnviarDados)
BotaoEnviarDadosSerial.place(x=710,y=197)
BotaoEnviarDadosSerial['bg'] = '#00FF7F'


#Cria um loop na janela para ela não ser fechada automaticamente
janela.mainloop()
