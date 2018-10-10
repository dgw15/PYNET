# exercise 4
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 
show_version = show_version.strip()

fields = show_version.split()
model = fields[1]
serial_number = fields[2]

print ()
vendor_cisco = "cisco" in model.lower()
print ("Checking if cisco is in model: {}".format(vendor_cisco))

model_881  = "881" in model
print ("is 811 in model: {}".format (model_881))

print ("model: {}".format(model))
print ("serial number: {}".format(serial_number))
print ()
