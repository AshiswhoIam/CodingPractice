#calc for compound interest

initial_balance=0
rate=0
time=0

while initial_balance<=0:
    initial_balance=float(input("Enter the initial amount: "))
    if initial_balance<=0:
        print("initial amount cannot be less than or equal to zero")


while rate<=0:
    rate=float(input("Enter the rate amount: "))
    if rate<=0:
        print("rate amount cannot be less than or equal to zero")

while time<=0:
    time=int(input("Enter the time in yrs: "))
    if time<=0:
        print("Time cannot be less than or equal to zero")

print(initial_balance)
print(rate)
print(time)

total=initial_balance*pow(1+rate/100,time)
print(f"Balance after {time}yrs : ${total:.2f}")