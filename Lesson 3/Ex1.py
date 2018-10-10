#f = open("c:/Users/wilso/Desktop/Python/Lesson 3/show_vlan.txt")
#show_ver = f.readlines()

from pprint import pprint

vlan_list  = []
with open("c:/Users/wilso/Desktop/Python/Lesson 3/show_vlan.txt") as a:
    show_vlan = a.read()

for line in show_vlan.splitlines():
    if 'VLAN' in line or '-----' in line or line.startswith('  '):
        continue
    fields = line.split()
    vlan_ID = fields[1]
    vlan_name = fields[2]
    vlan_list.append((vlan_ID, vlan_name))


pprint (vlan_list)




