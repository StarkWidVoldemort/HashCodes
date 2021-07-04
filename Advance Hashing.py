import hashlib
import os


users = {}

# Inputs from the user
username = input('Enter any username: ')
password = input('Enter the password of your choice: ')

print('Loading...')

# Hashing
salt = os.urandom(36)  # Generated a salt
key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        1000000,
        dklen=128)

# Storing the values
users[username] = {
    'salt': salt,
    'key': key
}

# Verifying
password_to_check = input('Enter the password again to verify: ')
print('Loading...')
salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'),
    salt,
    1000000,
    dklen=128
)

if key == new_key:
    print('PASSWORD MATCHED. VERIFIED!!')
else:
    print('PASSWORD INCORRECT. NOT VERIFIED!!')
