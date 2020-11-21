def smallest_substring(input_string):
	a = set()
	a.add(input_string[0])
	i = 0
	j = 1
	res = 1
	while i<=j and j<len(input_string):
		if input_string[j] in a:
			a.remove(input_string[i])
			i+=1
		else:
			a.add(input_string[j])
			j+=1
		res = max(len(a),res)
	return res

input_string = input()
print(smallest_substring(input_string))
