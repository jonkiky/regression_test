# -*- coding:utf8 -*-
import json
import csv
import re
import os
import math
from clean_data import *
dir_path = os.path.dirname(os.path.realpath(__file__))


getTestCasesDetails_file="./micorarray.csv"
affected_ITM="./micorarray_affected_clean_data.csv"
fn_pp_excel="./micorarray_clean_data.csv"


def getTestCasesDetailsFromITM():
    #get ITM csv file
    details_testsuit ={}
    with open(fn_pp_excel, "r+") as files:
        reader = csv.reader(files)
        for row in reader:
            #find testcase in dic add ppi and pp
            if row[2] not in details_testsuit:
                details_testsuit[row[2]] = {
                         'ppi': [],
                         'fn': [],
                         'affected_fn': [],
                         'affected_ppi': []
                }

            details_testsuit[row[2]]['ppi'].append(row[1]+"."+row[0]+"&ppi&"+row[3])
            details_testsuit[row[2]]['fn'].append(row[1]+"."+row[0])
    return details_testsuit

def getAllFiles(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f)) if f.endswith('txt')]
    #print onlyfiles
    return onlyfiles


if __name__ == '__main__':
    getTestCasesDetailsFromITM()