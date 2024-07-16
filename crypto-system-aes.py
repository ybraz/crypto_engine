from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import base64
import sys
import getpass

def pad(text):
    # O tamanho do bloco AES é de 16 bytes
    padding_length = 16 - len(text) % 16
    # Cria o padding necessário
    padding = chr(padding_length) * padding_length
    return text + padding

def unpad(text):
    # Obtém o comprimento do padding do último caractere do texto
    padding_length = ord(text[-1])
    # Remove o padding do texto
    return text[:-padding_length]

def encrypt(text, password):
    # Gera um sal aleatório de 16 bytes
    salt = get_random_bytes(16)
    # Deriva uma chave a partir da senha e do sal usando scrypt
    key = scrypt(password.encode(), salt, 32, N=2**14, r=8, p=1)
    # Cria um novo objeto de cifra AES no modo CBC
    cipher = AES.new(key, AES.MODE_CBC)
    # Criptografa o texto com padding
    ciphertext = cipher.encrypt(pad(text).encode())
    # Retorna o texto cifrado codificado em base64, incluindo o sal e o IV
    return base64.b64encode(salt + cipher.iv + ciphertext).decode('utf-8')

def decrypt(encrypted_text, password):
    # Decodifica os dados codificados em base64
    data = base64.b64decode(encrypted_text)
    # Extrai o sal, IV e o texto cifrado
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]
    # Deriva a chave a partir da senha e do sal usando scrypt
    key = scrypt(password.encode(), salt, 32, N=2**14, r=8, p=1)
    # Cria um novo objeto de cifra AES no modo CBC com o IV extraído
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Descriptografa e remove o padding do texto
    plaintext = unpad(cipher.decrypt(ciphertext).decode('utf-8'))
    return plaintext

def main():
    if len(sys.argv) != 3:
        # Verifica se o número correto de argumentos foi fornecido
        print("Uso: python script.py <modo> <texto>")
        print("Modo: 1 para criptografar, 2 para descriptografar")
        print("Texto: texto a ser processado")
        return
    
    try:
        # Tenta converter o modo para um número inteiro
        mode = int(sys.argv[1])
        text = sys.argv[2]
    except ValueError:
        # Exibe uma mensagem de erro se a conversão falhar
        print("Erro: Modo deve ser um número inteiro")
        return

    # Solicita a senha de forma interativa
    password = getpass.getpass("Digite a senha: ")
    
    if mode == 1:
        # Chama a função de cr 
        # iptografia se o modo for 1
        result = encrypt(text, password)
        print(f"Texto cifrado: {result}")
    elif mode == 2:
        # Chama a função de descriptografia se o modo for 2
        result = decrypt(text, password)
        print(f"Texto decifrado: {result}")
    else:
        # Exibe uma mensagem de erro se o modo for inválido
        print("Modo inválido. Use 1 para criptografar e 2 para descriptografar.")
        print("Uso: python script.py <modo> <texto>")

if __name__ == "__main__":
    # Garante que a função main seja chamada apenas quando o script é executado diretamente
    main()
