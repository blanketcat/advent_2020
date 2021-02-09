#!/usr/bin/env python3

"""

"""


path_to_input_file = './03_input.txt'


def array_from_txt_file(path_to_file):
	f = open(path_to_file, 'r')
	array = [[char for char in line.strip('\n')] for line in f.readlines()]
	print(len(array[0]))
	print(len(array))
	f.close()
	return array


def part_01():
	position = [0, 0]
	for row in array_from_txt_file(path_to_input_file):
		print(row)


def part_02():
	pass


def main():
	part_01()


if __name__ == '__main__':
	main()
