unit = input("is this temp in celcius or farhenit (C/F): ")
temp = float(input("enter the temperature: "))

if unit == "C":
   temp = round((9 * temp)/ 5 + 32 , 1)
   print(f"temperature in fara is {temp}: ")

elif unit == "F":
   temp = round((temp - 32) * 5/9,1)
   print(f"temperature in fara {temp}: ")

else:
   print(f"{unit} is an invalid unit of mesurement")