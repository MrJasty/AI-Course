import math

start = 100 
end = 1000
sum = 0

while (start <= end):
	number = start
	

	#Check if number is an armstrong number
	while(number > 0):
		rem = (number % 10)
		number = number / 10
		sum = sum + math.pow(rem, 3)
	if(sum == start):
		print(start)
	start = start - 1
					
