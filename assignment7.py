import re

text = """
My emails are nikhil@gmail.com, pvtt123@yahoo.com,
student_01@mit.edu.in and test.email@outlook.com.
"""

# Regular expression for email
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)