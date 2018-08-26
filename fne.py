#!/usr/bin/env python3

"""
fne = file name editor
"""

import argparse
import os
import sys


def print_names(names, msg):
	print("{:*^30s}".format(msg))
	for name in names:
		print(name)
	print("\n")


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--default", help="rm final 12 char (for youtube-dl)", action='store_true')
	parser.add_argument("-s", "--start", help="starting index for file name slice", type=int, nargs='?', default=None)
	parser.add_argument("-e", "--end", help="ending index for file name slice", type=int, nargs='?', default=None)
	parser.add_argument("-l", "--lowercase", help="lowercase file names", action='store_true')
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit()
	return parser.parse_args()


def execute_edits():
	user_confirmation = input("look good? (RETURN to execute ||| 'r' to redo args ||| 'q' to quit) ➡️   ")
	if user_confirmation == "":
		print('modification confirmed')
		for orig, new in zip(orig_names, new_names):
			os.rename(orig, new)
		print('🔼  modification complete')
	else:
		print('🔽  modification aborted')


# take inputs
args = parse_args()

# store file names
orig_names = [x for x in os.listdir('.') if x[-3:]=="mp3" and os.path.isfile(x)]
print_names(orig_names, "original names")
new_names = list()

# --default
if args.default:
	new_names = [x[:-16]+".mp3" for x in os.listdir('.') if x[-3:] == "mp3" and os.path.isfile(x)]
# --end
elif args.end:
	args.end = -args.end
	new_names = [x[args.start:args.end-4]+".mp3" for x in os.listdir('.') if x[-3:] == "mp3" and os.path.isfile(x)]
# --start
else:
	new_names = [x[args.start:] for x in os.listdir('.') if x[-3:]=="mp3" and os.path.isfile(x)]

print_names(new_names, "updated names")

# edit
execute_edits()
