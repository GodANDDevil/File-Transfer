File-Transfer is a Python-based socket programming project designed to demonstrate secure file transfer using RSA encryption.
This project is part of a cybersecurity learning initiative, showing how cryptography can be applied to protect data during transmission across networks

Features

- Socket Programming: Implements client-server communication for file transfer.
- RSA Encryption: Ensures confidentiality of files during transfer.
- Cross-Platform: Works on any system with Python installed.
- Educational Focus: Built for learning cybersecurity concepts like encryption, secure communication, and network programming.

Tech 

Language:Python 3

Networking:Socket Library

Cryptography:RSA Algorithm

Getting Started

Prerequisites

- Python 3.8+
- Basic knowledge of socket programming and RSA encryption.

- Clone the repository

git clone https://github.com/GodANDDevil/File-Transfer.git

cd File-Transfer

Run the server

-python server.py

Run the client

-python client.py(Frist time to sent the File to server to encrypect the again run client to receive the file after decrypect)


🔒 Security Context
This project demonstrates:
- Confidentiality: Files are encrypted before transmission.
- Integrity: RSA ensures files cannot be tampered with easily.
- Authentication: Public/private key pairs validate sender and receiver.
⚠️ Note: This is a learning project. For production use, additional safeguards (TLS, stronger key management, error handling, etc.) are required.

📂 Project Structure
File-Transfer/
│── client.py       # Client-side script
│── server.py       # Server-side script
│── rsa_utils.py    # RSA encryption/decryption logic


💡 Future Improvements
- Add AES hybrid encryption (RSA for key exchange, AES for file encryption).
- Implement user authentication.
- Add logging and monitoring for intrusion detection.
- Deploy on a secure server for real-world testing.

