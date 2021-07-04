import hashlib


str_ = input('Enter the string to be hashed: ')

# --------------------------------------------------
# Program 1: Generating MD5 hash of the given string
# --------------------------------------------------
hashcode = hashlib.md5(str_.encode('utf-8')).hexdigest()
print('X----------PROGRAM 1: GENERATING AN MD5 HASH----------X')
print()
print('MD5 hash of entered string: ' + hashcode)
print()
print('X-------------------END OF PROGRAM 1-------------------X')
print()
print()
print()
print()


# ----------------------------------------------
# Program 2: Generating hashes from 3 algorithms
# ----------------------------------------------
print('X----PROGRAM 2: GENERATING HASHES FROM 3 ALGORITHMS-----X')
print()
# Creating hashes:
hashed1 = hashlib.sha512(str_.encode('utf-8')).hexdigest()
hashed2 = hashlib.sha256(str_.encode('utf-8')).hexdigest()
str_ = hashlib.blake2b().hexdigest()


def generate_hash(argument):
    switcher = {
        0: 'SHA512 hash of entered string: ' + hashed1,
        1: 'SHA256 hash of entered string: ' + hashed2,
        2: 'blake2b hash of entered string: ' + str_
    }

    return switcher.get(argument, 'nothing')


for i in range(3):
    print(generate_hash(i))

print()
print('X-------------------END OF PROGRAM 2-------------------X')
