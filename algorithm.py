def factorization(n):  # функция для разложения числа на простые множители
	r = n
	i = 2
	result_list = []
	while i*i <= n:
		while n % i == 0:
			result_list.append(int(i))
			n = n/i
		i = i+1
	if n > 1:
		result_list.append(int(n))
	# print(result_list)
	if len(result_list) == 1:
		result = "{} = 1 * {}".format(r, r)
	else:
		result = "{} = {}".format(r, ' * '.join(map(str, result_list)))
	if r < 2:
		result = "error, try again"
	return result
