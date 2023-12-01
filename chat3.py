line=[]
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for a in f:
		line.append(a.strip())
for b in line:
	s = b.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(s)
		
