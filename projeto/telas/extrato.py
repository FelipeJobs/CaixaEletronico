from tabulate import tabulate
import json
import projeto.funcionalidades.checagens as checagens
import projeto.funcionalidades.alertas as alertas
from projeto.funcionalidades.envia_email import enviar_email_extrato



class Extrato:

    def __init__(self):
        self.conta_logada = checagens.conta_logada()
        self.email = self.retornar_email()
        self.operacoes = self.retornar_operacoes()
        self.extrato = self.criar_extrato()
        self.salvar_extrato()
        self.enviar_extrato()

    def retornar_email(self):
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
            dados = json.load(file)
        email = dados[self.conta_logada]['Email']
        return email

    def retornar_operacoes(self):
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
            dados = dict(json.load(file))
        operacoes = dados[self.conta_logada]['Operacoes']
        return operacoes

    def criar_extrato(self):
        dados_extrato = [['Operação', 'Data', 'Valor']]
        for operacao in self.operacoes:
            dados_extrato.append(operacao)
        dados_extrato.append(['', 'Saldo', checagens.retornar_saldo(self.conta_logada)])
        return tabulate(dados_extrato, headers='firstrow')

    def salvar_extrato(self):
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\extrato.txt', 'w') as file:
            self.extrato.encode()
            file.write(self.extrato)

    def enviar_extrato(self):
        enviar_email_extrato(self.email)
        alertas.extrato_enviado()

if __name__ == '__main__':
    e1 = Extrato()