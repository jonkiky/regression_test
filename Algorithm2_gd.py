# -*- coding:utf8 -*-
import numpy as np
from clean_data import *

dir_path = os.path.dirname(os.path.realpath(__file__))

#global var
getTestCasesDetails_file="./micorarray.csv"
affected_ITM="./micorarray_affected_clean_data.csv"
fn_pp_excel="./micorarray_clean_data.csv"


"""
 t=[0,1] 0: not be selected. 1: selected. 
 F(t) = Risk(t) + ratio * Cost(t)
 Risk(t) = risk1*(1-t1)+risk2*(1-t2)+....+riskn*(1-tn)
 risk = ratio1 * (modified_Function / all_function )
          + ratio2 * (affected_program_invariant / all_program_invarialt)
 Cost(t) = (# of function )*t1+(# of function )*t2+(# of function )*t2....(# of function )*tn

 derivative F on t : [# of fn - risk]

    t(i+1) = t(i) - learning_step * [# of fn - risk]

 threshold: 0.5   - if t(i) >= 0.5 then t(i) = 1.
 learning_step : 0.632
 Convergence : F(t(i+1)) - F(t(i)) <= 0.01
 supp(t) = get non-zero ts
"""

threshold = 1

learning_step = 0.632

convergence = 0.08

risk_ratio = 0.5

def alg(t,number_of_functions_of_each_test,risk_of_each_test_input):

    while True:
        # t(i+1) = t(i) + learning_step * [# of fn - risk]
        d = [learning_step * x for x in np.subtract(number_of_functions_of_each_test,risk_of_each_test_input)]
        t_next =np.add(d,t)
        t_obj =objectivesFunction(t,risk_of_each_test_input,number_of_functions_of_each_test)
        t_next_obj = objectivesFunction(t_next,risk_of_each_test_input,number_of_functions_of_each_test)
        diff = t_next_obj-t_obj

        # Convergence
        print (diff)
        if 0<=diff<convergence:
            return supp(t_next)
        t = t_next



def supp(t):
    output =[]
    for j in range(len(t)):
        if t[j]>threshold:
            output.append(1)
        else:
            output.append(0)

    return  output


def objectivesFunction(t,risk_of_each_test_input,number_of_functions_of_each_test):

    t =  supp(t)

    # Risk function

    Fn_Risk = np.dot(([1 - x for x in t]), risk_ratio * np.array(risk_of_each_test_input)) / len(t)

    # cost function

    Fn_Cost = np.dot(t, number_of_functions_of_each_test) / len(t)

    # Objective function

    Fn_Obj_value = Fn_Risk + Fn_Cost

    return Fn_Obj_value


def risk_of_each_test(details_testsuit):
    '''risk = ratio1 * (modified_Function / all_function)
    + ratio2 * (affected_program_invariant / all_program_invarialt)'''

    ratio1 = 1
    ratio2 = 1
    output=[]
    for tc in details_testsuit.items():
        tc=tc[1]
        # modified_Function / all_function
        if(len(tc['affected_fn']))>0:
            print (1)
        mf = len(tc['affected_fn'])/len(tc['fn'])
        mInv =len(tc['affected_ppi'])/len(tc['ppi'])
        output.append(ratio1*mf+ratio2*mInv)
    return output

def cost_of_each_test(details_testsuit):
    # get avg # of fns of a test
    total_fns =0
    for tc in details_testsuit.items():
        tc = tc[1]
        total_fns = total_fns +len(tc['fn'])
    avg = total_fns/ len(details_testsuit.items())

    output = []
    for tc in details_testsuit.items():
        tc = tc[1]
        output.append(len(tc['fn'])/avg)
    return output



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
    # get ITM csv file
    details_testsuit = {}
    with open(fn_pp_excel, "r+") as files:
        reader = csv.reader(files)
        header= next(reader)
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    if header[col] not in details_testsuit:
                        details_testsuit[header[col]]= {
                            'ppi': [],
                            'fn': [],
                            'affected_fn': [],
                            'affected_ppi': []
                        }
                    #find testcase in dic add ppi and pp
                    details_testsuit[header[col]]['ppi'].append(row[0]+"&ppi&"+row[1])
                    details_testsuit[header[col]]['fn'].append(row[0])
    return details_testsuit


def getTestCasesAffectDetails(details_testsuit):
    #get ITM csv file
    with open(affected_ITM, "r+") as files:
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
    with open(affected_ITM, "r+") as files:
        reader = csv.reader(files)
        header = next(reader)
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    pp.add(row[0])
    return pp

def getAffectedInvariants():
    ppi = set()
    with open(affected_ITM, "r+") as files:
        reader = csv.reader(files)
        header= next(reader)
        for row in reader:
            for col in range(len(header)):
                if(row[col]=='1'):
                    ppi.add(row[0]+row[1])
    return ppi




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

    with open(affected_ITM, mode='w') as clean_file:
        writer = csv.writer(clean_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(gpp)):
            writer.writerow(gpp[i])



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




if __name__ == '__main__':

    testsuit = set()

    testsuit = getTestSuit(data_path)


    # case 2
    setAffectedITM([""], ["./api/cohort/select", "this.state.filter", "filter"])

    pp = getProgramPoints(data_path)
    total_number_fn = len(pp)

    dic_cpp = callGraph(pp)

    ppi = set()
    ppi = getProgramPointsInvariant(data_path)
    total_number_ppi = len(ppi)

    affected_ppi = set()
    affected_ppi = getAffectedInvariants();

    affected_pp = set()
    affected_pp = getAffectedFunctions();

    #details_testsuit = getTestCasesDetails()
    details_testsuit =getTestCasesDetailsFromITM()
    details_testsuit = getTestCasesAffectDetails(details_testsuit)


    # variables
    number_of_tests = len(details_testsuit.items())

    # tests vector
    t = [0] * number_of_tests

    risk_of_each_test_input = risk_of_each_test(details_testsuit)

    number_of_functions_of_each_test = cost_of_each_test(details_testsuit)



    print (alg(t,number_of_functions_of_each_test,risk_of_each_test_input))
