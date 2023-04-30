""""
Student: Juan Plasencia

"""
#Asking the user for their grade percentage
print("\nHello, this is your Grate Bot, please enter your grade percentage from 0 - 100 on the following:\n")
grade = int(input("What is your grade percentage? "))
letter = "F"
sing = ""

#Determining the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"

if grade % 10 >= 7:
    sing = "+"
elif grade % 10 <= 3:
    sing = "-"

#Showing results
if letter in("AF"):
    print(f"Hey! your letter grade is: {letter}")
else:
    print(f"Hey! your letter grade is: {letter}{sing}")
if letter in("DF"):
    print("Sorry, You didn't pass, please improve your performance for next time")
else:
    print("Congrats! You passed the class!")