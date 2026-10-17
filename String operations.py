# Accept a string
s = input("Enter a string: ")

# (a) Find frequency of a character
ch = input("Enter character to find frequency: ")
print("Frequency =", s.count(ch))

# (b) Replace a character
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", s.replace(old, new))

# (c) Remove the first occurrence of a character
ch = input("Enter character to remove (first occurrence): ")
print("After removing first occurrence:", s.replace(ch, "", 1))

# (d) Remove all occurrences of a character
ch = input("Enter character to remove (all occurrences): ")
print("After removing all occurrences:", s.replace(ch, ""))