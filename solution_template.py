#!/usr/bin/env python3

"""
	Problem Summary:
"""


path_to_input_file = './01_input.txt'


def array_from_txt_file(path_to_file):
	f = open(path_to_file, 'r')
	array = [int(line) for line in f.readlines()]
	f.close()
	return array


def part_01():
	pass


def part_02():
	pass


def main():
	part_01()


if __name__ == '__main__':
	main()
