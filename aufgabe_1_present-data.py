import pandas as pd # für Datenimport
import os # für Dateipfade



# Dateinamen definieren und Dateipfade erstellen 
customers_file = "data/customers.csv"
customers_path = os.path.join(os.getcwd(), customers_file)
offers_file = "data/offers.csv"
offers_path = os.path.join(os.getcwd(), offers_file)
contacts_file = "data/contacts.csv"
contacts_path = os.path.join(os.getcwd(), contacts_file)


# Datensätze laden, Übersicht anzeigen und Datentypen ausgeben
customers_data = pd.read_csv(customers_path)
print("\nÜbersicht von Kunden-Datensatz:", )
print(customers_data.head())
print("\nDatentypen im Kunden-Datensatz:")
print(customers_data.dtypes)

offers_data = pd.read_csv(offers_path)
print("\nÜbersicht von Angebote-Datensatz:")
print(offers_data.head())
print("\nDatentypen im Angebote-Datensatz:")
print(offers_data.dtypes)

contacts_data = pd.read_csv(contacts_path)
print("\nÜbersicht von Kontakte-Datensatz:")
print(contacts_data.head())
print("\nDatentypen im Kontakte-Datensatz:")
print(contacts_data.dtypes)


# Datensätze aufräumen

# For-Schleife zum Vergleichen der Werte in den ersten beiden Spalten
# Können die ersten beiden Spalten gestrichen werden?
for index, row in customers_data.iterrows():
    if row['Unnamed: 0'] - row['Unnamed: 0.1'] != 0:
        print(f"Fehler in Zeile {index+1}: Wert von Spalte B ist nicht gleich dem Wert von Spalte A")

# Entscheidung dafür, die ersten beiden Spalten zu streichen

customers_data = customers_data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1) # drop-Funktion gibt es ein neues DataFrame aus


""" # Statistische Zusammenfassung der numerischen Spalten im Kunden-Datensatz anzeigen
print("Statistische Zusammenfassung des Kundenwerts:")
print(customers_data["customer_value"].describe())

# Statistische Zusammenfassung der Dauer im Angebote-Datensatz anzeigen
print("Statistische Zusammenfassung der Dauer der Angebote:")
print(offers_data["duration"].describe()) """

