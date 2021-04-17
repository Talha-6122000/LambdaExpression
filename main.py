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
# Let's do something else
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames = ['John','Cindy','Sarah','Kelly','Mike']
s=list(map(splicer,mynames))
print(s)
# There's another function called filter
# What does it do is filter thing and return true or false
def check_even(my_numss):
  if(my_numss)%2==0:
    return my_numss % 2 == 0 
nums = [0,1,2,3,4,5,6,7,8,9,10]
num_filter=list(filter(check_even,nums))
for i in num_filter:
  print(i)