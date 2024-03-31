import statistics

def toFloats(data):
    for i in range (len(data)):
        data[i] = float(data[i])
    return data
try:
    with open('inputdata.txt', 'r') as inputfile:
        data = inputfile.read().splitlines()
        data = toFloats(data)
except:
    print("ERROR occured")
else:
    m = round(statistics.mean(data), 3)
    dev = round(statistics.stdev(data), 3)
try:
    with open('outputdata.txt', 'w', encoding = 'utf-8') as outputfile:
        outputfile.write('Μεσος ορος = ' + str(m) + '\n')
        outputfile.write('Τυπικη αποκλιση = ' +  str(dev) + '\n')
except:
    print("ERROR occured")
else:
    print("Copying of file ended")

