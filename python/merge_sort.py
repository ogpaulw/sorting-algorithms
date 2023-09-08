### (probably quite a pythonic) merge sort

def merge_sort(arr): # arr is a list* of unsorted numbers (both integer and float).			*I know it says "arr", which clearly isn't the short-hand for list, but it's obvious what it represents - especially in the context of a sorting algorithm; it also makes sense to use considering that most other languages have actual arrays and not just lists in disguise.
	arr_len = len(arr)
	left = []
	right = []
	if arr_len > 1:
		halfway_index = round(arr_len/2) # halfway point (or the closest even index - due to how round() rounds) of the input array.
		left = arr[:halfway_index] # left_arr is elements 0 (incl.) to halfway_index (excl.).
		right = arr[halfway_index:] # right_arr is elements halfway_index (incl.) to arr_len (excl.)
		left = merge_sort(left) # time to go back and recurse with the split array
		right = merge_sort(right) # "
	elif arr_len == 1: # return arr ONLY IF ARR IS LENGTH OF 1, otherwise continue
		return arr
	
	sorted_arr = []
	
	# BASIC PRINCIPLE OF FOLLOWING CODE IS AS FOLLOWS:
	# while left list is not empty,
	# check the first element in it against the first element in the right list.
	# if left list first element is smaller than right list first element,
	# add left list first element to temp_arr and pop/delete first element from left list (shifts indices of all following elements by -1).
	# else,
	# add right list first element to temp_arr and pop.delete first element from right list.
	
	while len(left) > 0: # while the left list isn't empty.
		if len(right) > 0: # check the right list isn't empty
			if left[0] < right[0]:
				sorted_arr.append(left[0])
				left.pop(0)
			else:
				sorted_arr.append(right[0])
				right.pop(0)
		else: # if right list IS empty
			sorted_arr.append(left[0])
			left.pop(0)
			
	while len(right) > 0: # in case the left list IS empty, add all elements from right list provided it ISN'T empty.
		sorted_arr.append(right[0])
		right.pop(0)
		
	return sorted_arr

if __name__ == "__main__":	
	random_numbers = [13, 11, 32, 22, 9, 10, 42]
	sorted_numbers = merge_sort(random_numbers)
	print(sorted_numbers)
