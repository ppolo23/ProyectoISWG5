import requests
import json

apiBase = "http://localhost:8080/apiPagos/"

# post de cancion
# http://localhost:8080/miAplicacion/cancion
# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests


token = "my token"

data = {
  "cod_id": 1,
  "fecha": "1-1-2017",
  "hora": "10:00",
  "id_prof": 2,
  "cantidad": 13
}

headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", "data":"data"}


r3 = requests.put(apiBase + "insertarCobroEspacio", data = json.dumps(data),  headers=headers)

#r3 = requests.put("http://localhost:8080/apiPagos/insertarCobroEspacio",  data = json.dumps(data),  headers=headers)

print(r3.text)