"""

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

"""

n = 5
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(n):
#     for j in range(n-i-1):
#         print(j+1,end=" ")
#     print()
""" 
    Diamond
"""
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(2 * n, 2 * i + 1, -1):
#         print("*", end=" ")
#     for j in range(i):
#         print(" ", end=" ")
#     print()
"""
Vertical Triangle
"""
# for i in range(n-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()

"""
0 1 Triangle
"""
# start = 1
# for i in range(n):
#     if i%2==0: start=1
#     else: start=0
#     for j in range(i+1):
#         print(start,end=" ")
#         start=1-start
#     print()

"""
Double numeric Triangle
"""
# k=1
# for i in range(n):
#     for j in range(i):
#         print(j+1,end=" ")
#         k+=1
#     for j in range(2*(n-i-1)):
#         print(" ",end=" ")
#     # for j in range(n-i-1):
#     #     print(" ",end=" ")
#     for j in range(i):
#         k=k-1
#         print(k,end=" ")
#     print()

"""
Traingle with 1 to end 
"""
# count=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(count,end=" ")
#         count+=1
#     print()
"""
Charecter Triangle
"""
# count=65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(count),end=" ")
#         count+=1
#     print()

"""
Empty Diamond
"""
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         print("*", end=" ")
#     for j in range(2 * i + 1):
#         print(" ", end=" ")
#     for j in range(n - i - 1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * n, 2 * i + 1, -1):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()
"""
Repetative charecter Triangle
"""
# count=65
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(chr(count),end=" ")
#         count+=1
#     count=65+i
#     for j in range(i):
#         count-=1
#         print(chr(count),end=" ")
#     print()
#     count=65
"""
Char Triangle
"""
# for i in range(n):
#         for ch in range(ord('A') + n - 1 - i, ord('A') + n):
#             print(chr(ch), end=" ")
#         print()
    
"""
Empty mid Sqaure
"""
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()


