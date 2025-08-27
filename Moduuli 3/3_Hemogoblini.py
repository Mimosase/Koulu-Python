gender = input("Enter biological gender (male/female): ")
value = float(input("Enter hemoglobin value (g/l): "))

if gender.lower() == "female":
    if value >= 117 and value <= 155:
        print("Your hemoglobin is normal.")
    elif value < 117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")

elif gender.lower() == "male":
    if value >= 137 and value <= 167:
        print("Your hemoglobin is normal.")
    elif value < 137:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")

else:
    print("Invalid gender.") #all genders are actually valid <3