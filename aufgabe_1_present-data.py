import pandas as pd
import os

# Dateinamen definieren
customers_file = "data/customers.csv"
offers_file = "data/offers.csv"
contacts_file = "data/contacts.csv"

# Vollständige Dateipfade erstellen
customers_path = os.path.join(os.getcwd(), customers_file)
offers_path = os.path.join(os.getcwd(), offers_file)
contacts_path = os.path.join(os.getcwd(), contacts_file)


# Kunden-Datensatz laden und anzeigen
customers_data = pd.read_csv(customers_path)
print("Kunden-Datensatz:")
print(customers_data.head())

# Angebote-Datensatz laden und anzeigen
offers_data = pd.read_csv(offers_path)
print("\nAngebote-Datensatz:")
print(offers_data.head())

# Kontakte-Datensatz laden und anzeigen
contacts_data = pd.read_csv(contacts_path)
print("\nKontakte-Datensatz:")
print(contacts_data.head())



# Datentypen im Kunden-Datensatz anzeigen
print("\nDatentypen im Kunden-Datensatz:")
print(customers_data.dtypes)

# Datentypen im Angebote-Datensatz anzeigen
print("\nDatentypen im Angebote-Datensatz:")
print(offers_data.dtypes)

# Datentypen im Kontakte-Datensatz anzeigen
print("\nDatentypen im Kontakte-Datensatz:")
print(contacts_data.dtypes)