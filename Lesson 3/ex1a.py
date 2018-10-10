from __future__ import unicode_literals, print_function
from pprint import pprint

vlan_list = []
with open("c:/Users/wilso/Desktop/Python/Lesson 3/show_vlan.txt") as f:
    show_vlan = f.read()

for line in show_vlan.splitlines():
    # Skip certain lines
    if 'VLAN' in line or '-----' in line or line.startswith('  '):
        continue

    fields = line.split()
    vlan_id = fields
    vlan_name = fields
    vlan_list.append((vlan_id))

print()
pprint (vlan_list)
pprint (vlan_list.count)
print()




