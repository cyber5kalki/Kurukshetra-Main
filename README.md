# Kurukshetra: File Encryption and Decryption Tool

## Project Description
Kurukshetra is a user-friendly application designed to protect user password keys at rest (on the disk). It provides functionalities to encrypt and decrypt files using robust encryption algorithms. The application is built using CustomTkinter for the GUI and PyCryptodome for cryptographic operations.

## Features
- Encrypt files with a secure passphrase
- Decrypt files with the corresponding passphrase
- Validate passphrases to ensure they meet security criteria
- User-friendly GUI built with CustomTkinter
- Progress indicators and status updates for encryption/decryption processes

## Requirements
- Python 3.6 or higher
- Cryptography
- PyCryptodome
- CustomTkinter
- Pylance (optional for development)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/kurukshetra.git
    cd kurukshetra
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Application
1. Navigate to the project directory:
    ```sh
    cd kurukshetra
    ```

2. Run the main application:
    ```sh
    python home.py
    ```

### Encrypting a File
1. Open the application and select "Encryption/Decryption".
2. In the new window, choose the "Encryption" option.
3. Browse for the file you want to encrypt.
4. Enter a secure passphrase that meets the validation criteria.
5. Click "Encrypt" and wait for the process to complete.

### Decrypting a File
1. Open the application and select "Encryption/Decryption".
2. In the new window, choose the "Decryption" option.
3. Browse for the encrypted file and the corresponding FEK file.
4. Enter the passphrase used for encryption.
5. Click "Decrypt" and wait for the process to complete.

## File Structure
```plaintext
kurukshetra/
│
├── images/
│   ├── encryption.png
│   ├── decryption.png
│   └── kurukshetra.gif
│
├── encrypt.py
├── encrypt_gui.py
├── decrypt.py
├── decrypt_gui.py
├── encryption_decryption_app.py
├── home.py
├── utils.py
└── requirements.txt
