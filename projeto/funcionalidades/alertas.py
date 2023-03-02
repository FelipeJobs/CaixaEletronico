from tkinter import messagebox

def preencher_campos():
    messagebox.showerror(title='Erro',message='Preencha todos os campos')

def senha_invalida():
    messagebox.showerror(title='Erro',message='Senha incorreta')

def conta_invalida():
    messagebox.showerror(title='Erro',message='Essa conta não está registrada em nosso banco de dados')

def saldo_insuficiente():
    messagebox.showinfo(title='Informativo',message='Você não tem saldo suficiente')

def logar():
    messagebox.showinfo(title='Informativo',message='Login realizado com sucesso')

def deposito():
    messagebox.showinfo(title='Informativo', message='Depósito realizado com sucesso')

def saque():
    messagebox.showinfo(title='Informativo', message='Saque realizado com sucesso')

def transferencia():
    messagebox.showinfo(title='Informativo', message='Transferência realizada com sucesso')

def cadastro():
    messagebox.showinfo(title='Informativo', message='Cadastro realizado com sucesso')

def tamanho_senha():
    messagebox.showinfo(title='Informativo',message='A senha deve ter exatamente 6 digitos')

def conferir_senhas():
    messagebox.showinfo(title='Informativo',message='As senhas digitadas não batem')

def alterar_senha():
    messagebox.showinfo(title='Informativo',message='Senha alterada com Sucesso')

def analisar_cpf():
    messagebox.showerror(title='Error',message='CPF inválido')

def deposito():
    messagebox.showinfo('Informativo',message='Deposito realizado com sucesso!!')

def saque_sucesso():
    messagebox.showinfo('Informativo',message='Saque realizado com sucesso!!')

def saldo_insuficiente():
    messagebox.showinfo('Informativo',message='Saldo insuficiente')

def nao_transfere():
    messagebox.showinfo('Informativo',message='Não pode transferir para sua própria conta.')

def codigo_enviado():
    messagebox.showinfo(title='Informativo', message='Código enviado para o seu email')

def codigo_invalido():
    messagebox.showerror(title='Error', message='Código inválido')

def agencia_invalida():
    messagebox.showerror(title='Error',message='Agencia inválida')

def extrato_enviado():
    messagebox.showinfo('Informativo','O seu extrato foi encaminhado para o seu E-mail cadastrado')

def email_invalido():
    messagebox.showinfo('Informativo','E-mail Inválido')