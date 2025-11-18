# sets and tuples examples:
# sets examples:
set1 = {1, 2, 3, 4, 5}
print(set1) #{1, 2, 3, 4, 5}
print(type(set1)) #<class'set'>
set1.add(6)
print(set1) #{1, 2 ,3, 4, 5, 6}
set1.remove(2)
print(set1) #{1, 3, 4, 5, 6}

set2 = {"apples", "banana" , "cherry", "cherry"}
print(set2)

#tuples
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) #(1, 2, 3, 4, 5)
print(type(tuple1))
# tuples are immutable, meaning they cannot be chnaged after creatation 
#this makes tuples useful for storing data that should not be modified
social_security_number = (123444, 444445, 5676789)
print(social_security_number) #(123444, 444445, 5676789)