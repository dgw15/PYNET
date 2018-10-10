# exercise 5

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

fields1 = mac1.split()
ip1 = fields1[1]
mac_add1 = fields1[3]

fields2 = mac2.split()
ip2 = fields2[1]
mac_add2 = fields2[3]

fields3 = mac3.split()
ip3 = fields3[1]
mac_add3 = fields3[3]

print ()
print ("{:>20}{:>20}".format ("IP_ADDR", "MAC_ADDR"))
print ("{:>20}{:>20}".format ("-"*19, "-"*19))
print ("{:>20}{:>20}".format (ip1, mac_add1))
print ("{:>20}{:>20}".format (ip2, mac_add2))
print ("{:>20}{:>20}".format (ip3, mac_add3))
print ()


