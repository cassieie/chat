def read(filename):
	line=[]
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for a in f:
			line.append(a.strip())
	return line
def convert(line):
	new=[]
	person = None
	for b in line:
		if b == 'Allen':
			person = 'Allen'
			continue
		elif b == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ':' + b)
	return new
def write(filename, line):
	with open(filename, 'w') as c:
		for d in line:
			c.write(d + '\n')


def main():
	line=read('input.txt')
	line=convert(line)
	write('output2.txt', line)
main()