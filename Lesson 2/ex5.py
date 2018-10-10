with open ("c:/Users/wilso/Desktop/Python/lesson 2/sh_ip_bgp.txt") as a:
    my_bgp = a.readlines()

from pprint import pprint

#pprint (my_bgp)

first_last1 = my_bgp[0].split()
first_last2 = my_bgp[3].split()

pprint (first_last1[7])
pprint (first_last2[2])


