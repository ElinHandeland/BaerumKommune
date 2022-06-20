import requests
from requests.structures import CaseInsensitiveDict
#URL for å hente ut passord
hent_passord_URL = "http://bk-intervju-oppgave-app.azurewebsites.net/api/HentPassord"

respons = requests.get(url=hent_passord_URL)

# sjekker respont. respons 200 = OK
print(respons.status_code)

#json_respons = respons.json()

#henter ut dictionary med key og key value.
print(respons.json())

#Henter ut kun passord
print("Passordet er: ", respons.json()["passord"])


#URL for å hente ut data
hent_data_URL = "http://bk-intervju-oppgave-app.azurewebsites.net/api/HentData"

#En funksjon for at den ikke skiller på store og små bokstaver
headers = CaseInsensitiveDict()

#apikey står i casen, header legger inn en "apikey" med passordet som hentes fra den første URL + dictionary
headers["apikey"] = respons.json()['passord']

respons2 = requests.get(url=hent_data_URL, headers=headers)

print("Data som hentes ut er: ", respons2.json()['data'])

