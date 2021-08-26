def sum_of_squares(a):
	sum = 0
	for i in a:
		sum += i*i;
	print sum


def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    assert sum_of_squares([2,3,4]) == 29
