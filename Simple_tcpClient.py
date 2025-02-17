from socket import *

# Configuração Diffie-Hellman
P = 23  # Número primo público
G = 5   # Base pública

# Gerador de números pseudoaleatórios (LCG)
def lcg(seed, a=1664525, c=1013904223, m=2**32):
    return (a * seed + c) % m

seed = 24  # Escolha uma semente fixa para reprodutibilidade
private_key = (lcg(seed) % (P - 1)) + 1  # Garante um valor entre 1 e P-1
public_key = (G ** private_key) % P  # Chave pública do cliente

# Alfabeto expandido para incluir caracteres acentuados
ALFABETO = "abcdefghijklmnopqrstuvwxyzáàâãéèêíïóôõöúùüçABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÙÜÇ"

# Função para criptografar a mensagem com a Cifra de César
def caesar_cipher_encrypt(text, shift):
    return "".join(ALFABETO[(ALFABETO.index(c) + shift) % len(ALFABETO)] if c in ALFABETO else c for c in text)

# Função para descriptografar a mensagem com a Cifra de César
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Conexão com o servidor
serverName = "10.1.67.38"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Troca de chaves Diffie-Hellman
clientSocket.send(str(public_key).encode("utf-8"))
server_public_key = int(clientSocket.recv(1024).decode("utf-8"))

# Cálculo da chave secreta compartilhada
shared_key = (server_public_key ** private_key) % P
shift = shared_key % len(ALFABETO)  # Ajusta para o tamanho do alfabeto expandido

print(f"🔹 Chave compartilhada gerada: {shared_key} (Usada como deslocamento {shift})\n")

# Leitura da entrada do usuário e criptografia
sentence = input("🔹 Digite uma frase: ")
encrypted_sentence = caesar_cipher_encrypt(sentence, shift)

# Exibindo mensagem criptografada antes de enviar ao servidor
print(f"🔹 Mensagem original digitada: {sentence}")
print(f"🔹 Mensagem criptografada enviada ao servidor: {encrypted_sentence}")

# Enviando mensagem criptografada ao servidor
clientSocket.send(encrypted_sentence.encode("utf-8"))

# Recebendo resposta do servidor
modifiedSentence = clientSocket.recv(65000).decode("utf-8")
decrypted_sentence = caesar_cipher_decrypt(modifiedSentence, shift)

# Exibição da resposta recebida
print(f"🔹 Mensagem criptografada recebida do servidor: {modifiedSentence}")
print(f"🔹 Mensagem descriptografada final: {decrypted_sentence}")

# Fechando conexão
clientSocket.close()
