from socket import *

# Implementação de um gerador de números pseudoaleatórios (LCG)
def lcg_random(seed, a=1664525, c=1013904223, m=2**32):
    return (a * seed + c) % m

# Configuração Diffie-Hellman
P = 23  # Número primo público
G = 5   # Base pública
seed = 12345  # Semente inicial
private_key = (lcg_random(seed) % (P - 1)) + 1  # Chave privada do servidor
public_key = (G ** private_key) % P  # Chave pública do servidor

# Alfabeto expandido para incluir caracteres acentuados
ALFABETO = "abcdefghijklmnopqrstuvwxyzáàâãéèêíïóôõöúùüçABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÙÜÇ"

# Função para criptografar a mensagem com a Cifra de César
def caesar_cipher_encrypt(text, shift):
    resultado = ""
    for char in text:
        if char in ALFABETO:
            idx = ALFABETO.index(char)
            new_idx = (idx + shift) % len(ALFABETO)
            resultado += ALFABETO[new_idx]
        else:
            resultado += char  # Mantém caracteres especiais
    return resultado

# Função para descriptografar a mensagem com a Cifra de César
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Configuração do servidor
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("🔹 TCP Server Iniciado...\n")

connectionSocket, addr = serverSocket.accept()

# Troca de chaves Diffie-Hellman
client_public_key = int(connectionSocket.recv(1024).decode("utf-8"))
connectionSocket.send(str(public_key).encode("utf-8"))

# Cálculo da chave secreta compartilhada
shared_key = (client_public_key ** private_key) % P
shift = shared_key % len(ALFABETO)  # Ajusta para o tamanho do alfabeto expandido

print(f"🔹 Chave compartilhada gerada: {shared_key} (Usada como deslocamento {shift})\n")

# Recebendo a mensagem do cliente
sentence = connectionSocket.recv(65000).decode("utf-8")

# Exibindo mensagens recebidas
print(f"🔹 Mensagem criptografada recebida do cliente: {sentence}")
decrypted_sentence = caesar_cipher_decrypt(sentence, shift)
print(f"🔹 Mensagem descriptografada do cliente: {decrypted_sentence}")

# Convertendo para maiúsculas sem perder acentos e recriptografando
capitalized_sentence = decrypted_sentence.upper()
encrypted_sentence = caesar_cipher_encrypt(capitalized_sentence, shift)

# Exibindo mensagem antes de enviar ao cliente
print(f"🔹 Mensagem transformada em maiúsculas: {capitalized_sentence}")
print(f"🔹 Mensagem criptografada enviada ao cliente: {encrypted_sentence}")

# Enviando resposta ao cliente
connectionSocket.send(encrypted_sentence.encode("utf-8"))

# Fechando conexão
connectionSocket.close()
