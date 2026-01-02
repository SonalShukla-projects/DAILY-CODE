# | Reverse array |
arr =[1,2,3,4]
n=len(arr)
for i in range(n-1,-1,-1):
    print(arr[i])
    

# | Max & Min | 
a=[1,2,3,4,5]
print(max(a))
print(min(a))


# | Kth max-min |
b=[5,2,7,9,4]
k=int(input("Enter kth value:"))
b.sort()
print(b[k-1])
print(b[-k])


