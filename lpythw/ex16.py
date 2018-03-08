from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want this, hit COMMAND + C(^C).")
print("If you do want this, press RETURN.")

input("?")

print("Opening the file....")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print(f"I'm going to write these into the file {filename}.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally, we'll close it")

target.close()
