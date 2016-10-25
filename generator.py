import random
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
    	if len(sys.argv) < 5:
        	sys.exit("Not enough params! usage: max_x max_y count out_file_name")
		
   	l = generate_towns(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    	write_file(sys.argv[4], l)
	
if __name__ == "__main__":
	random.seed()
	main()
