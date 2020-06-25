from Classes import ProgramInvariant,TestCase,Functions
import os
import sys
import argparse
import csv
import os

filePath="/Users/cheny39/Documents/tmp/"
result={}
out_filePath="/Users/cheny39/Documents/tmp/tmp.csv"
sys.stdout = open(out_filePath, 'w')

def loadInvariantToArrays(f):
    #print 'Loading Invariants from file: ' + fileName
    data = []
    ppts = []
    index = -1
    new_ppt = False
    ppt = None
    lineNum = 0
    while True:
        line = f.readline()
        lineNum += 1
        if line == '': # end of file
            break
        elif line == '\n':
            continue
        elif line.startswith("==="): # new program point
            new_ppt = True
            index += 1
        else:
            if new_ppt:
                new_ppt = False
                ppt = line.rstrip("\n\r")
                ppts.append(ppt)
                data.append([])
            else:
                if ppt:
                    data[index].append([lineNum, line.rstrip("\n\r")])
    f.close()
    return (ppts, data)

def loadInvariantToDict(f):
    #print 'Loading Invariants from file: ' + fileName
    data = {}
    new_ppt = False
    ppt = None
    while True:
        line = f.readline()
        if line == '': # end of file
            break
        elif line == '\n':
            continue
        elif line.startswith("==="): # new program point
            new_ppt = True
        else:
            if new_ppt:
                new_ppt = False
                ppt = line.rstrip("\n\r")
                if ppt not in data:
                    data[ppt] = []
            else:
                if ppt:
                    data[ppt].append([line.rstrip("\n\r")])
    f.close()
    return data


#replace double quotes " with two double quotes "", required by csv file format
def doubleQuotes(s):
    # maxLen = 8192
    # maxLen = 16384
    # maxLen = 24576
    # maxLen = 32000
    maxLen = 32700
    result = s
    countQuotes = result.count('"')
    if len(result) + countQuotes >= maxLen:
        result = result[:maxLen - 3 - countQuotes] + '###'
    result = result.replace('"', '""')
    result = result.replace("\r\n"," ")
    result = result.replace("\n"," ")
    return result





def getFiles():
    files = [f for f in os.listdir(filePath) if f.endswith('txt')]
    for f in files:
        if os.path.isfile(filePath+f):
             f2=open(filePath+f,"r+")
             merge(f2)



def toCSV3():
    DLMTR=","
    sys.stdout.write('"Program Points"{0}"Invariant"'.format(DLMTR))

    i=0
    files = [f for f in os.listdir(filePath)]
    for f in files:
        if f.endswith('txt'):
            f2 = open(filePath + f, "r+")
            local_in = loadInvariantToDict(f2)
            sys.stdout.write('{0}"{1}"'.format(DLMTR,f2.name))
        for key in result:
            'if the test case execute the function'
            if key in local_in:
                for item in  range(len(result[key])):
                    flag  = False
                    for local_item in range(len(local_in[key])):
                        if result[key][item][0] == local_in[key][local_item][0]:
                            flag=True
                    if flag:
                        result[key][item].append(1)
                    else:
                        result[key][item].append(0)
            else:
                'if the test case not execute the function'
                for item in range(len(result[key])):
                    result[key][item].append(0)
    sys.stdout.write("\n");
    for key in result:
        for item in range(len(result[key])):
            sys.stdout.write('"{1}"'.format(DLMTR, doubleQuotes(key)))
            for i in range(len(result[key][item])):
                if i ==0:
                    sys.stdout.write('{0}"{1}"'.format(DLMTR,doubleQuotes(result[key][item][i])))
                else:
                    sys.stdout.write('{0}"{1}"'.format(DLMTR, result[key][item][i]))
            sys.stdout.write("\n");



def merge(f2):
    data=loadInvariantToDict(f2)
    for key in data:
        if(key not in result):
            result[key]=data[key]
        else:
            for item in data[key]:
                if(item not in result[key]):
                    result[key].append(item)



def main():
    getFiles()
    toCSV3()


if __name__ == "__main__": main()