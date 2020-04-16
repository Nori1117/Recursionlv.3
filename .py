#Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list. 
#f there are no duplicate values, it should return an empty list.

def find_duplicates(list_of_numbers):
x=set(list_of_numbers)
    y=[]
    dup=[]
    count=0
    for i in x:
        y.append(i)
        for i in y:
        for j in list_of_numbers:
        if(j==i):
                count+=1
            if count>=2:
                    dup.append(i)
                    break
                    count=0
    return dup
    
    list_of_numbers=[1,2,3]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
