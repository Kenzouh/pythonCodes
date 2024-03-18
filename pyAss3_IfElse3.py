print("=============================")
print("||   Python Assignment #2  ||")
print("||   If-Else Statement 3   ||")
print("=============================")

print("\nSubmitted to:      Dr. Aleta Fabregas")
print("Submitted by:      Kenzo C. Ragundiaz")
print("                   (BSIT 2-5)")
print("Date submitted:    March 15, 2024 (Friday) ")

print("\n=================================\n")

print("Welcome to Kenzo Hotel!\n")

reservation = input("Do you have a reservation [y] if yes, [n] if no: ")

if reservation == 'y':
    code = input("Do you have a code [y] if yes, [n] if no:")

    if code == "Y" or "y":
        print("\nHere are your keys!")
    else:
        print("\nOkay.")

elif reservation == "N" or "n":
    print("\nNice!")

else:
    print("\nHave a good day!")



#NESTED IF

#HOTEL
# NORMAL ROOM / 5 STAR ROOM / VIP ROO
# CASH OR CREDIT CARD