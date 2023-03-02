import json
import projeto.funcionalidades.checagens as checagens
import datetime

def registrar(operacao,valor):
    data_ = data()
    conta_atual = checagens.conta_logada()
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
        dados = dict(json.load(file))

    lista = list(dados[conta_atual]['Operacoes'])
    operacoes = (operacao,data_,valor)
    lista.append(operacoes)

    conta = {conta_atual: dados[conta_atual]}
    conta[conta_atual]['Operacoes'] = lista
    checagens.atualizar(conta)

def data():
    data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    return data

if __name__ == '__main__':
    registrar('Transferencia',200)


