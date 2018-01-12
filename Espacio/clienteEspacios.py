import requests
import json

apiBase = "http://localhost:8080/APIespacios/"

# post de cancion
# http://localhost:8080/miAplicacion/cancion
# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests


token = "my token"

data = {
  "codId": 2,
  "fecha": "1-1-2017",
  "horaFin": "19:00",
  "horaInicio": "10:00",
  "id_prof": 5
}

headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", "data":"data"}

r3 = requests.put(apiBase + "alquilarEspacio", data = json.dumps(data),  headers=headers)

#r3 = requests.put("http://localhost:8080/APIespacios/alquilarEspacio", data = json.dumps(data),  headers=headers)

print(r3.text)