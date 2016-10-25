import random
import os
import sys

def generate_towns(mx, my, count):
	towns = []

	for i in range(0, count):
		x = random.random() * mx
		y = random.random() * my
		
		towns.append((x,y))
	
	return towns
	
def write_file(name, towns):
	f = open(name, "w")
	f.write(str(len(towns)) + '\n')
	
	for i in towns:
		f.write(str(i[0]) + ' ' + str(i[1]) + '\n')
	
	f.close()
	
def main():
	f = sys.stdin.readline()
	f = f.split(' ')

	l = generate_towns(int(f[0]), int(f[1]), int(f[2]))
	write_file(f[3], l)
	
if __name__ == "__main__":
	random.seed()
	main()
