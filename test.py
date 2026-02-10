from script import sum, devide

def test_sum():
	a = 1
	b = 2
	result = 3
	assert sum(a, b) == result

def test_devide():
	a = 4
	b = 2
	result = 0.5
	assert devide(b, a) == result

def test_devision_prohibited():
	try:
		devide("A", "B")
		print('Test string-devision fails')
		assert False
	except ValueError as e:
		print("Test string-devision passed")

if __name__ ==  "__main__":
	test_devide()
	test_sum()
	test_devision_prohibited()
