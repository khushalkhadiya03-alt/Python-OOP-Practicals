s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter the value of n: "))

if 0 <= n <= len(s1) and n <= len(s2):
    a = s1[:n]
    b = s2[:n]

    s1 = b + s1[n:]
    s2 = a + s2[n:]

    print("First string after swapping:", s1)
    print("Second string after swapping:", s2)
else:
    print("Invalid value of n")