import smtplib
from email.mime.text import MIMEText

def send_email():
    """
    Função para enviar um e-mail simples utilizando o servidor SMTP do Gmail.

    Configurações:
        - smtp_server: Endereço do servidor SMTP (neste caso, do Gmail).
        - smtp_port: Porta do servidor SMTP (porta 587 para STARTTLS).
        - smtp_username: Endereço de e-mail usado para autenticação.
        - smtp_password: Senha ou token de autenticação do endereço de e-mail.
        - sender_email: Endereço de e-mail do remetente.
        - receiver_email: Endereço de e-mail do destinatário.

    Processo:
        1. Criação da mensagem de e-mail com `MIMEText`.
        2. Conexão ao servidor SMTP usando `smtplib.SMTP`.
        3. Configuração de criptografia TLS.
        4. Autenticação com as credenciais fornecidas.
        5. Envio do e-mail.

    Observações:
        - Certifique-se de substituir `smtp_username` e `smtp_password` com suas credenciais.
        - O Gmail pode exigir configurações adicionais para permitir o envio de e-mails via SMTP, como ativar o acesso a aplicativos menos seguros ou configurar tokens específicos.

    Raises:
        smtplib.SMTPException: Caso ocorra algum erro durante o envio do e-mail.
    """
    smtp_server = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    smtp_port = 587  # Porta para conexão STARTTLS
    smtp_username = 'jffilho500@gmail.com'  # Endereço de e-mail usado para autenticação
    smtp_password = ''  # Senha ou token do e-mail (substituir)

    sender_email = 'jffilho500@gmail.com'  # Endereço do remetente
    receiver_email = 'jffilho618@gmail.com'  # Endereço do destinatário

    # Criação da mensagem de e-mail
    msg = MIMEText('Este é um e-mail de teste.')  # Corpo do e-mail
    msg['Subject'] = 'Teste de E-mail'  # Assunto do e-mail
    msg['From'] = sender_email  # Remetente
    msg['To'] = receiver_email  # Destinatário

    # Envio do e-mail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Inicia a criptografia TLS
            server.login(smtp_username, smtp_password)  # Autentica o usuário
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Envia o e-mail
            print("E-mail enviado com sucesso!")
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar o e-mail: {e}")

if __name__ == "__main__":
    send_email()

