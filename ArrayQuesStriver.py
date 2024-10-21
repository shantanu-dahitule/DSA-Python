"""

                            Arrays and Questions
"""

# arr = [1, 3, 87, 0,0,0,0,85, 39, 14, 78, 8]
# n = len(arr)
## Largest element of array
# # 1st approach
# print("Max element: ",max(arr))

# # 2nd approach
# maxe = arr[1]
# for i in arr:
#     if(maxe<i):
#         maxe = i
#     else:
#         continue
# print("Max element: ",maxe)

## Second Largest and Second smallest element
# max_ele = arr[0]
# min_ele = arr[0]
# second_max = arr[0]
# second_min = arr[0]
# for i in range(n):
#     max_ele = max(max_ele,arr[i])
#     min_ele = min(min_ele,arr[i])
# for i in range(n):
#     if arr[i] < second_min and arr[i]!=min_ele:
#         second_min = arr[i]
#     if arr[i] > second_max and arr[i]!=max_ele:
#         second_max = arr[i]
# print("Second max {} and Second min {}".format(second_max, second_min))

## Check if array is sorted or not
# arr = [3,4,5,1,2]
# for i in range(len(arr)-1):
#     if(arr[i]<=arr[i+1]):
#         flag=True
#         continue
#     else:
#         flag=False
#         break
# if flag is False:
#     print("Array is Unsorted")
# else:
#     print("Array is sorted")

# ## Remove Duplicate from Sorted Array
# arr = [1,1,2,2,3,4,8,9]
# # # Brute Force Approach
# # arr = set(arr)
# # print(arr)

# ## 2 Pointer approach
# i = 0
# for j in range(1,len(arr)):
#     if(arr[i]!=arr[j]):
#         arr[i+1] = arr[j]
#         i+=1
#     else:
#         j+=1
# print(arr)    
# print(i+1)

# ## Left Rotate Array
# n=int(input("How many palces wants to rotate: "))
# for j in range(n):
#     f2l = arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1] = arr[i]
#     arr[len(arr)-1] = f2l
# print(arr)

## Put zeroes at end
# arr = [1,2,0,3,0,0,4]
# i=0
# j=0
# while(j!=len(arr)-1):
#     if arr[i]!=0:
#         print("i: ",i)
#         i+=1
#     if arr[j]==0 and j>i:
#         print("j: ",j)
#     j += 1
#     arr[i],arr[j] = arr[j],arr[i]
    
# print(arr)    
    
## Union of Array
# # Brute Forece Approach
# arr1 = [1,2,3,4,5,6]
# arr2 = [3,4,5,6,7,9]
# union = []
# # freq = {}
# # for num in arr1:
# #     freq[num] = freq.get(num,0)+1
    
# # for num in arr2:
# #     freq[num] = freq.get(num,0)+1

# # for num in freq:
# #     union.append(num)
# # print(union)

# ### Optimal Approach 2 pointer method
# i=0
# j=0
# while(i<len(arr1) and j<len(arr2)):
#     if arr1[i]<arr2[j]:
#         union.append(arr1[i])
#         i+=1
#     if arr1[i]>=arr2[j]:
#         union.append(arr2[j])
#         i+=1
#         j+=1
# while(i<len(arr1)):
#     union.append(arr1[i])
#     i+=1
# while(j<len(arr2)):
#     union.append(arr2[j])
#     j+=1
# print(union)    

## Find missing number in sequence
# arr = [1,2,3,5,6]
# n = len(arr)+1
# esum = int(n*(n+1)/2)
# tsum=0
# for i in range(len(arr)):
#     tsum = tsum+arr[i]
# print(esum-tsum)


## Maximum Consecutive ones 
# arr = [1, 0, 1, 1, 0, 1]
# max1 = 0
# count=0
# for i in range(len(arr)):
#     if arr[i]==1:
#         count+=1
#     if count>=max1:
#         max1 = count
#     if arr[i]==0:
#         count = 0
# print("Maximum ones together: ",max1)

# ## Find the number that appears once, and the other numbers twice
# arr = [4,1,2,1,2]
# freq = {}
# for i in range(len(arr)):
#     freq[arr[i]] = freq.get(arr[i],0)+1
# for i in freq:
#     if freq[i]==1:
#         print(i)

# ## Approach 2
# xor = 0
# for i in range(len(arr)):
#     xor = xor^arr[i]

# print(xor)

        
        
        





    
    
    
    
    
    
    
    
    