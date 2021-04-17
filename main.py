# map function
# The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:
def square(num):
  return num**2
my_list=[1,2,3,4,5,6]
for item in map(square,my_list):
  print(item)
# To get the results, either iterate through map() 
# or just cast to a list
x=list(map(square,my_list))
for item in x:
  print(item)
   