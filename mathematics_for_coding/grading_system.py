#Ask the user to input a score
score = int(input("Enter the student's score (0 - 100): "))



if score >= 70:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >=50:
    grade = 'C'
elif score >=45:
    garde = 'D'
elif score >=40:
    grade = 'E'
else:
    grade = 'F'

print (f"Your Garde is: {grade}") # Outputs
