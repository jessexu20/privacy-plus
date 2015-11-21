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
if __name__ == '__main__':
    import sys
    addCountry(sys.argv[1],sys.argv[2],sys.argv[3])

