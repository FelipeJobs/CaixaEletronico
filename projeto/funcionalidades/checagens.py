import projeto.funcionalidades.alertas as alertas
import re
import json

def verificar_cpf(cpf:str):
    primeiro_digito_cpf_fornecido = cpf[0]
    contador = 0
    for digito in cpf:
        if(digito == primeiro_digito_cpf_fornecido):
            contador+=1
    if(contador != 11):
        posicao_digito = 1
        soma_digito_1 = 0
        soma_digito_2 = 0
        primeiro_digito = ''
        segundo_digito = ''
        for digito in cpf[0:9]:
            digito = int(digito)
            soma_digito_1+=(digito*posicao_digito)
            posicao_digito +=1

        resultado = soma_digito_1 %11

        if(resultado > 9):
            primeiro_digito = 0
        else:
            primeiro_digito = resultado

        posicao_digito = 0
        for digito in cpf[0:9]:
            digito = int(digito)
            soma_digito_2 += (digito * posicao_digito)
            posicao_digito += 1

        resultado_2 = (soma_digito_2 + (primeiro_digito*posicao_digito))%11
        if (resultado_2 > 9):
            segundo_digito = 0
        else:
            segundo_digito = resultado_2
        cpf_gerado = f'{cpf[0:9]}{primeiro_digito}{segundo_digito}'

        if(cpf_gerado == cpf):
            return True
    alertas.analisar_cpf()
    return False


def verificar_campos(lista):
    for i in lista:
        if(i == ''):
            alertas.preencher_campos()
            return False
            break
    return True

def conferir_senha(conta,senha):
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as contas:
        dados = dict(json.load(contas))
    senha_correta = dados[conta]['Senha']
    if(senha_correta == senha):
        return True
    alertas.senha_invalida()
    return False

def verificar_conta(conta):
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
        contas = dict(json.load(file))

    if(conta in contas.keys()):
        return True
    alertas.conta_invalida()
    return False

def atualizar(dict):
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as files:
        dados = json.load(files)
        dados.update(dict)
        with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'w') as files:
            json.dump(dados, files, indent=2)

def conta_logada():
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\conta_logada.txt'
, 'r') as file:
        return file.read()

def retornar_saldo(conta):
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
        dados = dict(json.load(file))
    return dados[conta]['Saldo']

def verificar_saldo(valor,conta):
    saldo_atual = retornar_saldo(conta)
    if(saldo_atual > valor):
        return True
    return False

def tamanho_senha(senha):
    tamanho = len(senha)
    if(tamanho == 6):
        return  True
    alertas.tamanho_senha()
    return False

# verifica se estou tentando transferir para a minha própria conta
def transferir_sua_conta(conta_trf, conta_logada):
    if(conta_trf != conta_logada):
        return True
    return alertas.nao_transfere()

def verificar_agencia(conta,agencia):
    with open('C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\clientes.json', 'r') as file:
        dados = dict(json.load(file))
    if(dados[conta]['Agencia'] == agencia):
        return True
    alertas.agencia_invalida()
    return False

def verificar_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        return True
    alertas.email_invalido()
    return False















verificar_cpf('45609928869')



