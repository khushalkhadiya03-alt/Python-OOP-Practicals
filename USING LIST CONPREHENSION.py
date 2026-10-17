lst = eval(input("Enter a list: "))

cubes = [x ** 3 for x in lst
         if type(x) == int and x % 2 == 0]

print("Cubes of even integers:", cubes)