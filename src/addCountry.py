def addCountry(inputFile,outputFile,ch):
     fd = open(inputFile, 'r')
     wd = open(outputFile, 'w')
     line = fd.readline()
     s = line[0:len(line)-2] + "country,\n" 
     wd.write(s)
     for line in fd:
         s = line[0:len(line)-2] + ( "%s,\n" % ch) 
         wd.write(s)
     fd.closed
def merge(output, inputFile):
    number = len(inputFile)
    print "NUMBER OF FILES MERGED = %s" % number
    wd = open(output,'w')
    flag = True
    for x in inputFile:
        fd=open(x,'r')
        line = fd.readline()
        if flag:
            wd.write(line)
            flag = False
        for line in fd:
            wd.write(line)
        fd.closed
    wd.closed
# merge(1,2,3)
if __name__ == '__main__':
    import sys
    # addCountry(sys.argv[1],sys.argv[2],sys.argv[3])
    print sys.argv[2:]
    merge(sys.argv[1],sys.argv[2:])

