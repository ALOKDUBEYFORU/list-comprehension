
#a simple list comprehension

try:
    list1 = [1,2,3,4,5]
    list2 = [i+1 for i in list1]
    print(list2)
except Exception as e:
    print(e)




#a list comprehension with an if condition

try:
    list1 = [1,2,3,4,5]
    list2 = [i for i in list1 if i%2 == 0 ]
    print(list2)
except Exception as e:
    print(e)



#a list comprehension with an if else condition

try:
    list1 = [1,2,3,4,5]
    list2 = ['even' if i%2 == 0 else 'odd' for i in list1]
    print(list2)
except Exception as e:
   print(e)




# list of unpacking the elements of a matrix

list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

list2 = [i for row in list1 for i in row]

print(list2)

#list comprehension for 3*3 matrix

list1 = [[[1,2,3],
          [4,5,6]],
         [[7,8,9],
          [10,11,12]]]

list2 = [i for matrix1 in list1 for row in matrix1 for i in row]

print(list2)



#Set comprehension

set1 = {1,2,3,4,5,5,6}
print(set1)
set2 = {i*i for i in set1}
print(set2)


#Dictionary comprehension

list1 = [0,1]
list2 = ['Female','Male']

dict1 = {key1:value1 for key1,value1 in zip(list1,list2)}

print(dict1)


#Dictionary comprehension using two disctionaries.

dict1 = {'a':1,'b':2}
dict2 = {1:'odd',2:'even'}


dict3 = {key1:dict2[value1] for key1,value1 in (dict1.items()) }
print(dict3)




#Food for thought

str1 = 'ABC'
list1 = list(str1)
dict1 = {key1:value1 for key1,value1 in zip(list1,range(len(list1))) }
print(dict1)

