# Read the file
f = open("data.txt", "r")
text = f.read()
f.close()

# (a) Count characters, words and lines
lines = text.splitlines()
words = text.split()

print("Total characters:", len(text))
print("Total words:", len(words))
print("Total lines:", len(lines))

# (b) Frequency of each character
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")
print(freq)

# (c) Print words in reverse order
print("Words in reverse order:")
print(" ".join(words[::-1]))

# (d) Copy even lines to File1 and odd lines to File2
f1 = open("File1.txt", "w")
f2 = open("File2.txt", "w")

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        f1.write(lines[i] + "\n")
    else:
        f2.write(lines[i] + "\n")

f1.close()
f2.close()

print("Even lines copied to File1.txt")
print("Odd lines copied to File2.txt")