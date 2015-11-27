import csv
import sys


def merge(inputFile, outputFile):
    csv.field_size_limit(sys.maxsize)

    new_rows = []
    changes = {
        # org1 in newer_us.csv
        'newer_us.csv': {
            'University of California/ Berkeley': '0',
            'University of Life': '1',
            'University of Texas at Austin': '2',
            'Stanford University': '3',
            'University of California/ Los Angeles': '4',
            'University of Washington': '5',
            'Google': '6',
            'University of Michigan': '7',
            'Brigham Young University': '8',
            'New York University': '9'
        },
        # org1 in newer_ch.csv
        'newer_ch.csv': {
            'Stanford University': '0',
            'University of California/ Berkeley': '1',
            'University of California/ Los Angeles': '2',
            'Tsinghua University': '3',
            'Carnegie Mellon University': '4',
            'Harvard University': '5',
            'Google': '6',
            'National University of Singapore': '7',
            'Yale University': '8',
            'University of Pennsylvania': '9'
        },
        # org1 in newer_fr.csv
        'newer_fr.csv': {
            'Life': '0',
            'University of Texas at Austin': '1',
            'Stanford University': '2',
            'Boston University': '3',
            'Google': '4',
            'University of California/ Berkeley': '5',
            'University of Massachusetts Lowell': '6',
            'University of Oregon': '7',
            'University of Phoenix': '8',
            'Canadian Broadcasting Corporation': '9'
        },
        # org1 in newer_gr.csv
        'newer_gr.csv': {
            'Life': '0',
            'Stanford University': '1',
            'Google': '2',
            'Carnegie Mellon University': '3',
            'University of Michigan': '4',
            'University of California/ Berkeley': '5',
            'Michigan State University': '6',
            'New York University': '7',
            'University of Chicago': '8',
            'University of Southern California': '9'
        },
        # org1 in newer_jp.csv
        'newer_jp.csv': {
            'Waseda University': '0',
            'University of Tokyo': '1',
            'University of Washington': '2',
            'New York University': '3',
            'Stanford University': '4',
            'University of California/ Berkeley': '5',
            'University of California/ Los Angeles': '6',
            'Keio University': '7',
            'Kyoto University': '8',
            'Osaka University': '9'
        },
        # org1 in overall.csv
        'wh_overall_merged.csv': {
            'Life': '0',
            'University of California/ Berkeley': '1',
            'Stanford University': '2',
            'University of California/ Los Angeles': '3',
            'Google': '4',
            'University of Texas at Austin': '5',
            'University of Washington': '6',
            'New York University': '7',
            'Harvard University': '8',
            'University of Michigan': '9'
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
