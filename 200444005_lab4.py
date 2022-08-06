#s200444005 Gökhan Kadir Karagöz
#question 1

f = open(alice29.txt,'r')
data = f.read()
words = data.split(' ')
d = {}
data1 = data.lower()

for c in data1:
    if d.get(ord(c))==None:
        d[ord(c)]=0
else:
    d[ord(c)]+=1

f.close()
f = open(alice29,'r')
lines = f.readlines()
print("Lines: ",len(lines))
print("Words: ",len(words))
print("Characters: ",len(data))

for char in d:
    if char in range(97,97+26):
        print('%s appears %d times'%(chr(char),d[char]))