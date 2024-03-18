print("=============================")
print("||   Python Assignment #2  ||")
print("||   If-Else Statement 1   ||")
print("=============================")

print("\nSubmitted to:      Dr. Aleta Fabregas")
print("Submitted by:      Kenzo C. Ragundiaz")
print("                   (BSIT 2-5)")
print("Date submitted:    March 15, 2024 (Friday) ")

print("\n=================================\n")

print("Welcome to Kenzo University!")

g7Grade = float(input("Please enter Grade 7 grade: "))
g8Grade = float(input("Please enter Grade 8 grade: "))
g9Grade = float(input("Please enter Grade 9 grade: "))
g10Grade = float(input("Please enter Grade 10 grade: "))
g11Grade = float(input("Please enter Grade 11 grade: "))
g12Grade = float(input("Please enter Grade 12 grade: "))

gradeTotal = g7Grade + g8Grade + g9Grade + g10Grade + g11Grade + g12Grade

gradeAverage = gradeTotal / 6
gradeAverage = round(gradeAverage, 2)

print(f"\nTotal Grade: {gradeTotal}")
print(f"Average Grade: {gradeAverage}")

if(gradeAverage >= 85):
    print("\nCongratulations! You got admitted to Kenzo University! :D")

else:
    print("\nYou failed. Grade must be greater than or equals to 85 to be admitted.")

