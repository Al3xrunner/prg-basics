###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, "r") as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

# calculates the total number of cars parked
i= 0
total = 0

for line in file_lines:
   file_lines[i]=line.split()
   total += len(file_lines[i])
   i += 1

print(file_content)
print("")
print('Number of words in the text: ', total)