#Max number of shapes in the pattern
n = 5
#for the variable in the range of 5
for i in range(n):
    for j in range(i):
#Prints $ sign and jumps to next paragraph (Prints it going out instead of in)	
        print ('ʕ•ᴥ•ʔ ☼.☼ ', end="")
#Loops the print
    print('')

for i in range(n,0,-1):
    for j in range(i):
#Prints $ sign and jumps to next paragraph (Prints it going in instead of out)
        print('☼.☼ ʕ•ᴥ•ʔ ', end="")
#Loops the print
    print('')
	
