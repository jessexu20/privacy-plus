import sys
import csv


def replace_url(inputFile, outputFile):
    fd = open(inputFile, 'r')
    wd = open(outputFile, 'w')
    occuCount = {}
    fd.readline()
    for line in fd:
        arr = line.split(',')
        if(len(arr) < 15):
            continue

        occuArr = arr[14].split('/ ')
        for occu in occuArr:
            if occu in occuCount:
                occuCount[occu] += 1
            else:
                occuCount[occu] = 1
    fd.close()
    print occuCount

    writer = csv.writer(wd)
    for key, value in occuCount.items():
        writer.writerow([key, value])
    wd.close()
if __name__ == '__main__':
    import sys
    replace_url(sys.argv[1], sys.argv[2])
