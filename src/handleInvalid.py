def handle(inputFile,outputFile):
     fd = open(inputFile, 'r')
     wd = open(outputFile, 'w')
     wd.write(fd.readline())
     for line in fd:
         arr = line.split(',')
         if(len(arr)<8):
             continue
         if(arr[8]!="" and arr[8].find("male")!=-1):
             wd.write(line)
     fd.closed
if __name__ == '__main__':
    import sys
    handle(sys.argv[1],sys.argv[2])

