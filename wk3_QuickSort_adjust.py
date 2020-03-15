# Quick sort algorithm
# By Moe under supervision of Chang
# Horrible weekends
# More painful than cornonavirvus

def swap_helpler(ls, idx_a, idx_b):
	temp = ls[idx_a]
	ls[idx_a] = ls[idx_b]
	ls[idx_b] = temp

def adjust(ls, start_index, end_index):

    # Check whether the input is qualified
	if not 0 <= start_index < end_index < len(ls): # Very important line!!!
		return

	pivot_index = (start_index + end_index) // 2
	swap_helpler(ls, start_index, pivot_index)

	j = end_index
	i = start_index + 1

	while i < j:
		while ls[i] < ls[start_index] and i < j:
			i += 1
		while ls[j] > ls[start_index] and i < j:
			j -= 1	
		if i != j:
			swap_helpler(ls, i, j)
	
	if ls[i] < ls[start_index]:
		swap_helpler(ls, start_index, i)
		pivot_index = i
	else:
		swap_helpler(ls, start_index, i - 1)
		pivot_index = i - 1

	adjust(ls, start_index, pivot_index - 1)
	adjust(ls, pivot_index + 1, end_index)

def QuickSort(ls):
	adjust(ls, 0, len(ls) - 1)
				

ls = [0, 3, 2, 1, 4, 5, 6, 9, 8, 7]
QuickSort(ls)
print(ls)
