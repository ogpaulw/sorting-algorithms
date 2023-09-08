### quicksort (at least, hopefully).

# set pivot to middle
### WIP

def quick_sort(arr): # recursive
	arr_len = len(arr)
	halfway_index = round(len(arr)/2) #halfway_index will always be rounded to the even integer of the two available (built-in round()'s workings).
	cursor_index = 0
	if arr_len > 1:
		pivot = arr[halfway_index] # pivot is set as middle element.
		cursor = 
	return arr



if __name__ == "__main__":
	unsorted_numbers = [73, 75, 12, 41, 36, 43, 76, 97, 40]
	sorted_numbers = quick_sort(unsorted_numbers)
	print(sorted_numbers)
