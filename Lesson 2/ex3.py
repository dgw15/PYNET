#a = open("c:/Users/wilso/Desktop/Python/lesson 2/show_arp.txt")
#my_arp = a.readlines()
#print(my_arp)

with open("c:/Users/wilso/Desktop/Python/lesson 2/show_arp.txt") as a:
    my_arplist = a.readlines()
my_arplist = my_arplist[2:]

from pprint import pprint
pprint(my_arplist)

my_arplist.sort()

first_3 = my_arplist[:3]
pprint(first_3)
print (type(first_3))
first_3 = "\n".join(first_3)
pprint(first_3)
print (type(first_3))

with open("c:/Users/wilso/Desktop/Python/lesson 2/arp_wr.txt", "wt") as f:
    f.write(first_3)

