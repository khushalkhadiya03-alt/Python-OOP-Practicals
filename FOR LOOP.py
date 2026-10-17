lst =eval(input("Enter a list: "))
cubes = []

for x in lst:
    if type(x) == int and x % 2 == 0:
        cubes.append(x ** 3)

print("Cubes of even integers:", cubes)