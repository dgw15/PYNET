
from pprint import pprint

with open("c:/Users/wilso/Desktop/Python/Lesson 3/show-arp.txt") as f:
    show_arp = f.read()

found1, found2 = (False, False)
for line in show_arp.splitlines():
    if "protocol" in line.lower():
        continue


    fields = line.split()
    ip_add = fields[1]
    mac_add = fields[3]

    if ip_add == "10.220.88.1":
        print ("ip address is: {}/{}".format(ip_add, mac_add))
        found1 = True
    elif ip_add == "10.220.88.30":
        print ("Arista ip is: {}/{}".format(ip_add, mac_add))
        found2 = True

    if found1 and found2:
        pprint ("exiting....")
        break


#strip = show_arp[2].strip()
#split = strip.splitlines()

#zero = split[0]
#pprint (strip)




