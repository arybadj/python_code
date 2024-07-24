import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.1.4"
port=9999                            # 0 to 65536

pura_add=(ip_add,port)  # connect both ip adddress and port


s.bind(pura_add)

while True:
    message=s.recvfrom(150)
    print(message)
    data_msg=message[0]
    find_msg=decode("ascii")
    print(find_msg)

