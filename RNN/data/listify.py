import os
import sys
import csv

def read(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        dates, newonday, cumnewonday = [],[],[]
        for i in csvreader:
            dates.append(i[1])
            newonday.append(i[2])
            cumnewonday.append(i[3])
        return(dates[1:-2],newonday[1:-2],cumnewonday[1:-2])	

def parse():
    if (len(sys.argv)>1):
        filename = os.path.join('Counties',"{}.csv".format(sys.argv[1]))
        return read(filename)
    else:
        returndata = []
        for i in os.listdir('Counties'):
            filename = os.path.join('Counties',"{}".format(i))
            returndata.append((filename,read(filename)))
        return returndata

print parse()