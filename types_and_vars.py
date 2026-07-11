grade = input("Please enter your grade ") # Asks the user to input a numeric grade 

if int(grade) >= 90:
    print("Your grade is A")
elif  80 <= int(grade):
    print("Your grade is B")
elif 70 <= int(grade):
    print("Your grade is C")
elif 60 <= int(grade):
    print("Your grade is D")
else:
    print("Your grade is F")
