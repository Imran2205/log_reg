import re
regex = r'[A-Za-z0-9._%+-]+@ulkasemi\.com$'
regex2 = r'[A-Za-z0-9._%+-]+@gfoundties\.com$'
#regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for
# for validating an Email


def check(email):
    # pass the regular expression
    # and the string in search() method
    if (re.match(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':
    # Enter the email
    email = "ankitrai326@ulkasemi.com"

    # calling run function
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)

dic = {'Name': 'Imran Kabir', 'Email': 'imran.kabir@ulkasemi.com', 'Age': 22, 'Gender': 'Male', 'University': 'MIST', 'Password': 'Imran@1996'}
print(dic.keys())
for key in dic.keys():
    dic[key] = [dic[key]]

import pandas as pd

dc = pd.DataFrame(dic)
dc.to_csv('info.csv', mode='a', index=False, header=False)

print(dc)