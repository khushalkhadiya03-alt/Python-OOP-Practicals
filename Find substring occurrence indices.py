def find_occurrences(s1, s2):
    indices = []
    start = 0

    while True:
        index = s1.find(s2, start)

        if index == -1:
            break

        indices.append(index)
        start = index + 1

    if len(indices) == 0:
        return -1
    else:
        return indices


# Main program
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

print(find_occurrences(s1, s2))