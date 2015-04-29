

string = "I am that I am"

def word_count(string):
	string = string.lower()
	string = string.split()
	string_dict = {}
	for word in string:
		if word in string_dict:
			string_dict[word] = string_dict[word] + 1
		else:
			string_dict[word] = 1
	return string_dict
	print(string_dict)

word_count(string)