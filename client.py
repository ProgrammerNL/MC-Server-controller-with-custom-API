from tkinter import *
import requests
import json
from datetime import datetime
app = Tk()
app.geometry("450x450")
app.title("Client test")

def load_api():
    pass

datafield = Text(app, width=450, height=450)

url = "http://127.0.0.1:5000/"
response = requests.get(url)

if response.status_code == 200:
    # Succesvolle respons
    data = response.json()  # Als de respons JSON is
    print("API Response:", data)
else:
    # Fout bij het verzoek
    print("Fout bij het verzoek. Status code:", response.status_code)

def refreshapi():
    response = requests.get(url)
    data = response.json()
    print("Refresh data")
    datafield.delete("1.0", END)
    print("Old data is deleted")
    time = datetime.now().strftime("%H:%M:%S")
    datafield.insert("end", time + " " + onlineplayers)
    print("Data succesfully refreshed")

k1 = Button(text="refresh", command=refreshapi, pady=5)
k1.pack()
onlineplayers = data.get("message", "geen bericht gevonden.")
datafield.insert("end", onlineplayers)
datafield.pack()

app.mainloop()