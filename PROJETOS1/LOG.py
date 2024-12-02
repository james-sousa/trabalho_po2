import subprocess
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def send_email(image_path):
    """
    Função para enviar um e-mail com uma imagem anexada.

    Parâmetros:
        image_path (str): Caminho para a imagem que será anexada ao e-mail.

    Configurações:
        - smtp_server: Servidor SMTP utilizado (neste caso, o Gmail).
        - smtp_port: Porta utilizada pelo servidor (587 para STARTTLS).
        - smtp_username: Endereço de e-mail para autenticação.
        - smtp_password: Senha ou token de autenticação do Gmail.
        - sender_email: Endereço de e-mail do remetente.
        - receiver_email: Endereço de e-mail do destinatário.

    Processo:
        1. Cria um e-mail com um corpo de texto e uma imagem anexada.
        2. Conecta-se ao servidor SMTP utilizando `smtplib`.
        3. Envia o e-mail.

    Observações:
        - Certifique-se de que o Gmail está configurado para permitir acesso via SMTP.
        - Substitua `smtp_username` e `smtp_password` com as credenciais corretas.
    """
    smtp_server = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    smtp_port = 587  # Porta para STARTTLS
    smtp_username = 'jffilho500@gmail.com'  # Seu endereço de e-mail
    smtp_password = 'xsujddrvujadbsti'  # Senha ou token de autenticação
    sender_email = 'jffilho500@gmail.com'  # Endereço do remetente
    receiver_email = 'jffilho618@gmail.com'  # Endereço do destinatário

    # Criação da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Intruso detectado'

    # Adiciona o corpo do e-mail
    body = MIMEText('Uma tentativa de login incorreta foi detectada.')
    msg.attach(body)

    # Adiciona a imagem ao e-mail
    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)

    # Envia o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Inicia a criptografia TLS
        server.login(smtp_username, smtp_password)  # Autentica o usuário
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Envia o e-mail

def capture_photo(photo_path):
    """
    Função para capturar uma foto usando o comando `fswebcam`.

    Parâmetros:
        photo_path (str): Caminho onde a foto será salva.

    Observação:
        - Certifique-se de que o comando `fswebcam` está instalado no sistema.
    """
    command = f'fswebcam -r 1280x720 {photo_path}'  # Comando para capturar a foto
    subprocess.run(command, shell=True)  # Executa o comando no shell

def monitor_auth_log():
    """
    Função para monitorar o arquivo de log de autenticação (`/var/log/auth.log`)
    em busca de tentativas de falha de autenticação e reagir a elas.

    Processo:
        1. Monitora continuamente o arquivo de log usando o comando `tail -F`.
        2. Procura por linhas que contenham o termo `authentication failure`.
        3. Extrai o nome do usuário associado à tentativa de falha de autenticação.
        4. Captura uma foto e envia por e-mail ao detectar uma tentativa de falha.

    Observações:
        - O script requer privilégios para acessar o arquivo `/var/log/auth.log`.
        - A variável `email_sent` impede múltiplos envios de e-mails para a mesma tentativa.

    Exceções:
        - Captura interrupções de teclado (Ctrl+C) para parar o monitoramento.
    """
    email_sent = False  # Variável para rastrear se o e-mail já foi enviado

    # Comando para monitorar continuamente o arquivo de log
    tail_process = subprocess.Popen(['tail', '-F', '/var/log/auth.log'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Started monitoring...")

    try:
        while True:
            line = tail_process.stdout.readline().decode().strip()  # Lê cada linha do log
            if 'authentication failure' in line and not email_sent:
                # Procura pelo nome de usuário associado à falha
                match = re.search(r'authentication failure.*user=([\w-]+)', line)
                print("Line:", line)
                print("Match object:", match)

                if match:
                    username = match.group(1)  # Extrai o nome do usuário
                    print(f"Falha detectada para o usuário: {username}")
                    photo_path = '/home/bomb4/Documentos/PROJETOS/fotos/photo.jpg'  # Caminho da foto

                    # Captura uma foto e envia o e-mail
                    capture_photo(photo_path)
                    send_email(photo_path)

                    email_sent = True  # Evita múltiplos envios
    except KeyboardInterrupt:
        print("Stopping monitoring...")  # Mensagem ao interromper o programa

if __name__ == "__main__":
    monitor_auth_log()

