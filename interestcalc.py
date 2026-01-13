principle =  0
rate = 0
time = 0

while  principle <=0 :
    principle = float(input("enter the principle amount: "))
    if principle <= 0:
        print("principle cannot be less than or equal to zero")

while  rate <=0 :
    rate = float(input("enter the rate interest: "))
    if rate <= 0:
        print("rate cannot be less than or equal to zero")

while  time <=0 :
    time = float(input("enter the number of years: "))
    if time <= 0:
        print("time cannot be less than or equal to zero")

total = principle * pow((1+rate/100), time)
print(f"balance after {time} year/s: {total:.2f}")