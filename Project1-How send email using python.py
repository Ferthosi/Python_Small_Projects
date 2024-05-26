'''from email.message import EmailMessage
import ssl
import smtplib

email_sender ="ferthosiakh99@gmail.com"
email_password ="cwoo dcai bucq sepk"

email_receiver="tiboj29322@godsigma.com"

subject = "Dont Forget to subscribe"
body ="hey help me gain followers"


em =EmailMessage()
em['From']= email_sender
em['TO']=email_receiver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver,em.as_string())'''

'''from email.message import EmailMessage
import ssl
import smtplib

email_sender="ferthosiakh99@gmail.com"
email_password ="cwoo dcai bucq sepk"
email_receiver="tiboj29322@godsigma.com"
subject ="Trying to send a email"
body ="Successfully sent a mail by self"

em =EmailMessage()

em["From"]= email_sender
em["To"]= email_receiver
em["subject"]= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context)as  smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())'''

'''from email.message import EmailMessage
import ssl
import smtplib

email_sender="ferthosiakh99@gmail.com"
email_password ="cwoo dcai bucq sepk"

email_receiver="tiboj29322@godsigma.com"
subject="Trying with out help"
body= "perechiiiiii, perechiiiii"

em = EmailMessage()
em["From"]= email_sender
em["To"]=email_receiver
em["subject"]=subject
em.set_content(body)

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())'''

from email.message import EmailMessage
import ssl
import smtplib

email_sender="ferthosiakh99@gmail.com"
email_password="cwoo dcai bucq sepk"

email_receiver="tiboj29322@godsigma.com"
subject="Again trying"
body="Successfull with out any error"


em=EmailMessage()
em["From"]=email_sender
em["To"]=email_receiver
em["subject"]=subject
em.set_content(body)

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())