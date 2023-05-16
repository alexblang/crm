import pandas as pd
import os



# Dateinamen definieren und Dateipfade erstellen 
customers_file = "data/customers.csv"
customers_path = os.path.join(os.getcwd(), customers_file)
offers_file = "data/offers.csv"
offers_path = os.path.join(os.getcwd(), offers_file)
contacts_file = "data/contacts.csv"
contacts_path = os.path.join(os.getcwd(), contacts_file)


# Datensätze laden und anzeigen
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
# Spaltenbezeichnungen des Kunden-Datensatzes
customers_columns = list(customers_data.columns)
print("Spaltenbezeichnungen des Kunden-Datensatzes:")
print(customers_columns)


# Datentypen im Angebote-Datensatz anzeigen
print("\nDatentypen im Angebote-Datensatz:")
print(offers_data.dtypes)
# Spaltenbezeichnungen des Angebote-Datensatzes
offers_columns = list(offers_data.columns)
print("\nSpaltenbezeichnungen des Angebote-Datensatzes:")
print(offers_columns)

# Datentypen im Kontakte-Datensatz anzeigen
print("\nDatentypen im Kontakte-Datensatz:")
print(contacts_data.dtypes)
# Spaltenbezeichnungen des Kontakte-Datensatzes
contacts_columns = list(contacts_data.columns)
print("\nSpaltenbezeichnungen des Kontakte-Datensatzes:")
print(contacts_columns)








""" # Statistische Zusammenfassung der numerischen Spalten im Kunden-Datensatz anzeigen
print("Statistische Zusammenfassung des Kundenwerts:")
print(customers_data["customer_value"].describe())

# Statistische Zusammenfassung der Dauer im Angebote-Datensatz anzeigen
print("Statistische Zusammenfassung der Dauer der Angebote:")
print(offers_data["duration"].describe()) """

