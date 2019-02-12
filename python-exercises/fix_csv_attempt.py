# Attempt at solving Trey Hunner's Python Morsels problem: fix_csv

# Original file looks like:
# Reading|Make|Model|Type|Value
# Reading 0|Toyota|Previa|distance|19.83942
# Reading 1|Dodge|Intrepid|distance|31.28257

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("input_file", 
					help = "location/name of input file")
parser.add_argument("output_file", 
					help = "location/name of output file")
parser.add_argument("--in-delimiter", 
					action = 'store',
					default = None)
parser.add_argument("--in-quote",
					action = 'store',
					default = None)
args = parser.parse_args()

with open(args.input_file, newline = '') as in_csv:
	# If delimiter or quote not specified determine it using Sniffer:
	if args.in_delimiter == None or args.in_quote == None:
		dialect = csv.Sniffer().sniff(in_csv.read(1024))
		if args.in_delimiter == None:
			args.in_delimiter = dialect.delimiter
		if args.in_quote == None:
			args.in_quote = dialect.quotechar
		in_csv.seek(0)
	in_reader = csv.reader(in_csv, delimiter=args.in_delimiter, 
							quotechar = args.in_quote)
	
	with open(args.output_file, 'w', newline = '') as out_csv:
		out_writer = csv.writer(out_csv, delimiter = ",")
		for row in in_reader:
			out_writer.writerow(row)