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

class Saque:
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

    def textos(self):
        self.saldo_atual = Label(text=f'Saldo Atual R$: {checagens.retornar_saldo(self.conta_logada)}',
                                 font=('arial', 18, 'bold'),
                                 bg=COR_RETANGULO)
        self.saldo_atual.place(x=80, y=100)

        self.valor = Label(text='Valor:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO)
        self.valor.place(x=10, y=180)

        self.senha = Label(text='Senha:',
                         font=('arial', 16, 'bold'),
                         bg=COR_RETANGULO
                         )
        self.senha.place(x=10, y=250)

        self.frase = Label(text='Cuidado com as pequenas despesas, um pequeno vazamento afundará um grande navio',
                         wraplength=win_width,
                         bg=AZUL_CLARO,
                         font=('arial', 18, 'bold'),
                         fg='#050B45'
                         )
        self.frase.place(x=10, y=380)

    def logo(self):
        self.img_logo = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\logo.png')
        self.img_retangulo = PhotoImage(file='C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\imagens\\fundo_interno.png')

        self.canvas = Canvas(width=93, height=85, highlightthickness=0, bg=AZUL_CLARO)
        self.logo = self.canvas.create_image(47, 43, image=self.img_logo)
        self.canvas.place(x=150, y=0)

    def retangulo(self):
        self.canvas_1 = Canvas(width=364, height=267, highlightthickness=0, bg=AZUL_CLARO)
        self.retangulo = self.canvas_1.create_image(182, 134, image=self.img_retangulo)
        self.canvas_1.place(x=0, y=100)


    def inputs_(self):
        self.input_valor = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS)

        self.input_valor.place(x=100, y=175, height=40)

        self.input_senha = Entry(font=FONTE_COMUM,
                               bg=COR_BUTTONS,
                               show='*')

        self.input_senha.place(x=100, y=245, height=40)

    def botoes(self):
        self.sacar = Button(text='Sacar',
                          font=FONTE_COMUM,
                          bg=COR_BUTTONS,
                          highlightthickness=0,
                          command=self.sacar)

        self.sacar.place(x=130, y=320, height=40, width=100)

    def sacar(self):
        campos = self.campos()
        if (checagens.verificar_campos(campos)):
            valor = int(self.input_valor.get())
            if (checagens.verificar_saldo(valor, self.conta_logada)):
                if(checagens.conferir_senha(self.conta_logada, self.input_senha.get())):
                    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json'
, 'r') as file:
                        contas = dict(json.load(file))
                    conta = {self.conta_logada: contas[self.conta_logada]}
                    saldo = int(conta[self.conta_logada]['Saldo'])
                    novo_saldo = saldo - valor
                    conta[self.conta_logada]['Saldo'] = novo_saldo
                    checagens.atualizar(conta)
                    alertas.saque_sucesso()
                    registrar('Saque', valor)
                    self.redirecionar_tela_principal()
            else:
                alertas.saldo_insuficiente()

    def redirecionar_tela_principal(self):
        self.janela.destroy()
        from projeto.telas.principal import Principal
        tela_principal = Principal()

    def campos(self):
        campos = [self.input_valor.get(), self.input_senha.get()]
        return campos

if __name__ == '__main__':
    sacar = Saque()
