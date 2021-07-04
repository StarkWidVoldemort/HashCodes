This repository contains 2 python programs:
  1. :hash: [Hash  Generator](#the-hash-genrator-computer)
  2. :mag_right: [Advance Hashing](#advance-hashing)

# The Hash Genrator :computer:
   
   ## Dependencies:
   The library used in this program is [hashlib](https://docs.python.org/3/library/hashlib.html)
   
   ## Overview:   
  This is a simple python program which takes a string from the user that is to be hashed and then hash the entered string using various algorithms 
  including : [MD5](https://en.wikipedia.org/wiki/MD5), [SHA512](https://en.wikipedia.org/wiki/SHA-2), [SHA256](https://en.wikipedia.org/wiki/SHA-2) and [blake2b method of hashlib](https://www.geeksforgeeks.org/hashlib-blake2b-in-python/#:~:text=With%20the%20help%20of%20hashlib,with%20the%20help%20of%20hashlib.)
  
  Further, this program contains 2 sub-programs called Program 1 and Program 2


   ### Program 1
   In this program the string already entered by the user is converted into a hash code using [MD5](https://en.wikipedia.org/wiki/MD5) algorithm. It then executes the generated [MD5](https://en.wikipedia.org/wiki/MD5) hash code of the entered string.
   Simple !!

   ### Program 2
   The program uses the already entered string by the user to hash it to three different algorithms namely [SHA512](https://en.wikipedia.org/wiki/SHA-2), [SHA256](https://en.wikipedia.org/wiki/SHA-2) and [blake2b method of hashlib](https://www.geeksforgeeks.org/hashlib-blake2b-in-python/#:~:text=With%20the%20help%20of%20hashlib,with%20the%20help%20of%20hashlib.).
   To execute the results of generated codes, it uses a function named ``generate_hash()``. 

   ## Note:
   Although the string is hashed using different types of algorithms present on hashlib, still these hash codes can be hacked using a [Brute Force Attack](https://www.varonis.com/blog/brute-force-attack/) 
   or [Dictionary Attack](https://searchsecurity.techtarget.com/definition/dictionary-attack). To prevent this from happening, we have to do some more things which are covered in [Advance Hashing](#advance-hashing)



# Advance Hashing :closed_lock_with_key:

   ## Dependencies:
   The libraries used in this program are [hashlib](https://docs.python.org/3/library/hashlib.html) and [os](https://docs.python.org/3/library/os.html)
   
   ## Overview:
   Program asks the user to input any username and a password of their choice. It then takes the password entered by the user and generates a key using ``.pbkdf2_hmac() method``.
   Salt is generated via `.urandom()` method using `os` library. In the hashing process, salt is added to the string. String is hashed  using [SHA256](https://en.wikipedia.org/wiki/SHA-2)
   algorithm. After successfully hashing, salt and the key is stored in a dictionary to verify the password entered by the user. User is asked to enter the password that he provided 
   earlier. The salt and key of the previous password were obtained from the dictionary used for storing the values. A new key is generated using the same `.pbkdf2_hmac()` method with 
   similar arguments. Now both the keys are compared with each other. If the old key matches the new one, then the password is correct. If not the password is incorrect.
   
   ## Note:
   The string is now more secured as we did salting and iteration to it other than hashing. 
