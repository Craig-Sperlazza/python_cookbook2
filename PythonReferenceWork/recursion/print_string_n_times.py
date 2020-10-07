#prints a string n times recursively

def print_n(user_string, n_times):
	"""prints a string n times"""
	if n_times <= 0:
		return
	else:
		print(user_string), print_n(user_string, n_times - 1)

print_n("Hello", 5)