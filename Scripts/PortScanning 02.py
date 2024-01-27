import socket
import os

def ScanPort(HostIP,StartPort,EndPort):
    for i in range(StartPort, EndPort + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        if s.connect_ex((HostIP, StartPort + 1)):
           print('port', StartPort, 'is closed or filtered')
           Port_N0 = str(StartPort)
        else:
           print('port', StartPort, 'is open')
           try:
               service = socket.getservbyport(StartPort, "Tcp")
               print(service)
               Port_N0 = str(StartPort)
           except:
               print('Unknow service')
               Port_N0 = str(StartPort)

        StartPort = StartPort + 1

def main():
    HostIP = input('Enter the Host IP you want to scan: ')
    StartPort = int(input('enter starting port: '))
    EndPort = int(input("enter ending port: "))
    ScanPort(HostIP,StartPort,EndPort)

main()
