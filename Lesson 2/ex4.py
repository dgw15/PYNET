with open ("c:/Users/wilso/Desktop/Python/lesson 2/sh_ip_arp.txt") as a:
    my_ip_arp = a.readlines()

from pprint import pprint
#pprint (my_ip_arp)

line_4 = my_ip_arp[5].strip()
fields = line_4.split()
my_int = fields[0]
my_add = fields[1]
both = (my_int, my_add)
pprint (both)
