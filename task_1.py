### Task 1.1: Dig this piece of code and try to predict the values of the output. Then, run it to check it.
## Prediction: 42 52


print("Task 1.1: Read the code and predict the result.")
print("Prediction: 42 52")
def f1():
    return 42
def f2(x):
    return 2 * x

print(f1(), f2(5) + f1())

### Task 1.2: Using the following functions, display a lettuce-tomato-double ham sandwich in your terminal.
print("Task 1.2: Using the following functions, display a lettuce-tomato-double ham sandwich in your terminal.")
def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")

bread()
lettuce()
tomato()
ham()
ham()
tomato()
lettuce()
bread()

print("Task 1.3: Write a function that takes a number of sandwiches to prepare as a parameter. Then displays as many sandwiches as requested if the parameter is correct, and I can't do this! if it's not (such as 3.14).")
def num_sandwhiches(num, veg = False):
    if type(num) != int:
        print("I can't do this!")
        return

    else:
       
       for i in range(num):
           print(f"Sandwhich #{i+1}:")
           bread()
           lettuce()
           tomato()
           if not veg: 
            ham()
            ham()
           if veg:
            lettuce()
            tomato()
            tomato()
            lettuce()
           tomato()
           lettuce()
           bread() 

### Test Cases Function
num_sandwhiches(5)
num_sandwhiches(3.14)

### Task 1.4: Add a parameter to provide the possibility for a veg sandwich (double vegetables + no ham). If this option isn't specified, the sandwich must be a lettuce-tomato-double ham one by default
num_sandwhiches(2)
num_sandwhiches(2, True)




