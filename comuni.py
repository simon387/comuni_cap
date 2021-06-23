import csv

# cap cf array, 2, 5
input_array = []

# array init
with open('docs/comuni_enc.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		else:
			if row[2] != '':
				print(f'{row[2]} {row[5]}')
				input_array.append([row[2], row[5]])
			line_count += 1
	print(f'Processed {line_count} lines.')
	print(f'Len internal array: {len(input_array)}')
	# writing to output
	with open('docs/old.csv', 'r') as csvinput:
		with open('docs/result.csv', 'w') as csvoutput:
			writer = csv.writer(csvoutput, lineterminator='\n')
			reader = csv.reader(csvinput)
			# header
			alls = []
			row = next(reader)
			row.append('cap')
			alls.append(row)
			# values
			for row in reader:
				for r in input_array:
					national_code = r[1]
					if national_code == row[1]:
						row.append(r[0])
						break
				alls.append(row)
			writer.writerows(alls)
