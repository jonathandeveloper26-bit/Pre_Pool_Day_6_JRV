### Task 2.2: Write a recursive function count_digits(n) that takes a positive integer and returns the total number of digits it contains.

def count_digits(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + count_digits(n//10)

print(count_digits(42000))