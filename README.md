# Ceasar and Vigenere
This is a semester project developed by students at the University "Hasan Prishtina" - Faculty of Electrical and Computer Engineering, in the course "Data Security" - Prof.Blerim Rexha and Asc.Mergim Hoti.

## Introduction
The Caesar cipher, named after Julius Caesar, is one of the simplest and most widely known encryption techniques. It works by shifting each letter of the plaintext by a fixed number of positions down or up the alphabet.

The Vigenère cipher, invented by Giovan Battista Bellaso and later misattributed to Blaise de Vigenère, is a more complex polyalphabetic substitution cipher. It uses a keyword to shift each letter of the plaintext by a different amount, making it more secure than the Caesar cipher.

This Python application provides a user-friendly interface for encrypting and decrypting text files using either the Caesar cipher or the Vigenère cipher.

### How it Works
1. The user selects the Vigenère or Caesar option.
2. They enter whether they want to encrypt or decrypt a file.
3. They provide the file to be encrypted/decrypted.
4. They select where do they want to save the encrypted/decrypted file.
5. They specify the encryption key.
6. The program performs the encryption/decryption and saves the result to a new file.

### Graphical User Interface (GUI)
The application uses tkinter for the GUI, allowing users to easily select options and input necessary information through dialog boxes.  

### Operation Dialogs
- Operation Selection: Users are prompted to enter whether they want to "encrypt" or "decrypt".
- File Selection: Users can browse and select the file to be processed.
- Save Location: Users can choose the directory to save the processed file.
- Key/Shift Input:
  - For Caesar cipher: Users are prompted to enter the shift value.
  - For Vigenère cipher: Users are prompted to enter the encryption key.     

### Functions
- caesar_encrypt: Encrypts text using the Caesar cipher.
- caesar_decrypt: Decrypts text using the Caesar cipher.
- vigenere_encrypt: Encrypts text using the Vigenère cipher.
- vigenere_decrypt: Decrypts text using the Vigenère cipher.
- select_operation: Handles user input for selecting the operation (encrypt/decrypt) and processing the file.
- main: Initializes the GUI and sets up the main application window.

### How to Use
- **Clone this repository to your local machine.**
  ```bash
   git clone https://github.com/elonekrasniqi/CaesarAndVigenere.git
- Make sure you have Python installed.
- Install the required dependencies by running `pip install -r requirements.txt.`
- Run the main.py file.

### Contributors:
- [Elma Shabani](https://github.com/ElmaShabani)
- [Elona Fetahu](https://github.com/ElonaFetahu)
- [Elonë Krasniqi](https://github.com/elonekrasniqi)
- [Elton Pajaziti](https://github.com/EltonPajaziti)

### Technical Documentation
For detailed explanations of the algorithms, refer to the following videos:
- [Caesar Algorithm](https://www.youtube.com/watch?v=JtbKh_12ctg)
- [Vigenère Algorithm](https://www.youtube.com/watch?v=_P7wg7otgfE)

### Security Considerations
It's important to note that while the Vigenère cipher offers more security than the Caesar cipher, both are considered weak by modern standards. They are educational examples and should not be used for sensitive data without additional measures.
