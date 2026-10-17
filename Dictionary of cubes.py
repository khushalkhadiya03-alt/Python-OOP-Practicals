
def cube_dictionary():
    cubes = {}
    n = int(input("How many numbers do you want to enter? "))

    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        cubes[num] = num ** 3

    return cubes


result = cube_dictionary()
print("Dictionary of cubes:", result)
