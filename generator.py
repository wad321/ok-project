import random
import os
import sys

def generate_towns(mx, my, count):
	towns = []
	
	for i in range(0, count):
		x = random.random() * mx
		y = random.random() * my
		
		towns += (x,y)
		
	return towns
	
def write_file(name, towns):
	f = open(name, "w")
	
	f.write(len(towns) + '\n')
	
	for i in towns:
		f.write(i[0] + ' ' + i[1] +'\n')
	
	f.close()
	
def main():
	f = sys.stdin.split(' ')
	
	l = generate_towns(f[0], f[1], f[2])
	write_file(f[3], l)
	
if __name__ == "__main__":
	main()
