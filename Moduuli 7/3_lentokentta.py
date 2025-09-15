airports = {}
#airports-sanakirja

while True:
    print()
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    ans = int(input("Please choose an option (1-3): "))

    if ans == 1:
        ICAO_code = input("Enter the ICAO code: ")
        airport_name = input("Enter the airport name: ")
        airports[ICAO_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {ICAO_code} has been added.")

    elif ans == 2:
        alt_ICAO = input("Enter the ICAO code: ")
        if alt_ICAO in airports:
            print(f"The airport with ICAO code {alt_ICAO} is {airports[ICAO_code]}.")
        else:
            print(f"No airport found with ICAO code {alt_ICAO}.")

    elif ans == 3:
        break

print("Thank you for using the Airport Data Management system. Goodbye!")