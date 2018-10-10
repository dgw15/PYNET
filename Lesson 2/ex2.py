 ip_list = ["192.168.1.1"]
print (ip_list)
ip_list.append ("192.168.2.2")
print (ip_list)
ip_list.extend (["192.168.3.3, 192.168.4.4"])
print (ip_list)
ip_list = ip_list + (["192.168.5.5"])
print (ip_list)

print (ip_list[0])
print (ip_list[-1])

ip_list.pop(0)
ip_list.pop(-1)
print (ip_list)

ip_list[0] = ("2.2.2.2")
print (ip_list)
