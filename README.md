# Brute Force ZIP Password Cracker
## Overview
This project is a Python-based brute-force password cracker for password-protected ZIP files. It attempts to unlock a ZIP file by trying a list of potential passwords, often referred to as a dictionary attack.

## Features
- Reads a password-protected ZIP file and a list of potential passwords from a dictionary file.
- Attempts to brute force the ZIP file by trying every password in the list.
- Reports the correct password upon success.
- Logs failed attempts.

## Requirements
- Python 3.x
- \zipfile\ module (part of Python's standard library)

## Usage
1. Clone the repository or download the code.
2. Prepare a dictionary file (\passwords.txt\) containing one password per line.
3. Run the script with the ZIP file and dictionary file as arguments:
   \\\ash
   python brute_force_zip.py <zipfile> <dictionary>
   \\\
   Example:
   \\\ash
   python brute_force_zip.py secret.zip passwords.txt
   \\\

## How it Works
- The script opens the ZIP file and iterates through the passwords listed in the dictionary file.
- Each password is tried in sequence until the correct password is found.
- If the correct password is found, it is displayed to the user and the ZIP file is unlocked.
