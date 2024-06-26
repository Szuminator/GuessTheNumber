import random

x = random.randrange(1, 101)
ans=0
while(ans!=x):
    try:
        ans= int(input("Zgadnij liczbe: "))
        if (ans < x):
            print("za mała proboj dalej")
        elif (ans > x):
            print("za duża proboj dalje")
    except ValueError:
        print("tylko cyfry")

print("brawooo zhgadłes")
