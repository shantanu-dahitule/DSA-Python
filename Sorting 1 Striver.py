'''

                            Sorting Technique

'''
# array = [9,6,7,2,0,4,7,3,1,8]
arr = [9,8,7,6,5,4,3,2,1,0]
n = len(arr)

# # Bubble Sort =======================
# for i in range(n):
#     print("step {} and array {}".format(i,array))
#     for j in range(n-1):
#         if(array[j]>array[j+1]):
#             array[j],array[j+1] = array[j+1],array[j]
# print("Sorted Array is : ",array)

# # Selection Sort =========================
# for i in range(n):
#     min_id = i
#     print("Minimum {} Element {} and Array {}".format(i,array[min_id],array))
#     for j in range(i+1,n):
#         if(array[min_id]>array[j]):
#             array[min_id],array[j] = array[j],array[min_id]
            
# print("Sorted Array: ",array)

# #Insertion Sort
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if arr[j - 1] > arr[j]:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#         else:
#             break
# print(arr)
