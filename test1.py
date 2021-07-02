import re
import pandas as pd
import os

info = {

}
files = os.listdir(os.getcwd())
print(files)
if 'info_test.csv' not in files:
    info['Name'] = []
    info['Email'] = []
    info['Age'] = []
    info['Gender'] = []
    info['University'] = []
    info['Password'] = []
    df = pd.DataFrame(info)
    df.to_csv('info_test.csv')

name = input("Enter your name:")

names = name.split()
print(names)
new_name = ''
for i, n in enumerate(names):
    name_up = ''
    char = ''
    for j, c in enumerate(n):
        if j == 0:
            if 'z' >= c >= 'a':
                char = chr(ord(c) - 32)
            else:
                char = c
    name_up = char + n[1:]
    new_name = new_name + name_up + ' '

print(new_name)


"""checker1 = r'[A-Za-z0-9._%+-]+@ulkasemi\.com$'
checker2 = r'[A-Za-z0-9._%+-]+@gfoundries\.com$'

if re.match(checker1, email) or re.match(checker2, email):
    print("valid email")
else:
    print("invalid email")"""

email_error = True
email = ''
while email_error:
    email = input("Enter your email")
    at_count = 0
    for c in email:
        if c == '@':
            at_count+=1

    if at_count==1:
        email_parts = email.split('@')
        if len(email_parts[0]) > 0:
            if email_parts[1] == 'ulkasemi.com' or email_parts[1] == 'globalfoundries.com':
                print("valid email")
                email_error = False
            else:
                print("invalid email")
                email_error = True
        else:
            print("invalid email")
            email_error = True
    else:
        print("invalid email")
        email_error = True



age = input("Enter your age")



gender = input("Enter your gender")

university = input("enter your university")
invalid_pass = True
password = ''
conf_pass = ''
while invalid_pass:
    password = input("enter password")

    conf_pass = input("confirm password")

    if password == conf_pass:
        if len(password) >= 8:
            capital_count = 0
            small_count = 0
            special_char_count = 0
            number_count = 0
            for c in password:
                invalid_pass = False
                if 'z' >= c >= 'a':
                    small_count+=1
                elif 'Z' >= c >= 'A':
                    capital_count+=1
                elif '9' >= c >= '0':
                    number_count+=1
                elif c in '~!@#$%^&*<>?':
                    special_char_count+=1
                else:
                    print('invalid password')
                    invalid_pass = True
                    break

            if not invalid_pass:
                if capital_count>0 and small_count>0 and special_char_count>0 and number_count>0:
                    print('valid password')
                    invalid_pass = False
                else:
                    print('invalid password')
                    invalid_pass = True

        else:
            invalid_pass = True
            print("must be at least 8 char long")
    else:
        invalid_pass = True
        print("password did not match")

user_info = {
    'Name': new_name,
    'Email': email,
    'Age': age,
    'University': university,
    'Gender': gender,
    'Password': password
}

for key in user_info.keys():
    user_info[key] = [user_info[key]]
df = pd.DataFrame(user_info)
df.to_csv('info_test.csv', mode='a', header=False)