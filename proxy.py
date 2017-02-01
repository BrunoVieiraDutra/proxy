import sys
import socket
import threading

import Servidor_P
import p_handler
import helpers

def main():

    if len(sys.argv[1:]) != 5:
        print "Modo de Uso: ./proxy.py [localhost] [portaLocal] [hostRemoto] [portaRemota] [primeiros_dados]"
        print "Exemplo: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
        sys.exit(0)

    #   Configuracao de parametros de escuta locais

    host_local = sys.argv[1]
    porta_local = int(sys.argv[2])

    #   Configurando alvo remoto
    host_remoto = sys.argv[3]
    porta_remota = int(sys.argv[4])

    #   Isso indica ao nosso proxy para se conectar e receber dados
    #   Antes de enviar para o host remoto

    primeiros_dados = sys.argv[5]

    if "True" in primeiros_dados:
        primeiros_dados = True
    else:
        primeiros_dados = False

    Servidor_P.servidor_loop(host_local, porta_local, host_remoto , porta_remota , primeiros_dados)

main()