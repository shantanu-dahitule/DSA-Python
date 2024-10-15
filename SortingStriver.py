'''

                            Sorting Technique

'''
# array = [9,6,7,2,0,4,7,3,1,8]
array = [9,8,7,6,5,4,3,2,1,0]
n = len(array)-1

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

# # Quick Sort ============================

# def partition(list, low:int, high:int):
#     pivote = list[low]
#     i = low
#     j = high
#     while(i<j):
#         while(list[i]<=pivote and i<=high-1):
#             i+=1
#         while(list[j]>pivote and j>=low+1):
#             j-=1
#         if(i<j):
#             list[i], list[j] = list[j], list[i]
    
#     list[low], list[j] = list[j], list[low]
#     return j
            

# def qs(list,low:int, high:int):
#     if(low<high):
#         partitionIndex = partition(list, low, high)
#         qs(list, partitionIndex+1,high)
#         qs(list, low, partitionIndex)
# qs(array,0,n)        
# print(array)


