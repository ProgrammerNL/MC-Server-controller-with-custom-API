import json

# Voorbeeld JSON-bericht
json_bericht = '{"naam": "John", "leeftijd": 30, "stad": "Amsterdam"}'

# JSON naar Python-dictionary vertalen
gegevens = json.loads(json_bericht)

# Toegang krijgen tot de gegevens en deze afdrukken
naam = gegevens["naam"]
leeftijd = gegevens["leeftijd"]
stad = gegevens["stad"]

# Tekstbericht samenstellen
tekst_bericht = f"Naam: {naam}, Leeftijd: {leeftijd}, Stad: {stad}"

# Afdrukken van het vertaalde tekstbericht
print(tekst_bericht)
