def test_distinct(input):
  if len(input) == len(set(input)):
    return True
  else:
    return False;
print(test_distinct(input))
#print(test_distinct([2,4,5,5,7,9]))

