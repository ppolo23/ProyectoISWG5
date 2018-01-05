import psycopg2
import smtplib
from time import sleep, strftime
from datetime import datetime
import datetime


def conectar():

	conexion = psycopg2.connect(
		database = "Pagos",
		user = "postgres",
		password = "postgres",
		host = "127.0.0.1",
		port = "5432"
	)

	return conexion

def recordatorioImpago(correo, msg):
	print("disjdis")
	username = 'proyectoisagii@gmail.com'
	password = 'ISA1997GII'
	fromaddr = 'proyectoisagii@gmail.com'
	toaddrs  = correo
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

def envios():

	while True:

		conex = conectar()
		cursor = conex.cursor()

		cursor.execute(
			"SELECT * FROM \"CobrosMatriculas\""
		)

		filas = cursor.fetchall()
		conex.close()

		for tupla in filas:
			print(tupla)

			if not tupla[3]:

				delta = datetime.date.today() - tupla[1]

				if delta.days == 15:
					recordatorioImpago(tupla[4], 'Debe realizar el pago de su matricula. \nRetraso de 15 dias.')

				elif delta.days == 30:
					recordatorioImpago(tupla[4], 'Debe realizar el pago de su matricula. \
					\nRetraso de 30 dias. \nEn caso contrario, procederemos a anular su matricula')

			else:
				recordatorioImpago(tupla[4], '     UNIVERSIDAD DE VILLAMAYOR     \n' + '\n' + tupla[0] + ' ha realizado el pago de su matricula con exito\n' + 'A fecha de ' + strftime("%d/%m/%y") + '\n')
				conex = conectar()
				cursor = conex.cursor()

				cursor.execute("DELETE FROM \"CobrosMatriculas\" WHERE \"DNI\" = '" +  tupla[0] + "';")

				conex.commit()
				conex.close()

		sleep(86400)
			


envios()
