x = 11
y = 29

# Write code to reverse the values in variables x and y

# Using third variable
temp = x
x = y 
y = temp

# Without using third variable
x = x + y	# 40
y = x - y	# 11
x = x - y	# 29

# Can you swap the values of x and y without using third variable?

print(x) # 29
print(y) # 11
