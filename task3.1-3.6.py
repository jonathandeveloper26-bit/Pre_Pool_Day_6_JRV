### Task 3.1: Use some built-in functions to get:
# ✓ the absolute value of 2,-2 and -3e4
# ✓ the rounded value of 3.14159 to two decimal places;
# ✓ the maximum value of[ 42, 3e2, 666]

print("*"*30)
print("Task 3.1A: the absolute value of 2,-2 and -3e4")
values = [2, -2, -3e4]
print(f"Given Values: {values}")
values = [abs(value) for value in values]
print(f"Absolute Values: {values}")

print("Task 3.1B: the rounded value of 3.14159 to two decimal places")
value = 3.14159
print(f"Given Value: {value}")
value = round(value,2)
print(f"Rounded Value: {value}")

print("Task 3.1C: the maximum value of [42, 3e2, 666]")
values = [42, 3e2, 666]
print(f"Given Values: {values}")
max_value = max(values)
print(f"Maximum Value: {max_value}")

print("*"*30)

print("*"*30)
print("Task 3.2: Apply the min() built-in function on the string 'Beautiful is better than ugly..' What do you observe? What do you make of it?")

print(min("Beautiful is better than ugly.."))

print("Observation: An empty line is printed...")
print("What do I make of it: A space is the lowest possible value of a character?")
print("*"*30)

print("*"*30)
print("Task 3.3: Using a built-in function, compute the value of 73 to the power 73.")
base = 73
exponent = 73
print(pow(base,exponent))
print("*"*30)

print("*"*30)
print("Task 3.4: What are the built-in functions that return:\n✓ True if there is at least one true element in a list?\n✓ True if there is zero false element in a list?")
print("Answer A: The built in function is - any(). Examples use: any(x > 10 for x in list_nums)")

list_nums = [0, 5, 3, 12, 5, 6]
print(f"Example 1: {list_nums}")
print(f"Answer 1: {any(x > 10 for x in list_nums)}")
list_nums = [0, 5, 3, 8, 6]
print(f"Example 2: {list_nums}")
print(f"Answer 2: {any(x > 10 for x in list_nums)}")
print("*"*30)

print("Answer B: The built in function is - all(). Examples use: all(x > 10 for x in list_nums)")

list_nums = [0, 5, 3, 12, 5, 6]
print(f"Example 1: {list_nums}")
print(f"Answer 1: {all(x > 10 for x in list_nums)}")
list_nums = [100, 50, 30, 80, 65]
print(f"Example 2: {list_nums}")
print(f"Answer 2: {all(x > 10 for x in list_nums)}")
print("*"*30)

### Task 3.5: Using a built-in function, calculate the sum of L1 + L2 + L3 + L4 where:
# ✓L1 = [1,2, 3, 4];
# ✓L2 = [5,7, 9, 32];
# ✓L3 = [23, 13, 17, 14, 16, 309]
# ✓L4 = [10, 20, 30, 40]
print("*"*30)
print("Task 3.5: Using a built-in function, calculate the sum of L1 + L2 + L3 + L4 where: ")
print("✓L1 = [1, 2, 3, 4];")
print("✓L2 = [5, 7, 9, 32];")
print("✓L3 = [23, 13, 17, 14, 16, 309]")
print("✓L4 = [10, 20, 30, 40]")

l1 = [1, 2, 3, 4]
l2 = [5, 7, 9, 32]
l3 = [23, 13, 17, 14, 16, 309]
l4 = [10, 20, 30, 40]

sum_lists = sum([*l1, *l2, *l3, *l4])
print(f"Sum of Lists: {sum_lists}")

print("*"*30)

### Task 3.6 Find an easy way to sort the names in this list:
# ✓ from shortest to longest; 
# ✓ from longest to shortest.
# ["Joe", "William", "Jack", "Averell"]
print("*"*30)

print("Task 3.6 Find an easy way to sort the names in this list:")
print("✓ from shortest to longest;")
print("✓ from longest to shortest.")
names = ["Joe", "William", "Jack", "Averell"]
print(f"Given List: {names}")


print(f"Sorted List (s->l): {sorted(names, key=len)})")
print(f"Sorted List (l->s): {sorted(names, key=len, reverse=True)}")


print("*"*30)



