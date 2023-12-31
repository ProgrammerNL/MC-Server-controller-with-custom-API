from tkinter import *
import requests
import json
from datetime import datetime
app = Tk()
app.geometry("750x750")
app.title("Client test")

console = Tk()
console.geometry("400x400")
console.title("Console")

def load_api():
    pass

datafield = Text(app, width=450, height=450)
consolefield = Text(console, width=400, height=400)
url = "http://127.0.0.1:5000/api/getplayercount"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Als de respons JSON is
    print("API Response:", data)
else:
    print("Fout bij het verzoek. Status code:", response.status_code)

def refreshapi():
    time = datetime.now().strftime("%H:%M:%S")
    consolefield.delete("1.0", END)
    consolefield.insert("end", time + " : Refreshing API")
    
    response = requests.get(url)
    data = response.json()
    datafield.delete("1.0", END)
    time = datetime.now().strftime("%H:%M:%S")
    datafield.insert("end", time + " " + onlineplayers)

k1 = Button(text="refresh", command=refreshapi, pady=5)
k1.pack()
onlineplayers = data.get("message", "geen bericht gevonden.")
datafield.insert("end", onlineplayers)
consolefield.insert("end", "Console loaded")

datafield.pack()
consolefield.pack()
console.mainloop()
app.mainloop()