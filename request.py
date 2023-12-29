import requests

url = "http://127.0.0.1:5000/"
response = requests.get(url)

if response.status_code == 200:
    # Succesvolle respons
    data = response.json()  # Als de respons JSON is
    print("API Response:", data)
else:
    # Fout bij het verzoek
    print("Fout bij het verzoek. Status code:", response.status_code)
