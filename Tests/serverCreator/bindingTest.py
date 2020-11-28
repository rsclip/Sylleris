import socket

ip, port = '192.168.0.18', 25565


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print('Binding..')
    s.bind((ip, port))
    print('Binded.')
    s.close()
    print('Successful.')
except OverflowError:
    print('Port is invalid')
except OSError as e:
    print(str(e))
