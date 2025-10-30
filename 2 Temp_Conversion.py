Temp = int(input("Enter a temperature: "))
unit = input("Celsius or Fahrenheit (C/F): ")

if unit.lower() == "c":
    print(f"{Temp}c° = {Temp* 9/5 + 32}f° ")

elif unit.lower() == "c":
    print(f"{Temp}f° = {(Temp - 32)* 5/9}c°")
