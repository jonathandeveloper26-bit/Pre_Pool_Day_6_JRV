### Challenge: Write a little program that computes the power function as fast as possible.
import time

def compute_power(base, exponent):
    return base ** exponent

def compute_power_non_operator(base, exponent):
    answer = base
    if exponent == 1:
        return answer
    else:
        answer = answer * compute_power_non_operator(base, exponent-1)

    return answer

print("Using ** Operator")
start_time = time.time()
compute_power(42,84)

print(f"Time Elapsed (42^84): {time.time()-start_time}")
print(f"Answer: {compute_power(42,84)}")

start_time = time.time()

compute_power(42,168)

print(f"Time Elapsed (42,168): {time.time()-start_time}")
print(f"Answer: {compute_power(42,168)}")

print("\nUsing Recusive Function")
start_time = time.time()
compute_power_non_operator(42,84)

print(f"Time Elapsed (42^84): {time.time()-start_time}")
print(f"Answer: {compute_power_non_operator(42,84)}")

start_time = time.time()

compute_power_non_operator(42,168)

print(f"Time Elapsed (42,168): {time.time()-start_time}")
print(f"Answer: {compute_power_non_operator(42,168)}")
