"""Crear impreso de cobro de matricula en un archivo de texto (.txt)"""
import time
import json
jsonData = '{"name": "Luis", "carrera": "GII", "curso": "2017/2018"}' #ejemplo
jsonPython = json.loads(jsonData)


def crearImpresoCobro(json):
    impreso = open(json['name'] + ' Pago de matricula.txt','a')
    impreso.write('     UNIVERSIDAD DE VILLAMAYOR     \n')
    impreso.write('\n')
    impreso.write(json['name'] + ' ha realizado el pago de su matricula con éxito\n')
    impreso.write('Alumno de ' + json['carrera'] + ' el curso ' + json['curso'] + '\n')
    impreso.write('A fecha de ' + time.strftime("%d/%m/%y") + '\n')
    impreso.write('\n')
    impreso.close() 



crearImpresoCobro(jsonPython)

