
try:
    name = input("Enter your name: ")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must not contain digits or special characters!")

    print("Name:", name)

except ValueError as e:
    print("Error occurred:", e)
