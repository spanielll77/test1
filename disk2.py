x = open("file.txt","r")
a = x.read()
b = x.readlines()
c = x.readlines()
print(a)
print(b)
print(c)
for line in x.readline():   # read lines
    print (line)
x.close()
