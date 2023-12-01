def read(filename):
	line=[]
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for a in f:
			line.append(a.strip())
	return line
def convert(line):
	allenword = 0
	vikiword = 0
	asc = 0
	vsc = 0
	ai = 0
	vi = 0
	for b in line:
		s = b.split(' ')
		time=s[0]
		name=s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				asc += 1
			elif s[2] =='圖片':
				ai += 0
			else:
				for m in s[2:]:
						allenword += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				vsc += 1
			elif s[2] =='圖片':
				vi += 0
			else:
				for m in s[2:]:
					vikiword += len(m)
	print('allen打了:', allenword, asc, ai)
	print('viki打了:', vikiword, vsc, vi)

def write(filename, line):
	with open(filename, 'w') as c:
		for d in line:
			c.write(d + '\n')


def main():
	line=read('LINE-Viki.txt')
	convert(line)
main()