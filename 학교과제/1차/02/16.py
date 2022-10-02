def tuple_double_rev(t):
	t1 = list(t)
	t2 = sorted(t1, reverse=True)
	t3 = t1 + t2
	result = tuple(t3)
	return result

print(tuple_double_rev(('a', 'b')))