import random

yMin=0
yMax=101
goal=random.randint(yMin,yMax)
algarv=102

while algarv != goal:
    algarv= int(input("arv: "))
    if algarv > goal:
        print("Liiga suur")
    elif algarv < goal:
            print("Liiga väike")
print("Õige vastus")