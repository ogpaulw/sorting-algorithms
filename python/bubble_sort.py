### bubble sort (just to add another easy one to the collection)

def bubble_sort(arr):
	isSorted = False
	arr_len = len(arr) # stops multiple calls to len()
	
	while not isSorted:
		trueUntilDisorder = True
		for i in range(0,arr_len-1): # although range()'s 2nd arg is excl., I am comparing the current element to the next and so the last item in the array can't have a next element, thus, it cannot be checked.
			if arr[i] > arr[i+1]:
				trueUntilDisorder = False
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				del temp # temp is no longer needed, delete variable from memory. (not really needed, but I like pretending to be writing in C without any of the hassle).
		if trueUntilDisorder:
			isSorted = True
	return arr



if __name__ == "__main__":
	unsorted_numbers = [53,82,78,100,41,17,16]
	sorted_numbers = bubble_sort(unsorted_numbers)
	print(sorted_numbers)
