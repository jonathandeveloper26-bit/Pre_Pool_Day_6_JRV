### Task 2.1: Write a recursive function that computes the sum of all integers from 1 to n, a given parameter.
print("Task 2.1: Write a recursive function that computes the sum of all integers from 1 to n, a given parameter.")
def sum_integers_one_to_n(n):
    value = 0
    if n == 0:
        return n
    else:
        return n + sum_integers_one_to_n(n-1)

test_sum_integers = 5
print(f"Test Case: {test_sum_integers}")
print(f"Sum of Integers: {sum_integers_one_to_n(test_sum_integers)}")
print("\n")
