# Password Generator

This is a simple password generator program written in Python. It allows users to create a secure password with a custom combination of letters, numbers, and symbols. The program was created by **Sahul Hameed**.

## Features

- Generates a random password based on user input.
- Users can specify how many letters, numbers, and symbols they want in their password.
- The password includes a mix of uppercase and lowercase letters, digits, and common special characters.
- The generated password is shuffled for added randomness and security.

## How It Works

1. The program asks the user for:
   - The number of **letters** to include in the password.
   - The number of **numbers** to include in the password.
   - The number of **symbols** to include in the password.
   
2. It then randomly selects characters from the specified categories (letters, numbers, symbols), adds them to a list, shuffles the list, and combines the characters into a secure password.

3. Finally, the program prints the randomly generated password for the user.

## How to Use

1. Install Python on your computer if you don't have it already: [Python Installation Guide](https://www.python.org/downloads/)
2. Download or copy the Python script (`password_generator.py`) to your local machine.
3. Run the script by opening your terminal or command prompt and typing:

   ```bash
   python password_generator.py
