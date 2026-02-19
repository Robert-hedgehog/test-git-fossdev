from script import sum, devide, substruct

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
		devide([1, 2, 3], [4, 5, 6])
		print('Test list-devision failed')
		assert False
	except ValueError as e:
		print("Test string-devision passed")

	try:
		devide("A", "B")
		print('Test string-devision fails')
		assert False
	except ValueError as e:
		print("Test string-devision passed")

def test_substruct():
	a = 5
	b = 3
	result = 2
	assert substruct(a, b) == result
	print("Test substruct passed")


if __name__ ==  "__main__":
	test_devide()
	test_sum()
	test_devision_prohibited()
	test_substruct()