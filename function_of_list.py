#len()  returns lenght of list

a=[2,3,4,5,6,7,8]
print(len(a))
print(a)


#list()  creates an empty list at first 

b="saif"
a = list() #retuns empty list
a = list(b) #makes a new list with inserting element
print(a)

#append() adds new element in last

a=[5,6,7,8,9]
a.append(25)
a.append(26)
a.append([25,45])
print(a)

#extend()  adds more than one argument in last

a=[23,54,67,87,786]
b=[45,56.8,78,"saif"]
a.extend(b)
c = a+b
print(a)

#insert()  inserts at particular index

a=[2,3,4,5,7,8,9]
a.insert(2,1067)
print(a)

#count()   counts the number of times element occured

a=[2,3,4,2,46,7,87,46,98,98]
print(a.count(98))


#index()    returns first occurence of the element
a=[2,2,2,2,34,56,78,34,97]
print(a.index(34))

#remove()  removes element fromt the list

a=[2,4,5,67,97,33,2]
a.remove(2)
print(a)

#pop()  removes using index number if nothing is given then pops the last element
a=[2,3,4,5,6,7,8]
print(a.pop(2)) # pops and print thge popped element as well as list after removing element

#reverse()   prints in reverse form
a=[2,3,4,5,56,67]
a.reverse()
print(a)


#sort()  by default sorts in ascending order and while using reverse=True sorts in decending
a=[2,56,7,89,45,78,5,456878,5654,]
b=["saif","cat","dog","sheep","ship"]
a.sort()  #ascending
a.sort(reverse=True) #decending
b.sort()
b.sort(reverse=True)
print(a)
print(b)

#sorted  sorts but in new list
a=[2,3,4,5,6,7,8,95,5,4,553,355,535,]
b=sorted(a)
print(b)

#min()  smallest element in list
#max()  largest element in list
#sum()  sum of list
a=[2,54,67,86]
b= min(a)
c= max(a)
print(b)
print(c)
print(sum(a))  