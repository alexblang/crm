import pandas as pd # für Datenimport
import os # für Dateipfade
import sys
from datetime import datetime # um Datum und Uhrzeit im Überblick auszugeben



# Dateinamen definieren und Dateipfade erstellen 
customers_file = "data/customers.csv"
customers_path = os.path.join(os.getcwd(), customers_file)
offers_file = "data/offers.csv"
offers_path = os.path.join(os.getcwd(), offers_file)
contacts_file = "data/contacts.csv"
contacts_path = os.path.join(os.getcwd(), contacts_file)


# Datensätze als Pandas-Dataframes laden 
customers_data = pd.read_csv(customers_path)
offers_data = pd.read_csv(offers_path)
contacts_data = pd.read_csv(contacts_path)


# Datensätze aufräumen

# For-Schleife zum Vergleichen der Werte in den ersten beiden Spalten
# Können die ersten beiden Spalten gestrichen werden?
for index, row in customers_data.iterrows():
    if row['Unnamed: 0'] - row['Unnamed: 0.1'] != 0:
        print(f"Fehler in Zeile {index+1}: Wert von Spalte B ist nicht gleich dem Wert von Spalte A")

# Entscheidung dafür, die ersten beiden Spalten zu streichen

customers_data = customers_data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1) # drop-Funktion gibt es ein neues DataFrame aus


# Hier wird der Überblick gespeichert
output_file = "data_overview.txt"

# Öffnen der Ausgabedatei im Schreibmodus
with open(output_file, "w") as file:
    # Umleitung der Standardausgabe auf die Datei
    original_stdout = sys.stdout
    sys.stdout = file

    print("Datum und Uhrzeit:", datetime.now())
    
    print("\n\nDATENSATZ CUSTOMERS")
    print("Übersicht von Kunden-Datensatz\n")
    print(customers_data.info())
    print("\nDatentypen im Kunden-Datensatz\n")
    print(customers_data.dtypes)

    print("\n\nDATENSATZ OFFERS")
    print("Übersicht von Angebote-Datensatz\n")
    print(offers_data.info())
    print("\nDatentypen im Angebote-Datensatz\n")
    print(offers_data.dtypes)

    print("\n\nDATENSATZ CONTACTS")
    print("\n\nÜbersicht von Kontakte-Datensatz\n")
    print(contacts_data.info())
    print("\nDatentypen im Kontakte-Datensatz\n")
    print(contacts_data.dtypes)

    # Rückkehr zur Standardausgabe
    sys.stdout = original_stdout

# Bestätigungsnachricht
print(f"Der Überblick über die Daten wurde in die Datei {output_file} geschrieben.")


# Übersicht anzeigen und Datentypen ausgeben






""" # Statistische Zusammenfassung der numerischen Spalten im Kunden-Datensatz anzeigen
print("Statistische Zusammenfassung des Kundenwerts:")
print(customers_data["customer_value"].describe())

# Statistische Zusammenfassung der Dauer im Angebote-Datensatz anzeigen
print("Statistische Zusammenfassung der Dauer der Angebote:")
print(offers_data["duration"].describe()) """

