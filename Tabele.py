import sqlite3
connection=sqlite3.connect("Politicka_opstina1.db")
crsr=connection.cursor()
sql_command="""CREATE TABLE IF NOT EXISTS KO (                       
naziv VARCHAR(30) PRIMARY KEY,
KO_id VARCHAR);"""
crsr.execute(sql_command)
connection.commit()                                                        #Tabela katastarske opštine
crsr.execute("""CREATE TABLE IF NOT EXISTS kc (
broj_parcele VARCHAR(8),
kc_id VARCHAR PRIMARY KEY,
KO_naziv VARCHAR (30),
KO_id VARCHAR,
CONSTRAINT fk_KO
    FOREIGN KEY (KO_id)
    REFERENCES KO(KO_id));""")
connection.commit()                                                         #Tabela parcele
sql_command="""CREATE TABLE IF NOT EXISTS vodovod (
voda_id VARCHAR PRIMARY KEY,
zona INTEGER,
materijal VARCHAR(10),
precnik_u_mm FLOAT,
koordinate VARCHAR,
kota_vrha_cijevi FLOAT,
KO_naziv VARCHAR (30),
kc_id VARCHAR,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)
connection.commit()                                                          #Tabela vodovoda
sql_command="""CREATE TABLE IF NOT EXISTS struja (
struja_id VARCHAR PRIMARY KEY,
napon INTEGER,
broj_kablova INTEGER,
koordinate VARCHAR,
kota_kabla FLOAT,
KO_naziv VARCHAR (30),
kc_id VARCHAR,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)
connection.commit()                                                          #Tabela elektroenergetskog voda

sql_command="""CREATE TABLE IF NOT EXISTS toplovod (
toplovod_id VARCHAR PRIMARY KEY,
materijal VARCHAR(20),
precnik FLOAT,
broj_cijevi INTEGER,
koordinate VARCHAR,
kota_cijevi FLOAT,
KO_naziv VARCHAR (30),
kc_id VARCHAR,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)                                                           #Tabela toplovoda
sql_command="""CREATE TABLE IF NOT EXISTS kanalizacija (
kanalizacija_id VARCHAR PRIMARY KEY,
oznaka_sistema VARCHAR(10),
materijal VARCHAR(20),
presjek FLOAT,
koordinate VARCHAR,
kota_cijevi FLOAT,
KO_naziv VARCHAR (30),
kc_id VARCHAR,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)                                                   #Tabela kanalizacije
sql_command="""CREATE TABLE IF NOT EXISTS naftagas (
naftagas_id VARCHAR PRIMARY KEY,
materijal VARCHAR(20),
precnik FLOAT,
broj_cijevi INTEGER,
koordinate VARCHAR,
kota_cijevi FLOAT,
KO_naziv VARCHAR (30),
kc_id VARCHAR,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)                                                   #Tabela voda nafte i plina
sql_command="""CREATE TABLE IF NOT EXISTS telekom (
telekom_id VARCHAR PRIMARY KEY,
vrsta_kabla VARCHAR(20),
broj_cijevi INTEGER,
koordinate VARCHAR,
kota_cijevi FLOAT,
KO_naziv VARCHAR (30),
kc_id VARCHAR,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)
connection.commit()
connection.close()
