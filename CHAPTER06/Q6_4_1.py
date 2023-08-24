%%time
f = open('some.txt')
lines = ''
for i in range(3):
    lines += f.readline()
print(lines)
f.close()
