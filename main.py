"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
# I had to import math to show the work for f(n) = log n. I don't know how to calculate work for f(n) = log n without importing math
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n==1:
		return 1
	else:
			return a*simple_work_calc(n//b, a, b) +n

	

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n==1:
		return f(1)
	else:
		return a*work_calc(n//b, a, b, f) + f(n)
		

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n==1:
		return 1
	else:
		return span_calc(n//b, a, b, f) + f(n)



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result



#For question 4 I am creating a function that calculates the work for the 3 cases using input sizes [1,10,100,1000]
#Jiaru Li helped me at the office hours with question 4 and directed me to https://www.w3schools.com/python/python_string_formatting.asp for python help.
def question4_work_genrator():
	input_size = [1,10,100,1000] #input sizes tested
	
	for n in input_size: # for loop to iterate through the input sizes and print the work of each input size for f(n) = 1
		print(f"W({n}) = {work_calc(n, 2, 2, lambda n: 1)}") #use f string. I recieved help from https://www.w3schools.com/python/python_string_formatting.asp and the TA Jiaru Li.
		
	for n in input_size: # for loop to iterate through the input sizes and print the work of each input size for f(n) = log n
		print(f"W({n}) = {work_calc(n, 2, 2, lambda n: math.log(n))}")
		
	for n in input_size: # for loop to iterate through the input sizes and print the work of each input size for f(n) = n
		print(f"W({n}) = {work_calc(n, 2, 2, lambda n: n)}")
	
	

if __name__ =="__main__": #only runs if main.py is run. Jiaru Li helped me with this part.
	question4_work_genrator()


def question6_span_generator():
	#calculate the span for the same inputs as in question 4

	input_sizes = [1, 10, 100, 1000]

	print("\nSpan Calculation for f(n) = 1:")
	for n in input_sizes: #for loop to iterate through the input sizes and print the work of each input size for f(n) = 1
			print(f"S({n}) = {span_calc(n, 2, 2, lambda n: 1)}") 

	print("\nSpan Calculation for f(n) = log(n):")
	for n in input_sizes:#for loop to iterate through the input sizes and print the work of each input size for f(n) = log
			print(f"S({n}) = {span_calc(n, 2, 2, lambda n: math.log(n))}")

	print("\nSpan Calculation for f(n) = n:")
	for n in input_sizes: #for loop to iterate through the input sizes and print the work of each input size for f(n) = n
			print(f"S({n}) = {span_calc(n, 2, 2, lambda n: n)}")
	

