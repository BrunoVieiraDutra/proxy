import sys
import socket
import threading

import Servidor_P
import helpers

def proxy_handler(client_socket, host_remoto, porta_remota, primeiros_dados):
    #   Conectar-se ao host remoto
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((host_remoto, porta_remota))

    #   Receber dados da extremidade remota se necessario
    if primeiros_dados:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        #  Envie para o nosso manipulador de resposta
        remote_buffer = response_handler(remote_buffer)

        # Se tivermos dados para enviar para o nosso cliente local, os envie
        if len(remote_buffer):
            print "[<==] Enviando %d bytes para localhost." % len(remote_buffer)
            cliente_socket.send(remote_buffer)

    # Iniciamos o loop e ler dados do hostlocal
    # envie para o remoto, envie para o local
    #  Repetir o procedimento

    while True:

        # Ler do localhost
        local_buffer = receive_from(cliente_socket)

        if len(local_buffer):
            print "[==>] recebidos %d bytes do localhost." % len(local_buffer)
            hexdump(local_buffer)

            # Envie para o nosso processador de pedidos
            local_buffer = request_handler(local_buffer)

            # Enviar os dados para o host remoto
            remote_socket.send(local_buffer)
            print "[==>] Enviar para o hostremote."

        # Receber de volta a resposta
        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print "[<==] Recebidos %d bytes do remote." % len(remote_buffer)
            hexdump(remote_buffer)

            # Envie para o nosso manipulador de resposta
            remote_buffer = response_handler(remote_buffer)

            # Enviar a resposta para o socke local

            client_socket.send(remote_buffer)
            print "[<==] Enviado para o localhost."

        # Se nao houver dados em nenhum dos lados , feche a comunicacao
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print "[*] nenhum Dado encontrado. Fechando Conexoes."
            break
