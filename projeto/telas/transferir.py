from tkinter import *

import projeto.funcionalidades.checagens as checagens
import projeto.funcionalidades.alertas as alertas
import json
from projeto.funcionalidades.registrar_operacoes import registrar

AZUL_CLARO = '#88D9F2'
COR_RETANGULO = '#D1F1FB'
FONTE_TITULOS = ('arial',30,'bold')
FONTE_COMUM = ('arial',15,'normal')
COR_BUTTONS = 'white'



win_width, win_height = 364, 516

class Transferir:
    def __init__(self):
        self.conta_logada = checagens.conta_logada()
        self.janela = Tk()
        self.tela()
        self.logo()
        self.retangulo()
        self.textos()
        self.inputs_()
        self.botoes()
        self.janela.mainloop()

    def tela(self):
        self.janela.title('Saque')
        self.janela.minsize(width=win_width, height=win_height)
        self.janela.config(background=AZUL_CLARO)
        self.janela.resizable(False, False)

    def logo(self):
        self.img_logo = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\logo.png')
        self.img_retangulo = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\fundo_interno.png'
)

        self.canvas = Canvas(width=93, height=85, highlightthickness=0, bg=AZUL_CLARO)
        self.logo = self.canvas.create_image(47, 43, image=self.img_logo)
        self.canvas.place(x=150, y=0)

    def retangulo(self):
        self.canvas_1 = Canvas(width=364, height=267, highlightthickness=0, bg=AZUL_CLARO)
        self.retangulo = self.canvas_1.create_image(182, 134, image=self.img_retangulo)
        self.canvas_1.place(x=0, y=100)

    def textos(self):
        self.saldo_atual = Label(text=f'Saldo Atual R$: {checagens.retornar_saldo(self.conta_logada)}',
                                 font=('arial', 18, 'bold'),
                                 bg=COR_RETANGULO)
        self.saldo_atual.place(x=80, y=100)

        self.agencia = Label(text='Agencia:',
                           font=('arial', 16, 'bold'),
                           bg=COR_RETANGULO)
        self.agencia.place(x=10, y=145)

        self.conta = Label(text='Conta:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO)
        self.conta.place(x=10, y=190)

        self.valor = Label(text='Valor:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO)
        self.valor.place(x=10, y=235)

        self.senha = Label(text='Senha:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO)

        self.senha.place(x=10, y=280)

        self.frase = Label(text='Cuide do seu patrimônio!',
                         wraplength=win_width,
                         bg=AZUL_CLARO,
                         font=('arial', 18, 'bold'),
                         fg='#050B45')
        self.frase.place(x=30, y=400)

    def inputs_(self):
        self.input_agencia = Entry(font=FONTE_COMUM,
                                 bg=COR_BUTTONS)
        self.input_agencia.place(x=120, y=140, height=40, width=200)

        self.input_conta = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS)
        self.input_conta.place(x=120, y=185, height=40, width=200)

        self.input_valor = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS)
        self.input_valor.place(x=120, y=230, height=40, width=200)

        self.input_senha = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS,
                               show='*')
        self.input_senha.place(x=120, y=275, height=40, width=200)

    def botoes(self):
        self.transfere = Button(text='Transferir',
                               font=FONTE_COMUM,
                               bg=COR_BUTTONS,
                               command= self.transferir)
        self.transfere.place(x=130, y=325, height=40, width=120)

    def transferir(self):
        campos = self.campos()
        if(checagens.verificar_campos(campos)):
            valor = int(self.input_valor.get())
            conta_transferencia = self.input_conta.get()

            if(checagens.transferir_sua_conta(self.input_conta.get(), self.conta_logada)):

                if(checagens.verificar_conta(conta_transferencia)):
                    saldo_atual = int(checagens.retornar_saldo(self.conta_logada))

                    if(checagens.verificar_agencia(conta_transferencia, self.input_agencia.get())):

                        if(valor <= saldo_atual):

                            if(checagens.conferir_senha(self.conta_logada, self.input_senha.get())):
                                with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json'
, 'r') as file:
                                    dados = dict(json.load(file))
                                #conta que sai o valor
                                conta_atual = {self.conta_logada:dados[self.conta_logada]}
                                conta_atual[self.conta_logada]['Saldo'] = saldo_atual - valor
                                checagens.atualizar(conta_atual)

                                #conta que recebe o valor
                                saldo_conta_trf = int(checagens.retornar_saldo(conta_transferencia))
                                conta_trf = {conta_transferencia: dados[conta_transferencia]}
                                conta_trf[conta_transferencia]['Saldo'] = saldo_conta_trf + valor
                                checagens.atualizar(conta_trf)
                                alertas.transferencia()
                                registrar('Transferencia',valor)
                                self.redirecionar_tela_principal()

    def redirecionar_tela_principal(self):
        self.janela.destroy()
        from projeto.telas.principal import Principal
        tela_principal = Principal()

    def campos(self):
        campos = [self.input_valor.get(),
                  self.input_senha.get(),
                  self.input_conta.get(),
                  self.input_agencia.get()]
        return campos
if __name__ == '__main__':
    trf = Transferir()


