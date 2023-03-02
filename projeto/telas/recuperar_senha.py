from tkinter import *
import projeto.funcionalidades.checagens as checagens
import projeto.funcionalidades.alertas as alertas
import json
from random import randint
from projeto.funcionalidades.envia_email import enviar_email_codigo

AZUL_CLARO = '#A0E4FA'
FONTE_TITULOS = ('arial',20,'bold')
FONTE_COMUM = ('arial',15,'normal')

win_width, win_height = 364, 516
class RecuperarSenha:
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.logo()
        self.textos()
        self.inputs_()
        self.botoes()
        self.codigo_ = self.gerar_codigo()
        self.janela.mainloop()

    def retornar_email(self,conta):
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
            dados = dict(json.load(file))
        return dados[conta]['Email']

    def gerar_codigo(self):
        codigo_ = ''
        for i in range(0,6):
            codigo_ += str(randint(0,9))
        return codigo_

    def enviar_codigo(self):
        conta = self.input_conta.get()
        if(checagens.verificar_conta(conta)):
            to_email = self.retornar_email(conta)
            enviar_email_codigo(to_email,self.codigo_)
            alertas.codigo_enviado()

    def redirecionar_tela_login(self):
        self.janela.destroy()
        from projeto.telas.login import Login
        tela_login = Login()



    def verificar_senhas(self):
        if(self.input_senha.get() == self.input_confirmar_senha.get()):
            return True
        return False

    def cadastrar_senha(self):
        self.dados_conta = self.input_conta.get()
        campos = self.campos()
        if(checagens.verificar_campos(campos)):
            if(checagens.verificar_conta(self.dados_conta)):

                if(self.verificar_senhas()):

                   if(self.codigo_ == self.input_codigo.get()):
                       with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
                           contas = dict(json.load(file))
                       conta = {self.dados_conta: contas[self.dados_conta]}
                       conta[self.dados_conta]['Senha'] = self.input_senha.get()
                       checagens.atualizar(conta)
                       alertas.alterar_senha()
                       self.redirecionar_tela_login()
                   else:
                       alertas.codigo_invalido()
                else:
                    return alertas.conferir_senhas()

    def tela(self):
        self.janela.title('Recuperar Senha')
        self.janela.minsize(width=win_width, height=win_height)
        self.janela.config(background=AZUL_CLARO)
        self.janela.resizable(False, False)

    def logo(self):
        self.imagem = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\logo.png')
        self.canvas = Canvas(width= 93, height= 85,highlightthickness = 0,bg=AZUL_CLARO)
        self.canvas.create_image(47,43,image = self.imagem)
        self.canvas.place(x = 270,y=0)

    def textos(self):
        self.titulo = Label(text='Recuperar Senha',
                          font=FONTE_TITULOS,
                          bg=AZUL_CLARO,
                          pady=20)
        self.titulo.place(x = 50,y = 0)

        self.conta = Label(text='Conta',
                          font=FONTE_COMUM,
                          bg=AZUL_CLARO)
        self.conta.place(x = 80,y = 70)

        self.senha = Label(text='Senha',
                          font=FONTE_COMUM,
                          bg=AZUL_CLARO)
        self.senha.place(x = 80,y=150)

        self.confirmar_senha = Label(text='Confirmar senha',
                          font=FONTE_COMUM,
                          bg=AZUL_CLARO)
        self.confirmar_senha.place(x = 80,y=230)

        self.codigo = Label(text='Código',
                          font=FONTE_COMUM,
                          bg=AZUL_CLARO)
        self.codigo.place(x = 80,y=310)

        self.frase = Label(text='Pense com cuidado esses caracteres vão proteger a sua conta.',
                         wraplength=win_width,
                         bg=AZUL_CLARO,
                         font=('arial',16,'bold'),
                         fg='#050B45')
        self.frase.place(x = 10,y=440)

    def inputs_(self):
        self.input_conta = Entry(font=FONTE_COMUM)
        self.input_conta.place(x=80, y=100, height=40)


        self.input_senha = Entry(font = FONTE_COMUM)
        self.input_senha.place(x=80, y=180, height=40)

        self.input_confirmar_senha = Entry(font=FONTE_COMUM)
        self.input_confirmar_senha.place(x=80, y=260, height=40)

        self.input_codigo = Entry(font=FONTE_COMUM)
        self.input_codigo.place(x=80, y=340, height=40)

    def botoes(self):
        self.cadastrar = Button(text='Cadastrar',
                              bg='white',
                              highlightthickness=0,
                              font=FONTE_COMUM,
                              command=self.cadastrar_senha)

        self.cadastrar.place(x = 80,y = 400,height=40)

        self.envia_codigo = Button(text='Enviar código',
                                bg='white',
                                highlightthickness=0,
                                font=FONTE_COMUM,
                                command=self.enviar_codigo)

        self.envia_codigo.place(x=190, y=400, height=40)

    def campos(self):
        campos = [self.input_senha.get(),
                  self.input_conta.get(),
                  self.input_confirmar_senha.get(),
                  self.input_codigo.get()]
        return campos

if __name__ == '__main__':
    recuperar = RecuperarSenha()