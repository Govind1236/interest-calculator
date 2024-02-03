
# Assignment:
# Write a Python program that defines a function called "find_primes_in_range" which finds and returns all prime numbers within a given range. The function should take two parameters, "start" and "end", representing the range (inclusive). Then, in your program, prompt the user to enter the start and end of the range, call the "find_primes_in_range" function with these values, and print the prime numbers found in the range.

# Here's a step-by-step guide:

# 1. Define a function called "find_primes_in_range" that takes two parameters, "start" and "end".
# 2. Inside the function, write logic to find all prime numbers within the given range (inclusive).
# 3. Use a loop to iterate through each number in the range.
# 4. For each number, check if it is prime using a helper function (you can reuse the "check_prime" function from the previous assignment).
# 5. If a number is prime, add it to a list of prime numbers.
# 6. Return the list of prime numbers.
# 7. Prompt the user to enter the start and end of the range.
# 8. Call the "find_primes_in_range" function with the user-provided start and end values.
# 9. Print the prime numbers found in the range.

# Feel free to reuse the "check_prime" function or implement a new method to check for prime numbers. This assignment should give you a good opportunity to practice function composition and more complex logic.

# Give it a try, and let me know if you need further guidance or assistance!
def check_even(num):
    return num % 2 == 0


def find_even_in_range(start, end):
   evens = []
   for i in range(start, end):
      is_even = check_even(i)
      if is_even:
         evens.append(i)
   return evens


even_numbers = find_even_in_range(1,100)
print(even_numbers)
