# from array import *
# vals=array('i',[1,2,3,4,5,6,7,8,9])
# newArr=array(vals.typecode,(a*a for a in vals))
# for i in newArr:
#     print (i)

from array import *
arr=array('i',[])
n=int(input("Enter the array length: "))
for i in range(n):
    arr.append(int(input("Enter the element: ")))
for e in arr:
    print(e)
val=int(input("Enter the value to search: "))
x=0
for y in arr:
    if val==y:
        print(f'The value is in index {x}')
    x+=1