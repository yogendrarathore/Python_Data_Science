
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = []
n=int(input("enter nuber of terms:"))
for i in range(n):
    ele=int(input("enter elements:"))
    data.append(ele)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
