from pprint import pprint
with open("c:/Users/wilso/Desktop/Python/Lesson 3/show_lldp.txt") as f:
    show_lldp = f.read()

found1, found2 == (False, False)
for line in show_lldp.splitlines():
    continue

    fields = line.split()
    port = fields[1]
    name = fields[1]

if port == "Port id":
    pprint (port)
    found1 = True

elif name == "System Name":
    pprint (name)
    found2 = True

if found1 and found2:
    break



pprint (show_lldp)


