import smtplib
import email.message

def enviar_email(alteracao):  
    
    if alteracao == [0]:
    
        corpo_email = """
        <p>Olá</p>
        <p>Su issue foi computada com sucesso</p>
        """

    else:
        corpo_email = f"""
        <p>Olá</p>
        <p>Sua issue foi computada com sucesso, porém com alteraçoes</p>
        <p>as alteraçoes foram no campos:</p>
        {alteracao}
        """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'raphaelrrprates@gmail.com'
    msg['To'] = 'raphaelrrprates@gmail.com'
    password = 'jswwvisfusrgnwzl' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


alteracao = [0]
enviar_email(alteracao)