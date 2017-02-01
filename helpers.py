import sys
import socket
import threading

import Servidor_P
import p_handler


def hexdump(src, length=16):

    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src), length):

        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append( b"%04X %-*s %s" %(i, length*(digits + 1), hexa,text))

    print b'\n'.join(result)


def receive_from(connection):

    buffer = ""

    # Set 2 segundos de timeout; Dependendo do alvo, isso necessita ser ajustado
    connection.settimeout(2)

    try:

    #Continue lendo no buffer ate
    # Nao haver mais dados
    #ou o timeout
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data

    except:
        pass


# Modificar quaisquer pedidos destinados para o host remoto
def request_handler(buffer):

    # Executar modificacoes de pacote
    return


# Modificar quaisquer respostas destinadas ao host local
def response_handler(buffer):
    # Executar modificacoes de pacote
    return buffer
