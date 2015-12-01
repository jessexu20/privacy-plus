def calculate(inputFile):
    fd = open(inputFile, 'r')
    # wd = open(outputFile, 'w')
    title = fd.readline().split(',')
    pb = []
    pab = []
    for _ in range(28):
        pb.append(0)
        pab.append(0)
    for line in fd:
        arr = line.split(',')
        if(len(arr)!=28):
            continue
        for i in range(len(arr)):
            if(arr[i]!=' '):
                pb[i]=pb[i]+1;
                if(float (arr[27])>=0.64):
                    pab[i]= pab[i]+1
    fd.closed
    pro=[]
    for i in range(len(pb)):
        if(pb[i]==0):
            pro.append(0)
        else:
            pro.append(float(pab[i])/float(pb[i]))
    # print pb
    dic = {}
    for i in range(len(title)):
        dic[title[i]] = pro[i]
    for i in range(len(title)):
        print i, title[i]
    import operator
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    sorted_dic.reverse()
    print sorted_dic
def calculateTwo(inputFile):
    selected = [20,19,17,22,21,3,16,14]
    fd = open(inputFile, 'r')
    title = fd.readline().split(',')
    t = []
    pb = []
    pab = []
    for _ in range(28):
        pb.append(0)
        pab.append(0)
    pb = {}
    pab = {}
    for line in fd:
        arr = line.split(',')
        if(len(arr)!=28):
            continue
        for i in range(len(selected)):
            for j in range(i+1,len(selected)):
                name_set = {title[selected[i]],title[selected[j]]}
                if name_set not in t:
                    t.append(name_set)
                    name = ""
                    for x in name_set:
                        name+=(' '+ x)
                    pb[name] = 0
                    pab[name] = 0
                if(arr[selected[i]]!=' ' and arr[selected[j]]!=' '):
                    name_set = {title[selected[i]],title[selected[j]]}
                    name = ""
                    for x in name_set:
                        name+=(' '+ x)
                    pb[name] +=1
                    if(float (arr[27])>=0.64):
                        pab[name]+=1
    fd.closed
    pro = {}
    for key in pb.keys():
        if(pb[key]!=0):
            pro[key] = float(float(pab[key])/float(pb[key]))
    import operator
    sorted_dic = sorted(pro.items(), key=operator.itemgetter(1))
    sorted_dic.reverse()
    print sorted_dic,len(sorted_dic)
def reverseCal(inputFile):
    fd = open(inputFile, 'r')
    title = fd.readline().split(',')
    count = 0;
    count2 = 0;
    counter = []
    counter_2 = []
    for _ in range(26):
        counter.append(0)
        counter_2.append(0)
    for line in fd:
        arr = line.split(',')
        # print arr[27]
        if(len(arr)!=28):
            continue
        if(float (arr[27])>=0):
            count+=1
            for i in range(26):
                if(arr[i]!=' '):
                    counter[i]+=1
        if(float (arr[27])>=0.64):
            count2+=1
            for i in range(26):
                if(arr[i]!=' '):
                    counter_2[i]+=1
    dic = {}
    for i in range(26):
        counter[i] = (float)(float(counter[i])/count)
    for i in range(26):
        counter_2[i] = (float)(float(counter_2[i])/count2)
    print counter
    print counter_2
    for i in range(len(counter)):
        if(counter[i]==0):
            counter[i] = 100
        # dic[title[i]] = float((counter_2[i] - counter[i]))/counter[i]
        dic[title[i]] = float(float(counter[i])/count)
    # for i in range(len(title)):
#         print i, title[i]
    import operator
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    sorted_dic.reverse()
    print sorted_dic
            
if __name__ == '__main__':
    import sys
    reverseCal(sys.argv[1])
    # calculateTwo(sys.argv[1])