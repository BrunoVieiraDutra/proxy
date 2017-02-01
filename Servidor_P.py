import sys
import socket
import threading

import p_handler
import helpers


def servidor_loop(host_local, porta_local,host_remoto ,porta_remota,primeiros_dados):

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        servidor.bind((host_local,porta_local))

    except:

        print "[!!] Falha em escutar em %s:%d" %(host_local,porta_local)
        print "[!!] Verifique se ha outros sockets em escuta ou as permissoes corretas."
        sys.exit(0)

    print "[*] Escutando em %s:%d" %(host_local, porta_local)

    servidor.listen(5)

    while True:

        cliente_socket, addr = servidor.accept()

        #Imprimir as informacoes de conexao local
        print "[==>] Conexao recebida  de %s:%d" %(addr[0],addr[1])

        #start a thread to talk to the remote host
        proxy_thread = threading.Thread(target = p_handler.proxy_handler, args=(cliente_socket,host_remoto,porta_remota,primeiros_dados))
        proxy_thread.start()

