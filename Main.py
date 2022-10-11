from typing import List

def merge_sort(data) -> None:
  # Write code here
  if len(data) > 1:
 
        mid = len(data)//2
 
        L = data[:mid]
 
        R = data[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1
 
 
 
def printList(data):
    for i in range(len(data)):
        print(data[i], end=", ")
    print()


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
