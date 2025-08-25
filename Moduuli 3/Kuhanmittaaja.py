length = float(input("Enter the length of the zander in centimeters: "))
if length >= 42.0:
    print("The zander meets the size limit.")

else:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    missing_length = 42.0 - length
    print(f"The fish was {missing_length:.1f} centimeters below the size limit.")