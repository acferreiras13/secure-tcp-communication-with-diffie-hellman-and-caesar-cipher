# secure-tcp-communication-with-diffie-hellman-and-caesar-cipher
Este projeto implementa uma comunicação segura entre um servidor e um cliente utilizando o protocolo TCP, utilizando técnicas de criptografia clássica e um algoritmo moderno de troca de chaves.

# Funcionalidades
Diffie-Hellman: O servidor e o cliente geram chaves privadas e públicas e trocam essas chaves para estabelecer uma chave secreta compartilhada. Essa chave é usada para criptografar e descriptografar as mensagens.

Cifra de César: As mensagens trocadas entre o servidor e o cliente são criptografadas usando a Cifra de César, onde o deslocamento é derivado da chave secreta compartilhada gerada pelo Diffie-Hellman.

# Arquivos
1. Simple_tcpServer.py
Este arquivo implementa o servidor que escuta em uma porta específica, realiza a troca de chaves Diffie-Hellman com o cliente e criptografa/descriptografa mensagens com a Cifra de César.

2. Simple_tcpClient.py
Este arquivo implementa o cliente que se conecta ao servidor, troca chaves Diffie-Hellman e envia uma mensagem criptografada, recebendo a resposta do servidor.

# Requisitos
Python 3.x instalado
Conexão de rede para a comunicação TCP (pode ser executado localmente ou em uma rede)

# Como usar

Servidor:
1. Execute o arquivo Simple_tcpServer.py.
2. O servidor começará a escutar na porta 1300.

Cliente:
1. Execute o arquivo Simple_tcpClient.py.
2. O cliente se conectará ao servidor e iniciará a troca de mensagens.

Interação:
1. O cliente irá digitar uma frase que será criptografada e enviada ao servidor.
2. O servidor receberá a mensagem, a descriptografará, converterá para maiúsculas e a recriptografará antes de enviar de volta ao cliente.
3. O cliente receberá a resposta, descriptografará a mensagem final e exibirá o resultado.
