import mysql.connector

def hae_lentokentta(icao_code):
    sql = f"SELECT airport.name, airport.municipality FROM airport WHERE airport.ident = '{icao_code}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if not tulos:
        print(f"No airport found with ICAO code {icao_code}")
        return

    print(f"Airport name: {tulos[0]}")
    print(f"Location: {tulos[1]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )

input_code = input("Enter the ICAO code of an airport: ").upper()
hae_lentokentta(input_code)