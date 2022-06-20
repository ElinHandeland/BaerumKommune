import requests
from requests.structures import CaseInsensitiveDict

hent_passord_URL = "http://bk-intervju-oppgave-app.azurewebsites.net/api/HentPassord"

respons = requests.get(url=hent_passord_URL)
if respons.status_code == 200:
    try:
        #json_respons = respons.json()
        print()
        print("Passordet er:", respons.json()['passord'])
        print()

    except:
        print("Error")


#Henter data
hent_data_URL = "http://bk-intervju-oppgave-app.azurewebsites.net/api/HentData"

headers = CaseInsensitiveDict()
headers["apikey"] = respons.json()['passord']
respons2 = requests.get(url=hent_data_URL, headers=headers)

print("Data som hentes ut er: ", respons2.json()['data'])


