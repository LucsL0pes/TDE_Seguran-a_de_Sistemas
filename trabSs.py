from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util import Counter
import binascii
import os

def hex_para_bytes(texto_hex):
    return binascii.unhexlify(texto_hex)

def bytes_para_hex(bytes_data):
    return bytes_data.hex()

def hex_para_decimal(hex_str):
    return int(hex_str, 16)

# Função para descriptografar dados no modo CBC
def descriptografar_em_cbc(chave_hex, texto_cifrado_hex):
    chave = binascii.unhexlify(chave_hex)
    texto_cifrado = binascii.unhexlify(texto_cifrado_hex)
    iv = texto_cifrado[:16]
    cifra = AES.new(chave, AES.MODE_CBC, iv)
    dados_descriptografados = unpad(cifra.decrypt(texto_cifrado[16:]), AES.block_size)
    return dados_descriptografados.decode('utf-8', errors='ignore')  # Ignorar erros de conversão

# Função para descriptografar dados no modo CTR
def descriptografar_em_ctr(chave_hex, texto_cifrado_hex):
    chave = binascii.unhexlify(chave_hex)
    texto_cifrado = binascii.unhexlify(texto_cifrado_hex)
    contador = Counter.new(128, initial_value=int.from_bytes(texto_cifrado[:16], byteorder='big'))
    cifra = AES.new(chave, AES.MODE_CTR, counter=contador)
    dados_descriptografados = cifra.decrypt(texto_cifrado[16:])
    
    # Tentando retornar como bytes para evitar problemas de codificação inválida
    try:
        return dados_descriptografados.decode('utf-8')
    except UnicodeDecodeError:
        return dados_descriptografados  # Retorna como bytes, sem tentar interpretar como texto

# Função para criptografar uma mensagem com AES no modo CTR
def criptografar_em_ctr(chave_hex, texto_claro):
    chave = binascii.unhexlify(chave_hex)
    nonce = os.urandom(16)  # Gerar nonce aleatório
    contador = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))
    cifra = AES.new(chave, AES.MODE_CTR, counter=contador)
    texto_criptografado = cifra.encrypt(texto_claro.encode('utf-8'))
    
    # Retorna o texto cifrado em hexadecimal
    return binascii.hexlify(nonce + texto_criptografado).decode('utf-8')


# Tarefa 1 - Modo CBC
chave_cbc = "d50a3bb2c2811dd860ed0b344867b406"
texto_cifrado_cbc = "38f726acdccedb7953e4fc4e16f3035a3dd2581511cfaa3a7f0b12df725784cc2fc367ca81193c1898454431713c3422371e82e3cb64d95bc4263c08062662e3"
texto_decifrado_tarefa_1 = descriptografar_em_cbc(chave_cbc, texto_cifrado_cbc)
print(f"Texto decifrado da Tarefa 1: {texto_decifrado_tarefa_1}")

# Tarefa 2 - Modo CBC
texto_cifrado_cbc_tarefa_2 = "203c6bac6f9cf76ebecde621eb7615f9a7773dbfb6e20d75d78d2b7683d25597712190f6f6faf662dcd75b841566a134608ae5b0520d295c05142b42a9f887bd3edddacacf4f3e3b0c4b7849695d46d9"
texto_decifrado_tarefa_2 = descriptografar_em_cbc(chave_cbc, texto_cifrado_cbc_tarefa_2)
print(f"Texto decifrado da Tarefa 2: {texto_decifrado_tarefa_2}")

# Tarefa 3 - Modo CTR
chave_ctr = "1fbf6bebb2f7f365b00a4bdad4d0a4ac"
texto_cifrado_ctr_tarefa_3 = "4db4a169a55cf550ada23592edae27885f8b26d6ebba3a3f8bf6977cc5a25982bbb72d6e0183676b138a9ecf891c444587e77ae07b2f638ecf2ee5c6cd"
texto_decifrado_tarefa_3 = descriptografar_em_ctr(chave_ctr, texto_cifrado_ctr_tarefa_3)
print(f"Texto decifrado da Tarefa 3: {texto_decifrado_tarefa_3}")

# Tarefa 4 - Modo CTR
texto_cifrado_ctr_tarefa_4 = "267b0a4cea65edd43a43ca29990ac0da7659f392fcf5de0e4e32d065de9de5afad8bca61e0369cf8da7276507859a4ce8ba8fadbce5e5d1eb55c0f5875e752c723dd685a3b0d"
texto_decifrado_tarefa_4 = descriptografar_em_ctr(chave_ctr, texto_cifrado_ctr_tarefa_4)
print(f"Texto decifrado da Tarefa 4: {texto_decifrado_tarefa_4}")


# Criptografando o nome "Lucas Figueira Lopes" usando a mesma chave e modo da Tarefa 3
texto_claro = "Lucas Figueira Lopes"
nome_criptografado = criptografar_em_ctr(chave_ctr, texto_claro)
print(f"Nome criptografado: {nome_criptografado}")
texto_decifrado_tarefa = descriptografar_em_ctr(chave_ctr, nome_criptografado)
print(f"Nome Decifrado: {texto_decifrado_tarefa}")
