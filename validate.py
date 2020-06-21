# -*- coding:utf8 -*-
import json
import csv
import re
import os
import math
from clean_data import *
dir_path = os.path.dirname(os.path.realpath(__file__))

#global var

ITMpath="./clean_data3.csv"

fn_pp_excel="./clean_data.csv"
total_number_ppi =0

total_number_fn =0

count =0




def getTestCasesDetails():
    #get ITM csv file
    details_testsuit ={}
    with open(fn_pp_excel, "r+") as files:
        reader = csv.reader(files)
        header= reader.next()
        #init  dic of details_testsuit { testcase : { 'ppi':[],'fn':[]}}
        for col in range(len(header)):
            if col >1:
                details_testsuit[header[col]]={
                    'ppi':[],
                    'fn':[],
                    'affected_fn':[],
                    'affected_ppi':[]
                }
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    #find testcase in dic add ppi and pp
                    details_testsuit[header[col]]['ppi'].append(row[0]+"&ppi&"+row[1])
                    details_testsuit[header[col]]['fn'].append(row[0])
    return details_testsuit




# dic_cpp ={ pp : { set : [pp]}}
dic_cpp = {}

pp = set()

# 10%
#budget = 2655
# 5%
#budget = 1327
# 15%
#budget = 3981

# 20%
#budget = 5308

# 25
#budgetSet =[11917,13290]

budgetSet = [1327,2655,3981,5308,6635,11917,13290]

total_execution = 26555

if __name__ == '__main__':

    affected_ppi=["kf6.ikit.org"]
    affected_fn=[]
    details_testsuit = getTestCasesDetails()
    selection = []
    selection1=['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29', 't28', 't27', 't16', 't19', 't14', 't17', 't4']
    for tc, tc_detils in details_testsuit.iteritems():
       for i in range(len(affected_fn)):
           for j in range(len(tc_detils["fn"])):
               if affected_fn[i] in tc_detils["fn"][j]:
                   selection.append(tc)
                   continue
       for i in range(len(affected_ppi)):
           for j in range(len(tc_detils["ppi"])):
               if affected_ppi[i] in tc_detils["ppi"][j]:
                   selection.append(tc)
                   continue
    print(selection)
    print("selection1")
    print(len(selection1))
    print(len(selection))

    print (list(set(selection1).intersection(selection)))
    print(len(list(set(selection1).intersection(selection))))
    selection2 =['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29', 't28', 't27', 't16', 't19', 't14', 't17', 't4', 't20', 't68', 't1', 't105', 't23', 't22', 't25', 't24', 't97', '223', '222', 't188', 't98', 't99', 't176', 't177', 't178']
    print("selection2")
    print(len(selection2))
    print(len(selection))

    print(list(set(selection2).intersection(selection)))
    print(len(list(set(selection2).intersection(selection))))

    selection2 =['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29',
     't28', 't27', 't16', 't19', 't14', 't17', 't4', 't20', 't68', 't1', 't105', 't23', 't22', 't25', 't24', 't97',
     '223', '222', 't188', 't98', 't99', 't176', 't177', 't178', 't179', '225', 't183', 't182', 't184', '211', 't2',
     '203', 't94', '224', '221']
    print("selection3")
    print(len(selection2))
    print(len(selection))

    print(list(set(selection2).intersection(selection)))
    print(len(list(set(selection2).intersection(selection))))

    selection2 =['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29',
     't28', 't27', 't16', 't19', 't14', 't17', 't4', 't20', 't68', 't1', 't105', 't23', 't22', 't25', 't24', 't97',
     '223', '222', 't188', 't98', 't99', 't176', 't177', 't178', 't179', '225', 't183', 't182', 't184', '211', 't2',
     '203', 't94', '224', '221', '204', '213', 't95', 't90', 't21', 't181', 't101']

    print("selection4")
    print(len(selection2))
    print(len(selection))

    print(list(set(selection2).intersection(selection)))
    print(len(list(set(selection2).intersection(selection))))

    selection2 = ['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29', 't28', 't27', 't16', 't19', 't14', 't17', 't4', 't20', 't68', 't1', 't105', 't23', 't22', 't25', 't24', 't97', '223', '222', 't188', 't98', 't99', 't176', 't177', 't178', 't179', '225', 't183', 't182', 't184', '211', 't2', '203', 't94', '224', '221', '204', '213', 't95', 't90', 't21', 't181', 't101', 't100', 't102', 't108', 't171', 't155', 't89']


    print("selection5")
    print(len(selection2))
    print(len(selection))

    print(list(set(selection2).intersection(selection)))
    print(len(list(set(selection2).intersection(selection))))

    selection2 =['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29', 't28', 't27', 't16', 't19', 't14', 't17', 't4', 't20', 't68', 't1', 't105', 't23', 't22', 't25', 't24', 't97', '223', '222', 't188', 't98', 't99', 't176', 't177', 't178', 't179', '225', 't183', 't182', 't184', '211', 't2', '203', 't94', '224', '221', '204', '213', 't95', 't90', 't21', 't181', 't101', 't100', 't102', 't108', 't171', 't155', 't89', 't88', 't86', 't145', 't33', '206', 't70', 't91', 't69', 't61', 't60', 't63', 't62', 't78', '216']


    print("selection6")
    print(len(selection2))
    print(len(selection))

    print(list(set(selection2).intersection(selection)))
    print(len(list(set(selection2).intersection(selection))))

    selection2 = ['t195', 't5', 't6', 't26', 't15', 't13', 't32', 't7', 't10', 't12', 't30', 't31', 't18', 't8', 't9', 't3', 't29', 't28', 't27', 't16', 't19', 't14', 't17', 't4', 't20', 't68', 't1', 't105', 't23', 't22', 't25', 't24', 't97', '223', '222', 't188', 't98', 't99', 't176', 't177', 't178', 't179', '225', 't183', 't182', 't184', '211', 't2', '203', 't94', '224', '221', '204', '213', 't95', 't90', 't21', 't181', 't101', 't100', 't102', 't108', 't171', 't155', 't89', 't88', 't86', 't145', 't33', '206', 't70', 't91', 't69', 't61', 't60', 't63', 't62', 't78', '216', '205', '210', '209']


    print("selection6")
    print(len(selection2))
    print(len(selection))

    print(list(set(selection2).intersection(selection)))
    print(len(list(set(selection2).intersection(selection))))