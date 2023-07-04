import smtplib
from datetime import datetime
import email.message


data_hora = datetime.now()

def enviar_email(mail):  
    
    corpo_email = f"""
    <p>Olá</p>
    <h1>{data_hora}</h1>
    <p>Sua issue foi computada com sucesso</p>
    <p>as alteraçoes foram no campos:</p>
    
    """

    msg = email.message.Message()
    msg['Subject'] = "Jira - Bosch"
    msg['From'] = 'raphaelrrprates@gmail.com'
    msg['To'] = f'{mail}'
    password = 'xysmfstporodmgoc' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
   
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')



enviar_email('raphaelrrprates@gmail.com')