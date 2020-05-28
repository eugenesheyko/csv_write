import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            print('Column names are %s'%", ".join(row))
            #print('Column names are {}'.format(", ".join(row)))
            line_count += 1
        #print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        print('\t{} works in the {} department, and was born in {}.'.format(join(row)))
        line_count += 1
    print(f'Processed {line_count} lines.')