
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def primes_till_n(n):
    print("Prime numbers till", n, "are:")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")
    print()


def first_n_primes(n):
    print("First", n, "prime numbers are:")
    count = 0
    num = 2

    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()


# Main program
n = int(input("Enter a number: "))

# (a) Check if n is prime
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# (b) Generate all prime numbers till n
primes_till_n(n)

# (c) Generate first n prime numbers
if n > 0:
    first_n_primes(n)
else:
    print("Enter a positive number for the first n primes.")
