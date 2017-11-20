import json
import smtplib
import time

jsonData = '{"name": "Luis", "correo": "proyectoisagii@gmail.com", "carrera": "GII", "curso": "2017/2018"}' #ejemplo
jsonPython = json.loads(jsonData)
 
def enviarRecibo(json):
    username = 'proyectoisagii@gmail.com'
    password = 'ISA1997GII'

    fromaddr = 'proyectoisagii@gmail.com'
    toaddrs  = json['correo']
    msg = '     UNIVERSIDAD DE VILLAMAYOR     \n' + '\n' + json['name'] + ' ha realizado el pago de su matricula con exito\n' + 'Alumno de ' + json['carrera'] + ' el curso ' + json['curso'] + '\n' + 'A fecha de ' + time.strftime("%d/%m/%y") + '\n' 
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

enviarRecibo(jsonPython)


