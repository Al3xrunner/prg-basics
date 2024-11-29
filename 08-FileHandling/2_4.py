

employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

with open(employees_file, "r") as file:
   with open(position_file, "w") as new_file:
    content = file.read()
    file_lines = content.splitlines()
    i= 1
    for line in file_lines:
        if job_title in str(line):
            new_file.write(f"{i}. {line}\n")
            i +=1