import emails
message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                       subject="Your receipt No. 567098123",
                       mail_from=('Some Store', 'raphaelrrprates@gmail.com'))
message.attach(data=open('bill.pdf', 'rb'), filename='bill.pdf')

r = message.send(to='raphaelrrprates@gmail.com', smtp={'host': 'aspmx.l.google.com', 'timeout': 5})
