import csv
import sys
def merge(inputFile,outputFile):
    csv.field_size_limit(sys.maxsize)

    new_rows = []
    changes = {
        'San Francisco/ CA' : 'San Francisco',
        'Los Angeles/ CA' : 'Los Angeles',
        'San Diego/ CA' : 'San Diego',
        'Seattle/ WA' : 'Seattle',
        'Boston/ MA' : 'Boston',
        'Houston/ TX' : 'Houston',
        'Houston Texas' : 'Houston',
        'Atlanta/ Georgia' : 'Atlanta',
        'Atlanta/ GA' : 'Atlanta',
        'New York City' : 'New York',
        'New York/ NY' : 'New York',
        'Chicago/ IL' : 'Chicago',
        'London/ England' : 'London',
        'Paris/ France' : 'Paris',
        'paris' : 'Paris',
        'Tokyo/ Japan': 'Tokyo',
        'tokyo': 'Tokyo',
        'Beijing/ China' : 'Beijing',
        'Shanghai/ China' : 'Shanghai',
        'Taipei/ Taiwan' : 'Taipei',
        'UCLA' : 'University of California/ Los Angeles',
        'UC Berkeley' : 'University of California/ Berkeley',
        'University of Life' : 'Life'

    }

    #change the names of the input file and output file
    with open(inputFile, 'rb') as csv_toRead:
        reader = csv.reader(csv_toRead)
        for row in reader:
            new_row = row
            for key, value in changes.items():
                new_row = [ x.replace(key, value) for x in new_row ]
            new_rows.append(new_row)

    with open(outputFile, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)
    
if __name__ == '__main__':
    import sys
    merge(sys.argv[1],sys.argv[2])