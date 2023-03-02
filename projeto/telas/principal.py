from tkinter import *
import projeto.funcionalidades.checagens as checagens
from projeto.telas.saque import Saque
from projeto.telas.deposito import Deposito
from projeto.telas.transferir import Transferir
from projeto.telas.extrato import Extrato

AZUL_CLARO = '#88D9F2'
FONTE_TITULOS = ('arial',30,'bold')
FONTE_COMUM = ('arial',15,'normal')
COR_BUTTONS = 'white'

win_width, win_height = 364, 516


class Principal:
    def __init__(self):
        self.conta_logada = checagens.conta_logada()
        self.janela = Tk()
        self.tela()
        self.logo()
        self.textos()
        self.botoes()
        self.janela.mainloop()

    def tela(self):
        self.janela.title('Principal')
        self.janela.minsize(width=win_width, height=win_height)
        self.janela.config(background=AZUL_CLARO)
        self.janela.resizable(False, False)

    def textos(self):
        self.saldo = Label(text=f'Saldo R$: {checagens.retornar_saldo(self.conta_logada)}',
                           bg='#D1F1FB',
                           font=('arial', 18, 'bold'))
        self.saldo.place(x=80, y=120, width=200)

        self.frase = Label(text='Faça o dinheiro trabalhar por você, não o contrário!',
                         wraplength=win_width,
                         bg=AZUL_CLARO,
                         font=('arial', 18, 'bold'),
                         fg='#050B45')
        self.frase.place(x=10, y=440)

    def botoes(self):
        self.extrato = Button(text='Extrato',
                            font=FONTE_COMUM,
                            bg=COR_BUTTONS,
                            command= Extrato)
        self.extrato.place(x=130, y=190, height=40, width=140)

        self.saque = Button(text='Saque',
                          font=FONTE_COMUM,
                          bg=COR_BUTTONS,
                          command=self.redirecionar_saque)
        self.saque.place(x=30, y=250, height=40, width=140)

        self.deposito = Button(text='Depósito',
                             font=FONTE_COMUM,
                             bg=COR_BUTTONS,
                             command=self.redirecionar_deposito)
        self.deposito.place(x=200, y=250, height=40, width=140)

        self.trf = Button(text='Transferência',
                        font=FONTE_COMUM,
                        bg=COR_BUTTONS,
                        command= self.redirecionar_transferir)
        self.trf.place(x=30, y=350, height=40, width=140)

        self.desloga = Button(text='Deslogar',
                        font=FONTE_COMUM,
                        bg=COR_BUTTONS,
                        command= self.deslogar)
        self.desloga.place(x=200, y=350, height=40, width=140)

    def logo(self):
        self.imagem = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\logo.png')
        self.canvas = Canvas(width=93, height=85, highlightthickness=0, bg=AZUL_CLARO)
        self.canvas.create_image(47, 43, image=self.imagem)
        self.canvas.place(x=150, y=0)


    def redirecionar_deposito(self):
        self.janela.destroy()
        tela_deposito = Deposito()


    def redirecionar_saque(self):
        self.janela.destroy()
        tela_saque = Saque()

    def redirecionar_transferir(self):
        self.janela.destroy()
        tela_transferir = Transferir()


    def limpar_registro_logado(self):
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\conta_logada.txt', 'w') as file:
            file.write('')


    def deslogar(self):
        self.janela.destroy()
        from projeto.telas.login import Login
        self.limpar_registro_logado()
        tela_login = Login()

if __name__ == '__main__':
    p = Principal()



