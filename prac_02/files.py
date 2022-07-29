# 1.
OUTPUT_FILE = "name.txt"
name = input("Your name? ")
OUT_FILE = open(OUTPUT_FILE, 'w')
print(name, file=OUT_FILE)
OUT_FILE.close()

# 2.
IN_FILE = open("name.txt", "r")
name = IN_FILE.read().strip()
IN_FILE.close()
print("Your name is", name)

# 3.
IN_FILE = open("numbers.txt", "r")
number1 = int(IN_FILE.readline())
number2 = int(IN_FILE.readline())
IN_FILE.close()
print(number1 + number2)

# 4.
IN_FILE = open("numbers.txt", "r")
total = 0
for i in IN_FILE:
    total = total + int(i)
IN_FILE.close()
print(total)
