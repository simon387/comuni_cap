import csv

# cap cf array, 2, 5
input_array = []


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

	print(len(input_array))

	with open('docs/old.csv', 'r') as csvinput:
		with open('docs/result.csv', 'w') as csvoutput:
			writer = csv.writer(csvoutput, lineterminator='\n')
			reader = csv.reader(csvinput)

			all = []
			row = next(reader)
			row.append('cap')
			all.append(row)

			for row in reader:
				for r in input_array:
					national_code = r[1]
					if national_code == row[1]:
						row.append(r[0])
						break

				all.append(row)

			writer.writerows(all)
