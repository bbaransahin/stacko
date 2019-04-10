def calc(exp):
	index_of_first_space = exp.index(" ")
	first_value = int(exp[:index_of_first_space])
	second_value = int(exp[index_of_first_space+2:len(exp)])
	operator = exp[index_of_first_space+1]
	if operator == "+":
		return (first_value+second_value)
	elif operator == "-":
		return (first_value-second_value)
	elif operator == "*":
		return (first_value*second_value)
