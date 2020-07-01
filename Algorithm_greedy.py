# -*- coding:utf8 -*-
import json
import csv
import re
import os
import math
from clean_data import *

dir_path = os.path.dirname(os.path.realpath(__file__))

#global var

#ITMpath="./clean_data.csv"

#fn_pp_excel="./clean_data3.csv"
#
getTestCasesDetails_file="./micorarray.csv"
ITMpath="./micorarray_affected_clean_data.csv"
fn_pp_excel="./micorarray_clean_data.csv"
# #

# getTestCasesDetails_file="/Users/cheny39/Documents/GitHub/tmp/cedcd_c.csv"
# ITMpath="/Users/cheny39/Documents/GitHub/tmp/cedcd_affected_clean_data.csv"
# fn_pp_excel="/Users/cheny39/Documents/GitHub/tmp/cedcd_clean_data.csv"


# getTestCasesDetails_file="/Users/cheny39/Documents/tmp/tmp.csv"
# ITMpath="/Users/cheny39/Documents/tmp/tmp_affacted.csv"
# fn_pp_excel="/Users/cheny39/Documents/tmp/tmp.csv"

total_number_ppi =0

total_number_fn =0

count =0



def RiskFunction(selection,details_testsuit,affected_ppi,affected_pp):
    # get number of affected invariant
    # get number of affected fn
    tmp_Inv =[]
    tmp_fn=[]
    covered_fn=set()
    covered_ppi=set()
    for tc in range(len(selection)):
        if affected_ppi=="" or tc=="" or selection[tc]=="":
            continue;
        tmp_Inv=tmp_Inv+details_testsuit[selection[tc]]['affected_ppi']
        tmp_fn=tmp_fn+details_testsuit[selection[tc]]['affected_fn']
        # get covered fn
        covered_fn.add(tc)
        for i in range(len(details_testsuit[selection[tc]]['fn'])):
            fn=details_testsuit[selection[tc]]['fn'][i]
            att_fns = list(dic_cpp[fn]["attach"])
            for j in range(len(att_fns)):
                covered_fn.add(att_fns[j])
        for i in range(len(details_testsuit[selection[tc]]['ppi'])):
            fn = details_testsuit[selection[tc]]['ppi']

            for j in range(len(fn)):
                covered_ppi.add(fn[j])

    set_inv = set(tmp_Inv)
    set_fn = set(tmp_fn)
    uncovered_affected_fn_score = 1
    if (len(affected_pp) == 0):
        uncovered_affected_fn_score = 1
    else:
        uncovered_affected_fn_score = (len(affected_pp) - len(set_fn)) / float(len(affected_pp))

    uncovered_affected_inv_score = 1
    if (len(affected_ppi) == 0):
        uncovered_affected_inv_score = 1
    else:
        uncovered_affected_inv_score = (len(affected_ppi) - len(set_inv)) / float(len(affected_ppi))

    uncovered_fn_score = (len(pp)-len(covered_fn))/float(len(pp))

    uncovered_inv_score =(len(ppi)-len(covered_ppi))/float(len(ppi))
    # alg 1a
    #score = uncovered_affected_inv_score +uncovered_affected_fn_score
    # alg 1b
    #score = uncovered_affected_inv_score +uncovered_affected_fn_score +uncovered_fn_score
    # alg 1c
    #score = uncovered_affected_inv_score + uncovered_affected_fn_score + uncovered_inv_score



    #uncovered_fn_score
    #score = uncovered_affected_inv_score
    #score = uncovered_affected_fn_score
    #score = uncovered_inv_score
    #score = uncovered_fn_score
    #score = uncovered_affected_inv_score;
    score = uncovered_fn_score;
    return score


def costFunction(selection,details_testsuit):
    tmp_fn = 0
    count =1
    for tc in range(len(selection)):
        tmp_fn = tmp_fn + len(details_testsuit[selection[tc]]['ppi'])
    return tmp_fn


def ObjectFucntion(selection,tc,details_testsuit,affected_ppi,affected_pp):
    tmp_selection =[]
    tmp_selection.extend(selection)
    tmp_selection.append(tc)
    riskScore = RiskFunction(tmp_selection,details_testsuit,affected_ppi,affected_pp)
    costScore = costFunction(tmp_selection,details_testsuit)

    return math.pow(riskScore,2)+costScore/float(total_execution);


def getTestCasesDetails():
    #get ITM csv file
    details_testsuit ={}
    with open(getTestCasesDetails_file, "r+") as files:
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


def getTestCasesAffectDetails(details_testsuit):
    #get ITM csv file
    with open(ITMpath, "r+") as files:
        reader = csv.reader(files)
        header= next(reader)
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    #find testcase in dic add ppi and pp
                    details_testsuit[header[col]]['affected_ppi'].append(row[0]+"&ppi&"+row[1])
                    details_testsuit[header[col]]['affected_fn'].append(row[0])
    return details_testsuit



def getAffectedFunctions():
    pp = set()
    with open(ITMpath, "r+") as files:
        reader = csv.reader(files)
        header = next(reader)
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    pp.add(row[0])
    return pp

def getAffectedInvariants():
    ppi = set()
    with open(ITMpath, "r+") as files:
        reader = csv.reader(files)
        header= next(reader)
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    ppi.add(row[0]+row[1])
    return ppi

def callGraph(pp):
    list_pp = list(pp)
    dic_pp={}
    for i in range(len(list_pp)):
        dic_pp[list_pp[i]]={
            "attach":set()
        }

    with open(fn_pp_excel, "r+") as files:
        reader = csv.reader(files)
        header = next(reader)
        previous_row = [0] * (len(header)-2)
        previous_row_pp=""
        for row in reader:
            tmp_list =[]
            for col in range(2,len(header)):
                if(previous_row[col-2]=="1" and previous_row[col-2]==row[col]):
                    dic_pp[previous_row_pp]["attach"].add(row[0])
                    continue
            previous_row_pp=row[0]
            previous_row = row[2:]

    return dic_pp






def setAffectedITM(affeced_fns,affeced_ins):
    gpp = []
    with open(fn_pp_excel, "r+") as files:
        reader = csv.reader(files)
        gpp.append(next(reader))
        for row in reader:
            for col in range(2,len(row)):
                if row[col] == "1" and (row[0] in affeced_fns) :
                    row[col] = 1
                    continue
                if row[col] =="1":
                    flag = False;
                    for i in range(len(affeced_ins)):
                        if affeced_ins[i] in row[1]:
                            flag = True
                            continue
                    if flag:
                        row[col] =1
                    else:
                        row[col] =0
                    continue
                row[col] = 0
            gpp.append(row)

    with open(ITMpath, mode='w') as clean_file:
        writer = csv.writer(clean_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(gpp)):
            writer.writerow(gpp[i])




def Alg(details_testsuit,affected_ppi,affected_pp):
    # get details of a test cases.
    # number of affected invs, number of affected funs, running time.
    selection =[]
    selection_cost = []
    objective_score=[]
    risk_score=[]
    cost_score=[]
    global  budget
    total_cost =0

    while budget > total_cost:
        selected = ""
        tmp_cost = 99999
        for tc, tc_detils in details_testsuit.items():
            if tc not in selection:
                cost = ObjectFucntion(selection,tc,details_testsuit,affected_ppi,affected_pp)
                if cost<tmp_cost:
                    selected =tc
                    tmp_cost = cost

        selection.append(selected)
        # get object score of each selection
        objective_score.append(tmp_cost)
        # get risk score of each selection
        risk_score.append(math.pow(RiskFunction(selection,details_testsuit,affected_ppi,affected_pp),2))
        # get cost score of each selection
        cost_score.append(10*costFunction(selection,details_testsuit)/float(total_execution))

        total_cost=costFunction(selection,details_testsuit)
        # get total cost score of each selection
        selection_cost.append(total_cost)

    return  [selection,objective_score,risk_score,cost_score,selection_cost]


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
budget =0

#budgetSet = [437,874,1211,1784,2185,2622,3059,4370]

budgetSet = [1505,3010,4515,6020,7525,9030,10204,15050]

#budgetSet=[15050]

#total_execution = 222;

total_execution = 22115;

if __name__ == '__main__':

    for i in range(len(budgetSet)):
        budget = budgetSet[i]


        #setAffectedITM(["PUGTable.js.render"], ["api/analysis/runContrast","pathways_up"])

        #setAffectedITM(["PDGTable.js.render"], ["api/analysis/runContrast","pathways_up"])

        #setAffectedITM([""], ["api/analysis/runContrast"])


        #setAffectedITM([""], ["No Cancer"])
        #
        setAffectedITM([""],["./api/cohort/select","this.state.filter","filter"])

        pp = getProgramPoints(data_path) # this is og
        total_number_fn =len(pp)


        dic_cpp = callGraph(pp)   # clean data



        ppi = set()
        ppi = getProgramPointsInvariant(data_path)
        total_number_ppi = len(ppi)


        affected_ppi=set()
        affected_ppi=getAffectedInvariants();

        affected_pp=set()
        affected_pp=getAffectedFunctions();

        testsuit = set()
        testsuit=getTestSuit(data_path)
        print ("budget is  ")
        print  (budget)

        details_testsuit = getTestCasesDetails()
        details_testsuit =getTestCasesAffectDetails(details_testsuit)
        result =  Alg(details_testsuit,affected_ppi,affected_pp)
        print (result[0])
        print (result[1])
        print (result[2])
        print (result[3])
        print (result[4])
        print (len(result[0]))
        print ("===========================================")
