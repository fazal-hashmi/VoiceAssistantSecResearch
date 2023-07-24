import scapy.all as scapy
import time


def FindVendor(mac):
    new_mac = mac[0:8] # we are select first three pairs
    oui = new_mac.replace(':', '') #we are simply removing simicolon
    f = open('ouis.txt', 'r').read() #read a text file containg list of ouis
    math = eval(f)

    try:
        print(math[oui.upper()]) #if found oui against mac address
    except:
        print('Unknow') #else

def FindMac(Iprange):
    request = scapy.ARP()  # Creating an ARP packet

    request.pdst = Iprange  # pdst is where the ARP packet should go
    broadcast = scapy.Ether()  # Creating an Ethernet packet

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'  # broadcasting this packet for all mac address

    request_broadcast = broadcast / request  # Combing ARP request packet and Ethernet
    start_time = time.time() # start to calculate the time
    clients = scapy.srp(request_broadcast, timeout=5)[0]
    print("IP address" + "         " + "MAC address")
    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)  # hwsrc is sender hardware address
        mac = element[1].hwsrc
        FindVendor(mac) #calling other fuction to find uoi against mac address
    print("\nTotal duration of the scan: %s seconds" % (time.time() - start_time)) # printing total douration of the scan

def main():
    Iprange = str(input("'Please enter the IP Range e.g 192.168.1.1/24: ")) #Taking IP range from the user
    FindMac(Iprange) #calling the function and passing IpRange as an argument


main()


