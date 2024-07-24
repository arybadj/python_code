import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# this socket library use to communicate with each other
# dgram is used to------build a connectionless communication system 

ip_add="192.168.1.4"
port=9999              # 0 to 65536

pura_add=(ip_add,port)  # connect both ip adddress and port

message= input("kya krega re baba😊")

#encoding the message to binary
encript_msg=message.encode('ascii')
s.sendto(encript_msg,pura_add)


