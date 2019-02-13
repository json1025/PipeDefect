import csv


def read_file(file):
    data = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        write_headers = True
        for row in csv_reader:
            if write_headers:
                for header in row:
                    data.append([header.strip()])
                write_headers = False
                continue
            i = 0
            for value in row:
                data[i].append(value.strip())
                i += 1
    return data


def write_file(destination_file, data):
    with open(destination_file, 'w') as new_file:
        for row in data:
            for value in row:
                new_file.write(value + ',')
            new_file.write('\n')
