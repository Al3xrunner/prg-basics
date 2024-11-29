###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'
def read_from_file(name):
   with open(name, "r") as file:
      content = file.read()
   return content
# read the content of email
email = read_from_file(email_file)

# regular expression pattern
# for amounts
pattern = '....'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
...
for amount in amounts:
   ...

# print result
print(...)