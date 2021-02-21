def get_2d_array(array, x, y):
	""" Get the value of the given array at the given position, or None if it is out of range (instead of a runtime error) """
	if y >= len(array) or y < 0:
		return None
	if x >= len(array[y]) or x < 0:
		return None
	return array[y][x]
