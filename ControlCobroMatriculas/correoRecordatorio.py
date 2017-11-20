import json
import smtplib
import time

jsonData = '{"name": "Luis", "correo": "proyectoisagii@gmail.com", "carrera": "GII", "curso": "2017/2018"}' #ejemplo
jsonToPython = json.loads(jsonData)

def RecordatorioImpago15(json):
    username = 'proyectoisagii@gmail.com'
    password = 'ISA1997GII'

    fromaddr = 'proyectoisagii@gmail.com'
    toaddrs  = json['correo']
    msg = 'Debe realizar el pago de su matricula. \nRetraso de 15 dias.' 
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    
def RecordatorioImpago30(json):
    username = 'proyectoisagii@gmail.com'
    password = 'ISA1997GII'

    fromaddr = 'proyectoisagii@gmail.com'
    toaddrs  = json['correo']
    msg = 'Debe realizar el pago de su matricula. \nRetraso de 30 dias. \nEn caso contrario, procederemos a anular su matricula' 
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

RecordatorioImpago15(jsonToPython)
RecordatorioImpago30(jsonToPython)
