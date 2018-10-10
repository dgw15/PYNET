# exercise 2
ip_addr1  = input ("input ip address")
oct1 = "Octet1"
oct2 = "Octet2"
oct3 = "Octet3"
oct4 = "Octet4"

octets = ip_addr1.split(".")

print ("\n")
print ("{:^15}{:^15}{:^15}{:^15}".format (oct1, oct2, oct3, oct4))
print ("-"*60)
print ("\n")
print ("{:^15}{:^15}{:^15}{:^15}".format (*octets))
print ("{:^15}{:^15}{:^15}{:^15}".format (bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print ("{:^15}{:^15}{:^15}{:^15}".format (hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print ("-"*60)
