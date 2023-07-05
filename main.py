import smtplib, email.message, os
from datetime import datetime

kaka = datetime.now()

def enviar_email(mail):

    body = f"""
    <body style = "background-color: rgb(245, 245, 245); font-size: 30px">
    <div><img src="imagens/panda.png" alt="" style="width: 150px;"></div>
    <h3 style = "color: rgb(33, 32, 33); text-align: center;">Hello!</h3>
    <br>
    <div style = "color: rgb(33, 32, 33)">°Your Improvement has been successfully added at {kaka}</div>
    <br>
    <div style = "color: rgb(33, 32, 33)">°thank you very much for using our platform</div>
    <br>
    <div style = "color: rgb(33, 32, 33)">°Questions can be answered at: verwaljira@gmail.com</div>
    <br>
    </body>
    """

    msg = email.message.Message()

    msg['Subject'] = "Jira - Bosch"
    msg['From'] = 'verwaljira@gmail.com'
    msg['To'] = f'{mail}'
    password = 'itnahpjuxkdisfat'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')



enviar_email('raphaelrrprates2@gmail.com')
