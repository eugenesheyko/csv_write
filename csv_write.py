import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are %s'%", ".join(row))
            line_count += 1
        print('\t'+row['name']+'works in the '+row['department']+', and was born in '+row['birthday month'])
        line_count += 1
    print('Processed {} lines.'.format(line_count))
