from tkinter import *
import projeto.funcionalidades.checagens as checagens
import projeto.funcionalidades.alertas as alertas
from random import randint
from projeto.telas.login import Login

AZUL_CLARO = '#BAEBFB'
FONTE_TITULOS = ('arial',30,'bold')
FONTE_COMUM = ('arial',15,'normal')

win_width, win_height = 550, 450

class Cadastrar:
    def __init__(self):
        self.conta_gerada = self.gerar_conta()
        self.janela = Tk()
        self.tela()
        self.logo()
        self.textos()
        self.inputs_()
        self.botoes()

        self.janela.mainloop()

    def tela(self):
        self.janela.title('Cadastro')
        self.janela.minsize(width=win_width, height=win_height)
        self.janela.config(background=AZUL_CLARO)
        self.janela.resizable(False, False)

    def logo(self):
        self.imagem = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\logo.png')
        self.canvas = Canvas(width=93, height=85, highlightthickness=0, bg=AZUL_CLARO)
        self.canvas.create_image(47, 43, image=self.imagem)
        self.canvas.place(x=470, y=0)

    def textos(self):
        self.titulo = Label(text='Cadastrar',
                          font=FONTE_TITULOS,
                          bg=AZUL_CLARO)
        self.titulo.place(x=180, y=0)

        self.nome = Label(text='Nome Completo',
                        font=FONTE_COMUM,
                        bg=AZUL_CLARO)
        self.nome.place(x=30, y=60)

        self.cpf = Label(text='CPF',
                       font=FONTE_COMUM,
                       bg=AZUL_CLARO)
        self.cpf.place(x=30, y=140)

        self.senha = Label(text='Senha',
                         font=FONTE_COMUM,
                         bg=AZUL_CLARO)
        self.senha.place(x=30, y=220)

        self.agencia = Label(text='Agência',
                           font=FONTE_COMUM,
                           bg=AZUL_CLARO)
        self.agencia.place(x=30, y=300)

        self.email = Label(text='E-mail',
                         font=FONTE_COMUM,
                         bg=AZUL_CLARO)
        self.email.place(x=380, y=60)

        self.telefone = Label(text='Telefone',
                            font=FONTE_COMUM,
                            bg=AZUL_CLARO)
        self.telefone.place(x=380, y=140)

        self.conta = Label(text='Conta',
                         font=FONTE_COMUM,
                         bg=AZUL_CLARO)
        self.conta.place(x=380, y=220)

        self.new_conta = Label(font=FONTE_COMUM,
                             bg='white',
                             text= self.conta_gerada
                             )
        self.new_conta.place(x=300, y=250, height=40, width=222)

    def inputs_(self):
        self.input_nome = Entry(font=FONTE_COMUM)
        self.input_nome.place(x=30, y=90, height=40)

        self.input_cpf = Entry(font=FONTE_COMUM)
        self.input_cpf.place(x=30, y=170, height=40)

        self.input_senha = Entry(font=FONTE_COMUM)
        self.input_senha.place(x=30, y=250, height=40)

        self.input_agencia = Entry(font=FONTE_COMUM)
        self.input_agencia.place(x=30, y=330, height=40)

        self.input_email = Entry(font=FONTE_COMUM)
        self.input_email.place(x=300, y=90, height=40)

        self.input_telefone = Entry(font=FONTE_COMUM)
        self.input_telefone.place(x=300, y=170, height=40)

    def botoes(self):
        self.cadastro = Button(text='Cadastrar',
                             bg='white',
                             font=FONTE_COMUM,
                             highlightthickness=0,
                             command=self.cadastrar
                             )
        self.cadastro.place(x=220, y=400, height=40)

    def cadastrar(self):
        campos = self.campos()
        if(checagens.verificar_campos(campos)):
            if(checagens.verificar_email(self.input_email.get())):
                if(checagens.verificar_cpf(self.input_cpf.get())):
                    if(checagens.tamanho_senha(self.input_senha.get())):
                        self.salvar_dados()
                        alertas.cadastro()
                        self.redirecionar_login()

    def salvar_dados(self):
        conta = {self.conta_gerada: {
            'Nome': self.input_nome.get(),
            'Agencia': self.input_agencia.get(),
            'Senha': self.input_senha.get(),
            'Cpf': self.input_cpf.get(),
            'Email': self.input_email.get(),
            'Telefone': self.input_telefone.get(),
            'Saldo': 0,
            'Operacoes': []}}
        checagens.atualizar(conta)

    def gerar_conta(self):
        self.numeros_conta = ''
        for digito in range(0, 6):
            numero = randint(0, 9)
            self.numeros_conta += str(numero)
        return self.numeros_conta

    def campos(self):
        campos = [self.input_senha.get(),
                  self.input_agencia.get(),
                  self.input_telefone.get(),
                  self.input_email.get(),
                  self.input_nome.get(),
                  self.input_cpf.get()]
        return campos

    def redirecionar_login(self):
        self.janela.destroy()
        tela_login = Login()


if __name__ == '__main__':
    cadastro = Cadastrar()




