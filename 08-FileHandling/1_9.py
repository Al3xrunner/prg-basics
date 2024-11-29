###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, "r") as file:
   content = file.read()
   file_lines = content.splitlines()
   i= 1
   for line in file_lines:
      if job_title in str(line):
         print(f"{i}. ", end = "")
         print(line)
         i +=1