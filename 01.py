#!/usr/bin/env python3

"""
	Problem Summary:
		find the two entries that sum to 2020,
		and then multiply those two numbers together.

		keys:
			"The entires", indicates that the input contains
			exactly two entries which sum to 2020.
"""


path_to_input_file = './01_input.txt'


def array_from_txt_file(path_to_file):
	f = open(path_to_file, 'r')
	array = [int(line) for line in f.readlines()]
	f.close()
	return array


def part_01():
	targets = None
	candidates = array_from_txt_file(path_to_input_file)
	candidates.sort()

	# remove elements too large to be viable candidates
	# slice array where target_value < a[0] + a[i]

	for i in range(len(candidates)):
		if candidates[0] + candidates[i] > 2020:
			candidates = candidates[:i]
			break


	for i in range(len(candidates)):
		if targets:
			print(targets)
			print(targets[0] * targets[1])
			break
		for j in range(len(candidates)):
			if i == j:
				pass
			if candidates[i] + candidates[j] == 2020:
				targets = (candidates[i], candidates[j])
				break


def part_02():
	targets = None
	candidates = array_from_txt_file(path_to_input_file)
	candidates.sort()

	# remove elements too large to be viable candidates
	# slice array when target_value < a[0] + a[1] + a[i]

	for i in range(len(candidates)):
		if candidates[0] + candidates[1] + candidates[i] > 2020:
			candidates = candidates[:i]
			break


	# add another nested loop for the third value
	for i in range(len(candidates)):
		if targets:
			print(targets)
			print(targets[0] * targets[1] * targets[2])
			break
		for j in range(len(candidates)):
			if targets:
				break
			for k in range(len(candidates)):
				if i == j or i == k or j == k:
					pass
				if candidates[i] + candidates[j] + candidates[k] == 2020:
					targets = (candidates[i], candidates[j], candidates[k])
					break


def main():
	part_02()


if __name__ == '__main__':
	main()
