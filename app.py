from flask import Flask, render_template, request, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import base64
import getpass
import waitress

app = Flask(__name__)

def pad(text):
    padding_length = 16 - len(text) % 16
    padding = chr(padding_length) * padding_length
    return text + padding

def unpad(text):
    padding_length = ord(text[-1])
    return text[:-padding_length]

def encrypt(text, password):
    salt = get_random_bytes(16)
    key = scrypt(password.encode(), salt, 32, N=2**14, r=8, p=1)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(text).encode())
    return base64.b64encode(salt + cipher.iv + ciphertext).decode('utf-8')

def decrypt(encrypted_text, password):
    data = base64.b64decode(encrypted_text)
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]
    key = scrypt(password.encode(), salt, 32, N=2**14, r=8, p=1)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext).decode('utf-8'))
    return plaintext

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    mode = request.form.get('mode')
    text = request.form.get('text')
    password = request.form.get('password')

    print(f"Mode: {mode}")
    print(f"Text: {text}")
    print(f"Password: {password}")

    if mode == '1':
        result = encrypt(text, password)
        operation = "Texto Cifrado"
    elif mode == '2':
        result = decrypt(text, password)
        operation = "Texto Decifrado"
    else:
        return "Modo inválido."

    print(f"Result: {result}")
    print(f"Operation: {operation}")

    return render_template('result.html', result=result, operation=operation)


if __name__ == '__main__':
    print("Starting server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
