from random import randint


list = ["kivi", "paber" , "käärid"]

computer = list[randint(0,2)]

player = False

while player == False:
    player = input("kivi, paber, käärid: ")
    if player == computer:
        print("Viik")
    elif player == "kivi":
        if computer == "paber":
            print("Sa kaotasid", computer, "kattab", player)
        else:
            print("Sa võitsid", player, "lõhub", computer)
    elif player == "paber":
        if computer == "käärid":
            print("Sa kaotasid", computer, "lõikab", player)
        else:
            print("Sa võitsid", player, "kattab", computer)
    elif player == "käärid":
        if computer == "kivi":
            print("Sa kaotasid", computer, "lõikab", player)
        else:
            print("Sa võitsid", player, "lõikab", computer)
    else:
        print("Vale sisend, kontrollige sisendit")
    
    choice = input("Kas te tahate uuesti mängida? ")
    if choice = ",jah":
        else choice = "ei"
    
    player = False
    computer = list[randint(0,2)]