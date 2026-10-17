ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")

elif ch.isalpha():
    print("The character is a letter.")

    if ch.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")

elif ch.isdigit():
    print("The character is a numeric digit.")

    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
              "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    print("Digit in words:", digits[int(ch)])

else:
    print("The character is a special character.")