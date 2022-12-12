# Write a program program to find a local minima in an array


def localMinUtil(arr, low, high, n):

	mid = low + (high - low) // 2

	if(mid == 0 or arr[mid - 1] > arr[mid] and mid == n - 1 or arr[mid] < arr[mid + 1]):
		return mid


	elif(mid > 0 and arr[mid - 1] < arr[mid]):
		return localMinUtil(arr, low, mid - 1, n)

	return localMinUtil(arr, mid + 1, high, n)


def localMin(arr, n):

	return localMinUtil(arr, 0, n - 1, n)



arr = []
n=int(input("Enter number of element in an array:"))
for i in range(n):
    element=int(input("Enter Element :"))
    arr.append(element)
print("local minima is ",arr[localMin(arr, n)])


