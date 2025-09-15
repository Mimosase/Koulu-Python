import mysql.connector

def get_airports_by_country(country_code):
    sql = f"SELECT type, COUNT(ident) FROM airport WHERE iso_country = '{country_code}' GROUP BY type"
    #print(sql)

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if not tulos:
        print(f"No airports found for country code '{country_code}' or database connection failed.")
        return

    print(f"Airports in {country_code}:")
    for type in tulos:
        print(f"{type[1]} {type[0]} airports")

    return

def run_country_program():
    input_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    get_airports_by_country(input_code)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )

run_country_program()