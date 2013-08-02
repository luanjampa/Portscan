import socket,sys

ip = input("Ip:")
escolha = input("Informe a opção \n 1 - RANGE \n 2 - Porta especificas  :")
if escolha == '1':
    try:
        inicial = input("Informe a porta inicial:")
        final = input("Informe a porta final:")
        final = int(final)
        inicial = int(inicial)
        for port in range(inicial,final):
            socket.setdefaulttimeout(2)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ip, port))
            if (result == 0):
                print("Porta:",(port),"Status: OPEN")
            else:
                print("Porta:",(port),"Status: CLOSED")
            s.close()

 
    except socket.error:
        print ("Não foi possivel conectar")
        sys.exit()
        
elif escolha == '2':
    try:
        port = input("Informe a porta: ")
        port = int(port)
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if (result == 0):
                     print("Porta:",(port),"Status: OPEN")
        else:
                     print("Porta:",(port),"Status: CLOSED")
                     s.close()

 
    except socket.error:
        print ("Não foi possivel conectar")
        sys.exit()
    



