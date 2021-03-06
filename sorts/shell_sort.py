"""
This is a pure python implementation of the shell sort algorithm

For doctests run following command:
python -m doctest -v shell_sort.py
or
python3 -m doctest -v shell_sort.py

For manual testing run:
python shell_sort.py
"""
from __future__ import print_function


def shell_sort(collection):
	"""Pure implementation of shell sort algorithm in Python
	:param collection:  Some mutable ordered collection with heterogeneous
	comparable items inside
	:return:  the same collection ordered by ascending
	
	>>> shell_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]
	
	>>> shell_sort([])
	[]
	
	>>> shell_sort([-2, -5, -45])
	[-45, -5, -2]
	"""
	# Marcin Ciura's gap sequence
	gaps = [701, 301, 132, 57, 23, 10, 4, 1]
	
	for gap in gaps:
		i = gap
		while i < len(collection):
			temp = collection[i]
			j = i
			print("****")
			while j >= gap and collection[j - gap] > temp:
				print("---------------------->  ",j)
				collection[j] = collection[j - gap]
				j -= gap
			collection[j] = temp
			i += 1
	
	return collection
	
if __name__ == '__main__':
		import sys
		# For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
		# otherwise 2.x's input builtin function is too "smart"
		if sys.version_info.major < 3:
		    input_function = raw_input
		else:
		    input_function = input
		import time                          
		tstart=time.clock()                  
		#pdb.set_trace()                     
		unsorted=list(range(8000,1,-1))  
		#print(sort(unsorted))               
		print(shell_sort(unsorted))                       
		tend=time.clock()                    
		print("read: %f s" % (tend - tstart))
		
		#user_input = input_function('Enter numbers separated by a comma:\n')
		#unsorted = [int(item) for item in user_input.split(',')]
		#print(shell_sort(unsorted))
