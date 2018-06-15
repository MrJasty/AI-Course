# Python code to reverse a string 
# using loop
 
def rev(s):
  str = ""
  for i in s:
    str = i + str
    #print(str)
  return str

#s = "Jared Griffith"
s = input()

print ("The original name is : ",end="")
print (s)
 
print ("The reversed name (using loops) is : ",end="")
print("-------")
print (rev(s))
