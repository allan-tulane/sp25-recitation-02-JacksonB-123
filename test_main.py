from main import *


def test_simple_work():
	assert simple_work_calc(10, 2, 2) == 36  #TODO
	assert simple_work_calc(20, 3, 2) == 230  #TODO
	assert simple_work_calc(30, 4, 2) == 650  #TODO
	#compelte 3 additional test cases for simple_work_calc
	assert simple_work_calc(40, 2, 2) == 224
	assert simple_work_calc(50, 2, 2) == 276
	assert simple_work_calc(60, 3, 2) == 960


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15  #TODO
	assert work_calc(20, 1, 2, lambda n: n * n) == 530  #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300  #TODO
	# complete 3 additional test cases for work_calc
	assert work_calc(40, 2, 2, lambda n: n) == 224
	assert work_calc(50, 2, 2, lambda n: n) == 276
	assert work_calc(60, 3, 2, lambda n: n) == 960


def test_compare_work():
	#Adding size for question 5
	sizes = [10, 20, 50, 100, 1000, 5000, 10000]

	# create work_fn1
	#modification from the original code for Question 5 c < log_b a
	work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n**0.5)
	# create work_fn2
	#modification from the original code for Question 5 c > log_b a
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n)

	# create work_fn3
	#modification from the original code for Question 5 c = log_b a
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n**2)
	#res = compare_work(work_fn1, work_fn2) commented out for question 5
	comparison1 = compare_work(work_fn1, work_fn2, sizes)
	comparison2 = compare_work(work_fn2, work_fn3, sizes)
	#printing empirical results for question 5
	print("\nComparing Work Functions: c < log_b a vs. c = log_b a")
	print_results(comparison1)

	print("\nComparing Work Functions: c = log_b a vs. c > log_b a")
	print_results(comparison2)

	#I had to look the assert part up online to see how to get output from the shell.
	# I also did not know I had to use pytest -s test_main.py::test_compare_work to generate my output in the shell.
	#For the next lab can the instructions be more clear? I spent many hours trying to figure out what question 4 , 5 and 6 were asking. I went to TA's and asked peers for help but it was still challenging.
	assert comparison1 is not None
	assert comparison2 is not None


def test_compare_span():
	# TODO

	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	# Span for f(n) = 1 (Logarithmic Span)
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)

	# Span for f(n) = log(n) (Log-Squared Span)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: math.log(n))

	# Span for f(n) = n (Linear Span)
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda n: n)

	comparison1 = compare_span(span_fn1, span_fn2, sizes)
	comparison2 = compare_span(span_fn2, span_fn3, sizes)

	print("\nComparing Span Functions: Logarithmic vs. Log-Squared")
	print_results(comparison1)

	print("\nComparing Span Functions: Log-Squared vs. Linear")
	print_results(comparison2)

	assert comparison1 is not None
	assert comparison2 is not None
