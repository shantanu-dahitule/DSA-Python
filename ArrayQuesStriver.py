"""

                            Arrays and Questions
"""

arr = [1, 3, 87, 85, 39, 14, 78, 8]
n = len(arr)
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