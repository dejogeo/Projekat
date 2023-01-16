import sqlite3
import csv



#connection=sqlite3.connect("Politicka_opstina1.db")
#crsr=connection.cursor()

class KO:
    def __init__(self,naziv,KO_id):
        self.naziv=naziv
        self.KO_id = KO_id

    def unos_KO(connection,KO):
        """
                Create a new KO into the KO table
                :param connection:
                :param KO:
                :return: KO id
                """
        crsr = connection.cursor()
        sql = ''' INSERT OR IGNORE INTO KO(naziv,KO_id)
                          VALUES(?,?) '''
        params = (KO.naziv, KO.KO_id)
        crsr.execute(sql, params)
        connection.commit()

    def prenos_KO_id(connection, naziv_KO):
        crsr = connection.cursor()
        crsr.execute("SELECT KO_id FROM KO WHERE naziv=?", (naziv_KO,))
        separator = ", "
        rez_1 = separator.join(crsr.fetchone())
        #rez_1=crsr.fetchone()
        #connection.commit()
        return rez_1
        #print(rez_1)

class Kc:
    def __init__(self, broj_parcele, kc_id, KO_naziv, KO_id):
        self.broj_parcele = broj_parcele
        self.kc_id=kc_id
        self.KO_naziv=KO_naziv
        self.KO_id = KO_id


    def unos_kc(connection,kc):
        """
                Create a new kc into the kc table
                :param connection:
                :param kc:
                :return: kc id
                """
        crsr = connection.cursor()
        sql = ''' INSERT OR IGNORE INTO kc(broj_parcele,kc_id,KO_naziv, KO_id)
                          VALUES(?,?,?,?) '''
        params = (kc.broj_parcele, kc.kc_id,kc.KO_naziv,kc.KO_id)
        crsr.execute(sql, params)
        connection.commit()

    def prenos_kc_id(connection, broj_parcele,naziv_KO):
        crsr = connection.cursor()
        crsr.execute("SELECT kc_id FROM kc WHERE broj_parcele=? AND KO_naziv=?", (broj_parcele,naziv_KO))
        separator = ", "
        rez_2 = separator.join(crsr.fetchone())
        return rez_2

    def kontrola_parcele(connection, broj_kc, naziv_parcele):
        crsr = connection.cursor()
        crsr.execute("SELECT kc_id FROM kc WHERE broj_parcele=? AND KO_naziv=?", (broj_kc,naziv_parcele))
        rez_3 = crsr.fetchall()
        return rez_3


class Vodovod:
    def __init__(self,voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,KO_naziv, kc):
        self.id=voda_id
        self.zona=zona
        self.materijal=materijal
        self.precnik_u_mm=precnik_u_mm
        self.koordinate=koordinate
        self.kota_vrha_cijevi=kota_vrha_cijevi
        self.KO_naziv=KO_naziv
        self.kc=kc


    def unos_vode(connection,voda):

        """
            Create a new voda into the vodovod table
            :param connection:
            :param voda:
            :return: voda id
            """
        crsr = connection.cursor()
        sql=''' INSERT INTO vodovod(voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,KO_naziv, kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (voda.id, voda.zona, voda.materijal, voda.precnik_u_mm, voda.koordinate, voda.kota_vrha_cijevi, voda.KO_naziv, voda.kc)
        crsr.execute(sql, params)
        connection.commit()

    def ispis_vode(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM vodovod WHERE kc_id=?", (idkc,))
        rez = crsr.fetchall()
        return rez

class Struja:
    def __init__(self,struja_id,napon,broj_kablova,koordinate,kota_kabla,KO_naziv, kc):
        self.struja_id=struja_id
        self.napon=napon
        self.broja_kablova=broj_kablova
        self.koordinate=koordinate
        self.kota_kabla=kota_kabla
        self.KO_naziv=KO_naziv
        self.kc=kc

    def unos_struje(connection,struja):

        """
            Create a new struja into the struja table
            :param connection:
            :param struja
            :return: struja id
            """
        crsr = connection.cursor()
        sql=''' INSERT INTO struja(struja_id,napon,broj_kablova,koordinate,kota_kabla,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (struja.struja_id, struja.napon, struja.broja_kablova, struja.koordinate, struja.kota_kabla, struja.KO_naziv, struja.kc)
        crsr.execute(sql, params)
        connection.commit()

    def ispis_struje(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM struja WHERE kc_id=?", (idkc,))
        rez_4 = crsr.fetchall()
        return rez_4

class Toplovod:
    def __init__(self, toplovod_id, materijal, precnik, broj_cijevi, koordinate, kota_cijevi, KO_naziv, kc):
        self.toplovod_id = toplovod_id
        self.materijal = materijal
        self.precnik=precnik
        self.broj_cijevi = broj_cijevi
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc = kc

    def unos_toplovoda(connection, toplovod):
        """
            Create a new toplovod into the toplovod table
            :param connection:
            :param toplovod
            :return: toplovod id
            """
        crsr = connection.cursor()
        sql = ''' INSERT INTO toplovod(toplovod_id, materijal, precnik,broj_cijevi,koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (toplovod.toplovod_id, toplovod.materijal, toplovod.precnik,toplovod.broj_cijevi, toplovod.koordinate, toplovod.kota_cijevi, toplovod.KO_naziv, toplovod.kc)
        crsr.execute(sql, params)
        connection.commit()

    def ispis_toplovoda(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM toplovod WHERE kc_id=?", (idkc,))
        rez_5 = crsr.fetchall()
        return rez_5

class Kanalizacija:
    def __init__(self, kanalizacija_id, oznaka_sistema, materijal, presjek, koordinate, kota_cijevi, KO_naziv, kc):
        self.kanalizacija_id = kanalizacija_id
        self.oznaka_sistema = oznaka_sistema
        self.materijal = materijal
        self.presjek = presjek
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc = kc

    def unos_kanalizacije(connection, kanalizacija):
        """
            Create a new kanalizacija into the kanalizacija table
            :param connection:
            :param kanalizacija
            :return: kanalizacija id
            """
        crsr = connection.cursor()
        sql = ''' INSERT INTO kanalizacija (kanalizacija_id,oznaka_sistema, materijal, presjek, koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (kanalizacija.kanalizacija_id, kanalizacija.oznaka_sistema, kanalizacija.materijal, kanalizacija.presjek, kanalizacija.koordinate,
                  kanalizacija.kota_cijevi, kanalizacija.KO_naziv, kanalizacija.kc)
        crsr.execute(sql, params)
        connection.commit()

    def ispis_kanalizacije(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM kanalizacija WHERE kc_id=?", (idkc,))
        rez_6 = crsr.fetchall()
        return rez_6

class Naftagas:
    def __init__(self, naftagas_id, materijal, precnik, broj_cijevi, koordinate, kota_cijevi, KO_naziv, kc):
        self.naftagas_id = naftagas_id
        self.materijal = materijal
        self.precnik = precnik
        self.broj_cijevi = broj_cijevi
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc = kc

    def unos_naftagasa(connection, naftagas):
        """
        Create a new naftagas into the naftagas table
        :param connection:
        :param naftagas
        :return: naftagas id
        """
        crsr = connection.cursor()
        sql = ''' INSERT INTO naftagas (naftagas_id,materijal, precnik, broj_cijevi, koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (naftagas.naftagas_id, naftagas.materijal, naftagas.precnik, naftagas.broj_cijevi, naftagas.koordinate,naftagas.kota_cijevi,naftagas.KO_naziv,naftagas.kc)
        crsr.execute(sql, params)
        connection.commit()

    def ispis_naftagasa(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM naftagas WHERE kc_id=?", (idkc,))
        rez_7 = crsr.fetchall()
        return rez_7

class Telekom:
    def __init__(self,telekom_id,vrsta_kabla,broj_cijevi,koordinate,kota_cijevi,KO_naziv,kc):
        self.telekom_id=telekom_id
        self.vrsta_kabla=vrsta_kabla
        self.broj_cijevi=broj_cijevi
        self.koordinate=koordinate
        self.kota_cijevi=kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc=kc

    def unos_telekoma(connection,telekom):

        """
            Create a new telekom into the telekom table
            :param connection:
            :param telekom
            :return: telekom id
            """

        crsr=connection.cursor()
        sql=''' INSERT INTO telekom(telekom_id,vrsta_kabla,broj_cijevi, koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (telekom.telekom_id, telekom.vrsta_kabla, telekom.broj_cijevi, telekom.koordinate, telekom.kota_cijevi, telekom.KO_naziv, telekom.kc)
        crsr.execute(sql, params)
        connection.commit()

    def ispis_telekoma(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM telekom WHERE kc_id=?", (idkc,))
        rez_8 = crsr.fetchall()
        return rez_8