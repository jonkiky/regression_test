# -*- coding:utf8 -*-
import json
import csv
import re
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#data_path  = "/Users/cheny39/Documents/GitHub/tmp/cedcd.csv"
#
#data_path  = "./monitor.csv"
#data_path = "./micorarray-og.csv"
data_path ="./monitor.csv"
# data_path="/Users/cheny39/Documents/tmp/tmp.csv"

def getProgramPoints(path):
    pp = set()
    with open(path,"r+", encoding="utf8", errors='ignore') as files:
        reader = csv.reader(files)
        for row in reader:
           pp.add(row[2]+"."+row[3])
    return pp


def getProgramPointsInvariant(path):
    ppi = set()
    with open(path,"r+" ,encoding="utf8", errors='ignore') as files:
        reader = csv.reader(files)
        for row in reader:
           ppi.add(row[2]+"."+row[3]+"&pp&"+row[1])
    return ppi

def getTestSuit(path):
    pp = set()
    with open(path,"r+",encoding="utf8", errors='ignore') as files:
        reader = csv.reader(files)
        for row in reader:
           pp.add(row[5])
    return pp


def generateITM(path,ppi,pp,testsuit):
    # create ITM invariant tracebility matrix
    list_ppi =  list(ppi)
    list_ts = list(testsuit)
    ITM = [0]*len(ppi)
    for i in range(len(ppi)):
        ITM[i] = [0] * len(testsuit)
    with open(path, "r+",encoding="utf8", errors='ignore') as files:
        reader = csv.reader(files)
        for row in reader:
            index_ppi = list_ppi.index(row[2]+"."+row[3]+"&pp&"+row[1])
            index_ts =list_ts.index(row[5])
            ITM[index_ppi][index_ts]=1

    with open('./itm_clean_data.csv', mode='w') as clean_file:
        writer = csv.writer(clean_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ["program point","program invariant"]+list_ts
        #print(header)
        writer.writerow(header)
        for i in range(len(ppi)):
            row =[list_ppi[i].split('&pp&')[0],list_ppi[i].split('&pp&')[1]]+ITM[i]
            writer.writerow(row)



if __name__ == '__main__':
    'get all program point'
    pp = set()
    pp = getProgramPoints(data_path)
    print ("Program point")
    print(len(pp))

    testsuit = set()
    testsuit=getTestSuit(data_path)
    print("testsuit")
    print(len(testsuit))

    ppi = set()
    ppi = getProgramPointsInvariant(data_path)
    print("program ppi")
    print(ppi)

    generateITM(data_path,ppi,pp,testsuit)