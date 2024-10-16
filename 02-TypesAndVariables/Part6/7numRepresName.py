###
# A program that prints a numerical representation of each letter of your name.
#
name = input("Input your name: ")
name_length = len(name)
i = 0
while i < name_length:
    print(f'The letter {name[i]} has a code {ord(name[i])}')
    i += 1

