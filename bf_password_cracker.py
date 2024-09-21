# Brute Force ZIP Password Cracker
# Author: Ryan Feneley
# Date: September 2024

import zipfile

def crack_zip(zip_file_path, dictionary_file_path):
    # Open the zip file
    with zipfile.ZipFile(zip_file_path) as z:

        with open(dictionary_file_path, 'r') as dict_file:
            for line in dict_file:
                password = line.strip()
                try:
                    # Attempt to extract using the current password
                    z.extractall(pwd=password.encode())
                    print(f'Success! The password is: {password}')
                    return
                except (RuntimeError, zipfile.BadZipFile):
                    # Wrong password, continue
                    continue
    print('Password not found in the dictionary.')