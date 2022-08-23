import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

CRIA_TABELA = "create table if not exists hoteis(\
    hotel_id TEXT PRIMARY KEY,\
    nome TEXT,\
    estrelas real,\
    diaria real,\
    cidade TEXT)"

INSERE_HOTEL = "INSERT INTO hoteis values('alpha', 'Alpha hotel', 4.3, 300.14, 'Recife')"
INSERE_HOTEL = "INSERT INTO hoteis values('Bravo', 'Bravo restaurante hotel', 4.5, 500.80, 'Caruaru')"
INSERE_HOTEL = "INSERT INTO hoteis values('Delta', 'Delta resort hotel', 4.3, 200.45, 'Recife')"
INSERE_HOTEL = "INSERT INTO hoteis values('Gama', 'Hostel Gama', 4.3, 300.14, 'Recife')"
INSERE_HOTEL = "INSERT INTO hoteis values('alpha', 'Alpha hotel', 4.3, 300.14, 'Recife')"

cursor.execute(CRIA_TABELA)
connection.commit()
connection.close()
