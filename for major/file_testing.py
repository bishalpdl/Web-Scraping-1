f = open("test.txt", "w")

f.write('a')

f.close()

f = open('test.txt', 'r')
print(f.read())
f.close()
