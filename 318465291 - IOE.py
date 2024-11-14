#Daniel Tugendhaft 318465291
#Program_7 - IOExceptions.py:


####Q1

##def copy_no_comments(source,target):
##    f = open(source,'r')
##    nf = open(target,'w')
##    for line in f:
##        if line[0] != '#':
##            nf.write(line)
##    f.close()
##    nf.close()
##
##        
##sourceName = 'source1.txt'
##targetName = 'target1.txt'
##copy_no_comments(sourceName, targetName)




####Q2

##def csv_reader(source):
##    counter = []
##    File = open(source,'r')
##    for line in File:
##        line = line.rstrip()
##        line = line.split(',')
##        for i in range(len(line)):
##            line[i] = int(line[i])
##        counter.append(sum(line))
##    return counter
##            
##
##
##source2 = 'source2.csv'
##res = csv_reader(source2)




####Q3

def ConvertToNum(num):
    try:
        num = float(num)
        return 'result of conversion:  ' + str(num)
    except ValueError:
        print('cannot convert \"', num ,'\" string to a number.')
        print('result of conversion:',end='  ')

num = ConvertToNum('5')
print(num)

num = ConvertToNum('some text')
print(num)

