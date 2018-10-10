
banner = "-" * 80

#use / rather than \ in file location
f = open("c:/Users/wilso/Desktop/Python/Lesson 2/show_version.txt")
show_ver = f.read()

print(banner)
print(show_ver)
print(banner)
print(type(show_ver))
print(banner)
f.close()

with open("c:/Users/wilso/Desktop/Python/Lesson 2/show_version.txt")as f:
    output = f.readlines()

print("\n")
print(banner)
print(output)
print(type(output))
print(banner)
print("\n")
