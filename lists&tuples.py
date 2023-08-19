# Lists
list2= ["siva", "imran", "ram", "gopi"]
print(type(list))
list1 = [2.1, 2.9, 8.8, 9]
print(list1)
print(list2[-1])
print(list1[1])
list2[3]="srinu"
print(list2)
list2.append('ravi')
print(list2)
list2.insert(1,"vijay")
print(list2)
list2.extend(["charan", "mahesh"])
print(list2)
add = list2 + list1
print(add)
print(add.index(9))
add.remove("charan")
print(add)
add+=['bharat', 'prabhas']
print(add)
list2.sort()
print(list2)
list1.pop(2)
print(list1)
add.clear()
print(add)

import copy
names=copy.deepcopy(list2)
print(names)

other_names = names
print(other_names)

other_names.remove('vijay')
print(other_names)
print(names)
print(names[1:3])
print(names[:6:])
print(names[::3])
print(names[::-1])
names[4:-1]=['ashish','Radha']
print(names)
print('ram' in names)
print(names.pop(-2))
x="world"
print(x[0])
a,b,c,d,e = x
print(c)
#print(input('How are you? :'))
place= "new york city"
#place=input('where are you from? : ',)
print(place)
print(place.startswith('p'))
print(place.upper())
print(place.find('c'))
split_place=place.split(' ')
print(split_place)
join_char=','
print(join_char.join(split_place))
join_char=' '
print(join_char.join(split_place))

#Tuples

int_tuple=(1,2,3)
str_tuple=('hello', 'python')
print(int_tuple, str_tuple)

combine = int_tuple+str_tuple
print(combine)
my_tuple=2,'hello',3.8
print(my_tuple)
a,b,c=my_tuple
print(a)
print(b)
nested_tuple=(1,2,3,(4,5,6))
mixed_tuple=("hi",[2,4,6],("hello",6,9))
print(nested_tuple[3])
print(mixed_tuple[::-1])
print(mixed_tuple[-1][0])
print(3 in nested_tuple)
print(set(int_tuple))
mix_tuple=(1,2,3,[4,5,6])
mix_tuple[3][0]=9
print(mix_tuple)
t_1=(1,2,3,4,5)
t_2=(6,7,8,9,0)
zipped=zip(t_1,t_2)
print(zipped)
result=tuple(zipped)
print(result)
x,y=zip(*result)
print(x)
print(y)
t_1=(1,2,3,4,5)
t_2=(6,7,8,9,0)
zipped=zip(t_1,t_2)
print(zipped)
result = list(zipped)
print(result)
t_1=("hello","hi","python")
t_2=("siva",'ravi','ram')
zipped=zip(t_1,t_2)
print(zipped)
result = dict(zipped)
print(result)

num_list=[1,2.5,"number",True]
print(type(num_list))
print(type(num_list[1]))
num_list=(1,2.5,"number",True)
print(type(num_list))
print(type(num_list[-1]))