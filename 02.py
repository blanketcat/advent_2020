#!/usr/bin/env python3

"""
	Problem Summary:
		For example, 1-3 a means that the password 
		must contain a at least 1 time and at most 3 times.

		In the above example, 2 passwords are valid.
		The middle password, cdefg, is not;
		it contains no instances of b, but needs at least 1.
		The first and third passwords are valid:
		they contain one a or nine c,
		both within the limits of their respective policies.

		OUTPUT:
			int -> number of valid passwords in the pword list
"""


path_to_input_file = './02_input.txt'


def array_from_txt_file(path_to_file):
	f = open(path_to_file, 'r')
	array = [line for line in f.readlines()]
	f.close()
	return array


def parse_entry(entry):
	"""
		Example:
			3-5 g: ggggmhf
			2-3 h: smfhh
	"""
	entry = entry.split(': ')
	entry = entry[0].split() + entry[1:]
	entry = entry[0].split('-') + entry[1:]

	entry_dict = {
		'min': int(entry[0]),
		'max': int(entry[1]),
		'value': entry[2],
		'password': entry[3]
	}

	return entry_dict


def validate_count_entry(entry_dict):
	password = [char for char in entry_dict['password']]
	if entry_dict['min'] <= password.count(entry_dict['value']) <= entry_dict['max']:
		return True
	else:
		return False


def validate_positional_entry(entry_dict):
	password = [char for char in entry_dict['password']]
	check_chars = password[entry_dict['min'] - 1], password[entry_dict['max'] - 1]
	if check_chars.count(entry_dict['value']) == 1:
		return True
	else:
		return False


def part_01():
	count = 0
	for entry in array_from_txt_file(path_to_input_file):
		if validate_count_entry(parse_entry(entry)):
			count += 1

	print(count)


def part_02():
	count = 0
	for entry in array_from_txt_file(path_to_input_file):
		if validate_positional_entry(parse_entry(entry)):
			count += 1

	print(count)


def main():
	part_02()


if __name__ == '__main__':
	main()
