from main import *

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 36 #TODO
	assert work_calc(20, 3, 2) == 230 #TODO
	assert work_calc(30, 4, 2) == 870 #TODO

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 19 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 1400 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 870 #TODO


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
	
	# create work_fn1
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n)
	# create work_fn2
	work_fn2 = lambda n: work_calc(n, 3, 2, lambda n: n)
	
	res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():
	# TODO
