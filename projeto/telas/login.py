from tkinter import *
from time import sleep
import projeto.funcionalidades.checagens as checagens
import projeto.funcionalidades.alertas as alertas
from projeto.telas.principal import Principal

AZUL_CLARO = '#DBF1F8'
FONTE_TITULOS = ('arial',30,'bold')
FONTE_COMUM = ('arial',15,'bold')
win_width, win_height = 364, 516

class Login:
    def __init__(self):
        self.janela = Tk()
        self.tela()
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
        self.titulo = Label(text='Login', bg=AZUL_CLARO, font=FONTE_TITULOS)
        self.titulo.place(x=140, y=0)

        self.conta = Label(text='Conta', bg=AZUL_CLARO, font=FONTE_COMUM)
        self.conta.place(x=145, y=100)

        self.senha = Label(text='Senha', bg=AZUL_CLARO, font=FONTE_COMUM, pady=15)
        self.senha.place(x=145, y=180)

        self.cadastrar = Label(text='Cadastrar', font=FONTE_COMUM, bg=AZUL_CLARO, cursor='hand2')
        self.cadastrar.place(x=50, y=370)
        self.cadastrar.bind("<Button-1>", lambda e: self.cadastro())

        self.recuperar_senha = Label(text='Recuperar senha', font=FONTE_COMUM, bg=AZUL_CLARO, cursor='hand2')
        self.recuperar_senha.place(x=160, y=370)
        self.recuperar_senha.bind("<Button-1>", lambda e: self.recupera_senha())

        self.frase = Label(text='Como a fenix das cinzas, as suas finanças  vão renascer',
                         bg=AZUL_CLARO, font=FONTE_COMUM,
                         wraplength=364,
                         fg='#050B45')
        self.frase.place(x=10, y=440)

    def inputs_(self):
        self.input_conta = Entry(width=22, font=FONTE_COMUM)
        self.input_conta.place(x=60, y=130, height=40)

        self.input_senha = Entry(width=22, font=FONTE_COMUM)
        self.input_senha.place(x=60, y=220, height=40)

    def botoes(self):
        self.entrar = Button(text='Entrar',
                           font=FONTE_COMUM,
                           bg='white',
                           command=self.checar_login)
        self.entrar.place(x=150, y=300)

    def checar_login(self):
        conta_ = self.input_conta.get()
        senha_ = self.input_senha.get()
        campos = self.campos()

        if(checagens.verificar_campos(campos)):
            if (checagens.verificar_conta(conta_)):
                if (checagens.conferir_senha(conta_, senha_)):
                    alertas.logar()
                    self.registrar_conta_logada(conta_)
                    sleep(3)
                    self.redirecionar_principal()

    def registrar_conta_logada(self,conta):
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\conta_logada.txt', 'w') as file:
            file.write(conta)


    def redirecionar_principal(self):
        self.janela.destroy()
        tela_principal = Principal()

    def recupera_senha(self):
        self.janela.destroy()
        from projeto.telas.recuperar_senha import RecuperarSenha
        tela_recupera_senha = RecuperarSenha()

    def cadastro(self):
        self.janela.destroy()
        from projeto.telas.cadastrar import Cadastrar
        tela_cadastro = Cadastrar()


    def campos(self):
        campos = [self.input_conta.get(),self.input_senha.get()]
        return campos


if __name__ == '__main__':
    L1 = Login()

