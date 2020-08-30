def bubble_sort(unsorted_list):
	 sorted = False
	 index = len(unsorted_list) - 1 

	 while not sorted:

	 	for i in range(0, index):
		 	sorted = True
		 	if unsorted_list[i] < unsorted_list[i+1]:
			 	sorted = False
			 	unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1],unsorted_list[i]

	 return unsorted_list

def main():
	list = [1, 6, 9, 10, 2, -1]
	sorted_list = bubble_sort(list)
	print(sorted_list)


main()