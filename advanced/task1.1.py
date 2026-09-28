### Advanced: Write a function analyze_grades(grades) that takes a list of numbers representing student scores. Using the built-in functions you learned today, the function must calculate and print:
#- The highest grade in the class.
#- The lowest grade in the class.
#- The average grade.

print("Task 1.1: Write a function analyze_grades(grades) that takes a list of numbers representing student scores. Using the built-in functions you learned today, the function must calculate and print:")
print(" - The highest grade in the class.")
print(" - The lowest grade in the class.")
print(" - The average grade of the class.")

def analyze_grades(grades):
    print(max(grades))
    print(min(grades))
    print(round(sum(grades)/len(grades),2))

test_grades = [45, 82, 91, 37, 64, 12]
analyze_grades(test_grades)



