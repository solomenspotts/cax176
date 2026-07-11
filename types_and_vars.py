grade = input("Please enter your grade") # Asks the user to input a numeric grade 

if int(grade) >= 90:
    print("A")
elif  80 <= int(grade) < 89:
    print("B")
elif 70 <= int(grade) < 80:
    print("C")
elif 60 <= int(grade) < 69:
    print("D")
else:
    print("F")
