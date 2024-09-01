N=5
arr=[1]*N      #Here we are multiplying the number of rows by the empty list and hence the entire list is created with every element zero.
print("Create Array of Size n with 0 as value",arr)    ##creating one d array usnig list
N=5
arr=[]*N   
print("Create empty list:",arr)
arr=[0 for i in  range (N)]
print("Using range :",arr)
rows,cols=(5,5)
arr=[[0]*rows]*cols
print("Here we are multiplying the number of rows and hence we are getting the 1-D list of size equal to the number of rows and then multiplying it with the number of cols which results in the creation of a 2-D list :",arr)
print(arr,"Before")
arr[0][0]=1
print(arr,"After")

arr=[[0  for i in range(rows)] for j in range(cols)]
print("applying a loop for a list inside a list and hence creating a 2-D list",arr)
print("Here we are appending zeros as elements for a number of columns times and then appending this 1-D list into the empty row list and hence creating the 2-D list:")
arr=[]
rows,cols=(5,5)
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(j)
    arr.append(col)   
print(arr) 
##initializing 2-d array
rows,cols=(5,5)
arr=[[0]*cols]*rows ##all point to only one object 
arr[0][0]=1
for i in arr:
    print(i)
print("arr[1] is arr[0] :",arr[1] is arr[0])
##good way of declaring array
arr=[[i for i in range(N)] for j in range(rows)]
arr[0][0]=4
for i in arr:
    print(i)
print("arr[1] is arr[0]:",arr[1] is arr[0])
flat_list=[arr]
print()
##initialize 2 d array
# arr=[
#     [1,2,3,4],
#     [3,4,3,2],
#     [5,6,7,8]]
print("Accesing element using Subscript operator :",arr[1][3],arr[3][1],arr[0][0])
arr=[[i for i in range(cols)] for j in range(rows)]
for i in arr:
    print(i)
c=len(arr[0])
r=len(arr)
print(c,r)
tranpose=[[arr[r][c] for r in range(len(arr))] for c in range(len(arr[0]))]
print(tranpose)


