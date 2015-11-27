import csv
import sys


def merge(inputFile, outputFile):
    csv.field_size_limit(sys.maxsize)

    new_rows = []
    changes = {
        # place1 in newer_us.csv
        'Tnewer_us.csv': {
            'New York': '0',
            'San Francisco': '1',
            'Los Angeles': '2',
            'London': '3',
            'Chicago': '4',
            'Seattle': '5',
            'Atlanta': '6',
            'Austin/ TX': '7',
            'San Diego': '8',
            'USA': '9',
        },
        # place1 in newer_ch.csv
        'Tnewer_ch.csv': {
            'Beijing': '0',
            'San Francisco': '1',
            'Singapore': '2',
            'New York': '3',
            'Shanghai': '4',
            'Los Angeles': '5',
            'Taipei': '6',
            'Seattle': '7',
            'Hong Kong': '8',
            'Chicago': '9'
        },
        # place1 in newer_fr.csv
        'Tnewer_fr.csv': {
            'Paris': '0',
            'San Francisco': '1',
            'France': '2',
            'Montreal': '3',
            'New York': '4',
            'Los Angeles': '5',
            'London': '6',
            'Washington/ DC': '7',
            'USA': '8',
            'Boston': '9'
        },
        # place1 in newer_fr.csv
        'Tnewer_gr.csv': {
            'San Francisco': '0',
            'Berlin': '1',
            'New York': '2',
            'Los Angeles': '3',
            'Seattle': '4',
            'Hamburg': '5',
            'Chicago': '6',
            'Austin/ TX': '7',
            'Germany': '8',
            'Washington/ DC': '9'
        },
        # place1 in newer_gr.csv
        'Tnewer_jp.csv': {
            'Tokyo': '0',
            'New York': '1',
            'San Francisco': '2',
            'Los Angeles': '3',
            'Seattle': '4',
            'Japan': '5',
            'Kawasaki': '6',
            'California': '7',
            'Chicago': '8',
            'Osaka': '9'
        },
        # place1 in overall.csv
        'Twh_overall_merged.csv': {
            'New York': '0',
            'San Francisco': '1',
            'Los Angeles': '2',
            'London': '3',
            'Seattle': '4',
            'Chicago': '5',
            'Tokyo': '6',
            'Atlanta': '7',
            'Austin/ TX': '8',
            'San Diego': '9'
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
    merge(sys.argv[1], sys.argv[2])
