from socket import *
from this import d

if __name__ == '__main__':
    target = input('Enter IP of target: ')
    t_IP = gethostbyname(target)
    print('Scanning: ', t_IP)

    for i in range(1, 60):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: Otwarty' % (i,))
            service = s.recv(1024).decode()
            print(service)
        s.close()
print("ukończono")