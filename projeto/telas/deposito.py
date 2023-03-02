from tkinter import *
import json
import projeto.funcionalidades.checagens as checagens
import projeto.funcionalidades.alertas as alertas
from projeto.funcionalidades.registrar_operacoes import registrar

AZUL_CLARO = '#88D9F2'
COR_RETANGULO = '#D1F1FB'
FONTE_TITULOS = ('arial',30,'bold')
FONTE_COMUM = ('arial',15,'normal')
COR_BUTTONS = 'white'



win_width, win_height = 364, 516

class Deposito:
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
        self.janela.title('Login')
        self.janela.minsize(width=win_width, height=win_height)
        self.janela.config(background=AZUL_CLARO, pady=10)
        self.janela.resizable(False, False)

    def textos(self):
        self.valor = Label(text='Valor:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO)
        self.valor.place(x=10, y=120)

        self.senha = Label(text='Senha:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO
                         )
        self.senha.place(x=10, y=200)

        self.frase = Label(text='A gente gasta energia demais com coisas que importam de menos. '
                              'a chave para um vida saudável não é salada, é se poupar de todos '
                              'os excessos',
                         wraplength=win_width,
                         bg=AZUL_CLARO,
                         font=('arial', 17, 'bold'),
                         fg='#050B45'
                         )
        self.frase.place(x=10, y=370)

    def logo(self):
        self.img_logo = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\logo.png')
        self.img_retangulo = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\fundo_interno.png')

        self.canvas = Canvas(width=93, height=85, highlightthickness=0, bg=AZUL_CLARO)
        self.logo = self.canvas.create_image(47, 43, image=self.img_logo)
        self.canvas.place(x=150, y=0)

    def retangulo(self):
        self.canvas_1 = Canvas(width=364, height=267, highlightthickness=0, bg=AZUL_CLARO)
        retangulo = self.canvas_1.create_image(182, 134, image=self.img_retangulo)
        self.canvas_1.place(x=0, y=100)

    def inputs_(self):
        self.input_valor = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS)

        self.input_valor.place(x=100, y=115, height=40)

        self.input_senha = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS,
                               show='*')

        self.input_senha.place(x=100, y=195, height=40)

    def botoes(self):
        self.deposito = Button(text='Depositar',
                             font=FONTE_COMUM,
                             bg=COR_BUTTONS,
                             highlightthickness=0,
                             command=self.depositar)

        self.deposito.place(x=130, y=280, height=40, width=100)

    def depositar(self):
        campos = self.campos()
        if(checagens.verificar_campos(campos)):
            valor = int(self.input_valor.get())
            if (checagens.conferir_senha(self.conta_logada, self.input_senha.get())):
                with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
                    contas = dict(json.load(file))
                conta = {self.conta_logada: contas[self.conta_logada]}
                saldo = int(conta[self.conta_logada]['Saldo'])
                novo_saldo = saldo + valor
                conta[self.conta_logada]['Saldo'] = novo_saldo
                checagens.atualizar(conta)
                alertas.deposito()
                registrar('Deposito',valor)
                self.redirecionar_tela_principal()

    def redirecionar_tela_principal(self):
        self.janela.destroy()
        from projeto.telas.principal import Principal
        tela_principal = Principal()

    def campos(self):
        campos = [self.input_valor.get(), self.input_senha.get()]
        return campos


if __name__ == '__main__':
    deposito = Deposito()