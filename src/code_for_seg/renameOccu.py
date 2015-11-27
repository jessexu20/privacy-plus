import csv
import sys


def reOccu(inputFile, outputFile):
    csv.field_size_limit(sys.maxsize)

    new_rows = []

    changes = {
        #occu in overall.csv
        'wh_overall_renamed.csv': {
            'Software Developer': '0',
            'Photographer': '1',
            'Student': '2',
            'Writer': '3',
            'Entrepreneur': '4',
            'Journalist': '5',
            'Engineer': '6',
            'Artist': '7',
            'Attorney': '8',
            'Realtor': '9'
        }
    }

    # change the names of the input file and output file
    with open(inputFile, 'rb') as csv_toRead:
        reader = csv.reader(csv_toRead)
        for row in reader:
            new_row = row
            for key, value in changes[inputFile].items():
                new_row = [x.replace(key, value) for x in new_row]
            new_rows.append(new_row)

    with open(outputFile, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

if __name__ == '__main__':
    import sys
    reOccu(sys.argv[1], sys.argv[2])
