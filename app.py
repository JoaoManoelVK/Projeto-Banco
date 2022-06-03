import sqlite3
from tkinter import Text
import PySimpleGUI as sg
sg.theme('SandyBeach')

class telaPython:
    def __init__(self):
        #layout
        layoutinicio = [
            [sg.Text('Selecione uma Opção')],
            [sg.Button('Criar Conta',key='Criar_Conta'), sg.Button('Acessa Conta',key='Acessar_conta')],
        ]

        layoutcadastro = [
            [sg.Text('Cadastre suas Informações')],
            [sg.Text('Nome:'),sg.Input(size=(20,0),key='nome')],
            [sg.Text('CPF :'),sg.Input(size=(20,0),key='nome')],
            [sg.Text('Endereco:'),sg.Input(size=(20,0),key='nome')],
            [sg.Text('Numero:'),sg.Input(size=(20,0),key='nome')],
            [sg.Text('Tipo de Conta:'),sg.Input(size=(20,0),key='nome')],
            [sg.Button('Seguinte',key='CadastroS')],
        ]

        layoutentrada = [
            [sg.Text('Insira o Login')],
            [sg.Text('Nome:'),sg.Input(size=(20,0),key='nome')],
            [sg.Text('Senha :'),sg.Input(size=(20,0),key='nome')],
            [sg.Button('Login',key='Logon')],
        ]
        layouttela = [
            [sg.Text('Selecione uma Opção')],
            [sg.Button('Deposito',key='Deposito'), sg.Button('Saque',key='Saque'),sg.Button('Extrato',key='Extrato')],
        ]
        layoutdeposito = [
            [sg.Text('Saldo: ???')],
            [sg.Text('Digite a quantidade a ser depositada')],
            [sg.Input(size=(20,0),key='QtDeposito')],
            [sg.Button('Deposite',key='BTdeposit')]
        ]
        layoutsaque = [
            [sg.Text('Saldo: ???')],
            [sg.Text('Digite o valor a ser retirado')],
            [sg.Input(size=(20,0),key='QtSaque')],
            [sg.Button('Sacar',key='BTsaque')]
        ]
        layoutextrato = [
            [sg.Text('Saques Efetuados')],
            [sg.Text('-----')],
            [sg.Text('Depositos Efetuados')],
            [sg.Text('-----')],
            [sg.Button('Voltar',key='BTextractvoltar')]
        ]



        #janela
        janela = sg.Window("Banco").layout(layoutinicio)
        janelacadastro = sg.Window('Cadastro').layout(layoutcadastro)
        janelalogin = sg.Window('Login').layout(layoutentrada)
        janelainicial = sg.Window('Banco').layout(layouttela)
        janeladeposito = sg.Window('Deposito').layout(layoutdeposito)
        janelasaque = sg.Window('Saque').layout(layoutsaque)
        janelaextrato = sg.Window('Extrato').layout(layoutextrato)
        
        while True:  # Event Loop
            event, values = janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Criar_Conta':
                janela.close()
                janelacadastro.read()
                event, values = janelacadastro.read()
                if event == 'CadastroS':
                    janelacadastro.close()
                    janelalogin.read()
                    event, values = janelalogin.read()
            elif event == 'Acessar_conta':
                janela.close()
                janelalogin.read()
                event, values = janelalogin.read()
            if event == 'Logon':
                janelalogin.close()
                janelainicial.read()
                event, values = janelainicial.read()
                if event == 'Deposito':
                    janelainicial.close()
                    janeladeposito.read()
                    event, values = janeladeposito.read()
                    if event == 'BTdeposit':
                        janeladeposito.close()
                        janelainicial.read()
                        event, values = janelainicial.read()
                if event == 'Saque':
                    janelainicial.close()
                    janelasaque.read()
                    event, values = janelasaque.read()
                    if event == 'BTdeposit':
                        janeladeposito.close()
                        janelainicial.read()
                        event, values = janelainicial.read()
                if event == 'Extrato':
                    janelainicial.close()
                    janelaextrato.read()
                    event, values = janelaextrato.read()
                    if event == 'BTdeposit':
                        janeladeposito.close()
                        janelainicial.read()
                        event, values = janelainicial.read()
                



tela = telaPython()
tela.iniciar()