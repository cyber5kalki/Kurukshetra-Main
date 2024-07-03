# Kurukshetra: File Encryption and Decryption Using AES-256 Algorithm

## Project Description
In the epic Mahabharata, Kurukshetra symbolizes a monumental battle, drawing a parallel to the critical importance of securing files and data with utmost confidentiality. Any compromise in file confidentiality can lead to potential data breaches, emphasizing the crucial role of protecting, encrypting, and decrypting data as a vital defense strategy. This analogy inspires the project's title, Kurukshetra.

![Kurukshetra](/Internship-Main/images/kurukshetra.gif)

## Features
- Encrypt files with a secure passphrase
- Decrypt files with the corresponding passphrase
- Validate passphrases to ensure they meet security criteria
- User-friendly GUI built with CustomTkinter
- Progress indicators and status updates for encryption/decryption processes

## Requirements
- Cryptography
- PyCryptodome
- utils
- CustomTkinter

## Usage
1. **Launch the Application**:
   Run `home.py` to start the application. The welcome screen will guide you through the next steps.

2. **Encrypt a File**:
    - Click on the "Encrypt" button.
    - Select the file you want to encrypt.
    - Enter a passphrase and save the .fek file and then save in the disk.
    - Click "Encrypt" to secure your file.

3. **Decrypt a File**:
    - Click on the "Decrypt" button.
    - Select the encrypted and key as .fek file.
    - Enter the passphrase used during encryption.
    - Click "Decrypt" to access your file.

4. **Work Flow**
![Flowchat](src/Flowchat.jpeg)

5. **Encrypt(Work Flow)**
![Encrypt](src/Encrypt.jpeg)

6. **Decrypt(Work Flow)**
![Decrypt](src/Decrypt.jpeg)

7. **Demo video**
![Watch the video](https://drive.google.com/file/d/1PQQepLfM7AC0A-OVkK75TcMMQ2jjSzTy/view)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/cyber5kalki/Kurukshetra-Main.git
    cd kurukshetra
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:


### Running the Application
1. Navigate to the project directory:
    ```sh
    cd kurukshetra
    ```

2. Run the main application:
    ```sh
    python - u home.py
    ```

### Encrypting a File
1. Open the home.py application and select "Encryption/Decryption".
2. In the new window, choose the "Encryption" option.
3. Browse for the file you want to encrypt.
4. Enter a strong passphrase that meets the validation criteria, and save it as a file and an FEK file for security.
5. Click "Encrypt" and wait for the process to complete.

### Decrypting a File
1. Open the application and select "Encryption/Decryption".
2. In the new window, choose the "Decryption" option.
3. Browse for the encrypted file and the corresponding FEK file.
4. Enter the passphrase used for encryption.
5. Click "Decrypt" and wait for the process to complete.

## File Structure
```plaintext
kurukshetra-Main
├── src
├── README.md
├── Internship-Main
│   ├── assests
│   ├── images
│   ├── home.py
│   ├── encryption_decryption_app.py
│   ├── encrypt.py
│   ├── decrypt.py
│   ├── utils.py
│   ├── encrypt_gui.py
│   ├── decrypt_gui.py
│   ├── requirements.txt

