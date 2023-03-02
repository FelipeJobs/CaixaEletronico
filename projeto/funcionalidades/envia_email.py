import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_msg = MIMEMultipart()
email_msg['Subject'] = 'Seu Extratato Bancário'

caminho_do_arquivo = 'C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\extrato.txt'
anexo = open(caminho_do_arquivo,'rb')
att = MIMEBase('application','octet-stream')
att.set_payload(anexo.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition',f'anexo;filename = extrato.txt')
anexo.close()
email_msg.attach(att)

def enviar_email_codigo(email_,codigo):
    email = 'felipecaluxx@gmail.com'
    senha = 'nerfsjnqljeropvk'
    with smtplib.SMTP('smtp.gmail.com') as conexao:
        conexao.starttls()
        conexao.login(user=email, password=senha)
        conexao.sendmail(
                from_addr=email,
                to_addrs=email_,
                msg = f'Subject: Código banco \n\n{codigo}'.encode())

def enviar_email_extrato(email_):
    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'Seu Extratato Bancário'

    caminho_do_arquivo = 'C:\\Users\\Lipe\\Documents\\caixaEletronico\\projeto\\dados\\extrato.txt'
    anexo = open(caminho_do_arquivo, 'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(anexo.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'anexo;filename = extrato.txt')
    anexo.close()
    email_msg.attach(att)
    email = 'felipecaluxx@gmail.com'
    senha = 'nerfsjnqljeropvk'
    with smtplib.SMTP('smtp.gmail.com') as conexao:
        conexao.starttls()
        conexao.login(user=email, password=senha)
        conexao.sendmail(
        from_addr=email,
        to_addrs=email_,
        msg= email_msg.as_string())



