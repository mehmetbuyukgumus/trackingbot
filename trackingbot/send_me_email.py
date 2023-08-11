import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendMeEmail(toSend, subject, content):
    fromMailAdress = "youradress@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.starttls()
    server.login("youradress@gmail.com", "YOURPASSWORD")
    message = MIMEMultipart("alternateve")
    message["subject"] = subject
    htmlContent = MIMEText(content, "html") 
    message.attach(htmlContent)
    server.sendmail(
        fromMailAdress,
        toSend,
        message.as_string()
    )
    server.quit()
    
    
    
    
     
    