# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:36:14 2015

@author: Adil
"""


import numpy as np
#import mutual_info,time,pprint
from operator import itemgetter


def C(S):
    return len(S)

def F(S,V,y):
    f=[]
    FS=0.0
    FS_0=0.0
    #print 'y_len',len(y)
    for i in range(len(y)):
        temp=0.0
        for j in S:            
            temp+=V[j][i]
        f.append(temp)
    
    
    T=1.0/sum(y)
    
    for j in range(len(y)):
        if f[j]>=1:
            f[j]=1
        temp=y[j]*f[j]
        #if temp!=0:
            #print y[j],f[j]
        FS_0+=y[j]*f[j]
    
    #print sum(y)
    #print FS_0,S
    #print '---------------------------'
    #for j in range(len(y)):
    #    print f[j],y[j]
    
    FS=T*FS_0
    
    return FS
def readData1(fileName):
    with open(fileName,"r") as fp:

        data=[]
        d={}
        index=0
        #sindex=0
        for line in fp.readlines():
            #print tuple(line.split())
            #line=line.replace("\"","")
            line=[int(i) for i in line.split()]
            #print sum(line)
            data.append(line)
            d[index]=index
            #sindex+=1           
            index+=1    
                
            
    #data=data[34755:43011]        
    #print len(data[0])
    data=np.array(data)
    y=[]
    for j in range(len(data[0])):
        if sum(data[:,j])>=1:
            y.append(1)
        else:
            y.append(0)
        
    #print y,sum(y)
    return y,data,d    

   
def S_0(V,y,lambd1):
    S0=[]
    GScore_temp=-1000.0    
    inti_index=0
    t_l=[]
    gs_t=[]
    for i in range(len(V)):
        t_l[:]=[]        
        t_l.append(i)        
        tGS=GS(t_l,V,y,lambd1)
        print t_l ,tGS       
        gs_t.append(tGS)
        if tGS>GScore_temp:                        
            GScore_temp=tGS
            t_l.pop()
            inti_index=i
    print '>>#########',lambd1,'#########'
    S0.append(inti_index)
    #print 's0',tindex
    print S0,GScore_temp
    return S0,GScore_temp    
    
def GS(S,V,y,lambd1):
    #print 'S',S
    #print 'FS',F(S,V,y)
    #print 'C(S)',lambd*C(S)
    G=F(S,V,y)-lambd1*C(S)
    return round(G,4)
    
def cros_mat(S_c,S,cov):
    cros_Mat=np.zeros((len(S_c),len(S)))
    for q,i in enumerate(S_c):
        for k,j in enumerate(S):
            cros_Mat[q][k]=cov[i][j]
    return cros_Mat
    

    
    
def main():
    #dataFile="Data/chart/chart_raw.txt"
    #resultData="Data/chart/chart_Algo2_result2.txt"

    #dataFile="Data/time4/time4_raw.txt"
    #resultData="Data/time4/time4_Algo2_result2.txt"
    
    
    #dataFile="Data/lang2/lang_raw.txt"
    #resultData="Data/lang2/lang_Algo2_result2.txt"
    #dataFile="Data/time3_correct_withindex_data.txt"
    #resultData="Data/time3_correct_result.txt"
    t0=time.time()
    dataFile = "Data/batchAgent/batchAgent_data.txt"
    class_idF= "Data/batchAgent/class_id.txt"
    class_invF="Data/batchAgent/class_invariant.txt"
    class_classF="Data/batchAgent/class_class.txt"
    resultData = "Data/batchAgent/batchAgent_Algo2.txt"

    dataFile = "Data/time6/time6_data.txt"
    class_idF = "Data/time6/class_id.txt"
    class_invF = "Data/time6/class_invariant.txt"
    class_classF = "Data/time6/class_class.txt"
    resultData = "Data/time6/time6_Algo2.txt"

    dataFile = "Data/closure/closure_data.txt"
    class_idF = "Data/closure/class_id.txt"
    class_invF = "Data/closure/class_invariant.txt"
    class_classF = "Data/closure/class_class.txt" 
    resultData = "Data/closure/closure_Algo2.txt" #W
    
    dataFile = "Data/TIME/time_data_h.txt"
    class_idF = "Data/TIME/class_id.txt"
    class_invF = "Data/TIME/class_invariant.txt"
    class_classF = "Data/TIME/class_class.txt" 
    resultData = "Data/TIME/time_h_Algo2.txt" #W
    
#    dataFile = "Data/TIME/time_h_data.txt"
#    class_idF = "Data/TIME/class_id.txt"
#    class_invF = "Data/TIME/class_invariant.txt"
#    class_classF = "Data/TIME/class_class.txt" 
#    resultData = "Data/TIME/time_h_Algo2.txt" #W

    #y= t
    # d = index
    # v = data
    y,V,d=readData1(dataFile)
    rff=open(resultData,"w")
    #GV=[i for i in range(34)]
    lambd1=[i/10.0 for i in range(1,11)]
    lambd1=[i/100.0 for i in range(1,101,4)]

    print len(V)
    #lambd1=[0.1]
    #lambd2=[1]
    #S=[i for i in range(10,30)]
    #print 'M1  -  M2 = M'
    #for k in range(14):
    #    print M(S,GV,cov,k)
    #K=5
    SL=[]
    t0=time.time()
    BB=[int(r*len(V)) for r in [0.001]]
    for B in BB:
        for l1 in range(len(lambd1)):
            for l2 in range(1,2):
                GScore_temp=0.0
                #gs_t=[]
                tindex=0
                #t_l=[]
                S=[]
                S_t=[]
                print 'B=',B,"Lambda1=",lambd1[l1]
                for e in range(len(V)):
                        
                    if e not in S:
                        #print 'u=',u
                        
                        S_t.append(e)
                        #print S_t
                        
                        GScore_temp_e=GS(S_t,V,y,lambd1[l1])
                        GScore_temp=GS(S,V,y,lambd1[l1])
                        #print 'S',S,GScore_temp
                        #print 'S_t',S_t,GScore_temp_e
                        #time.sleep(0.11)
                        #time.sleep(1)
                        #print GScore_temp,GScore_temp_e 
                        if GScore_temp_e>=GScore_temp:
                            GS_t=GScore_temp_e
                            #tindex=e
                            S.append(e)
                        else:
                            S_t.remove(e)
                    
                    if len(S)>B:
                        break
                #SL.append((GS(S,V,y,lambd[lm]),S))
                #print 'B=',B,'>>>',F(S,V,y)
                #time.sleep(5)
                sS=[]
                print S,GS_t
                for iS in S:
                    sS.append(d[iS])
                SL.append((B,lambd1[l1],GS(S,V,y,lambd1[l1]),round(F(S,V,y),2),len(sorted(S)),sorted(sS)))
        
    print 'B lambda1 G(S) F(S) C(S) M(S)'
    SL=sorted(SL, key=itemgetter(2),reverse=True)
    print sS,
    rff.write("B lmbda1 lambda2 G(S) F(S) C(S) M(S)]\n")
    
    for ss in SL:
        rff.write(str(ss).replace("(","").replace(")","").replace(","," ")+"\n")        
    print 'done!!!!'#   print ss
    print time.time()-t0,' sec....'
    rff.close()

    print "selected Invariant By Algorithm",SL[0][5]
    class_id_dict={}
    with open(class_idF,"r") as c_idF:
        for line in c_idF.readlines():
            e=line.replace("\n","").split(" ")
            class_id_dict[e[1]]=int(e[0])
    N=len(class_id_dict)
    #print class_id_dict,len(class_id_dict)
    class_invar_List=[[] for i in range(N)]
    #print len(class_invar_List)
    
    with open(class_invF,"r") as c_i_F:
        for index,line in enumerate(c_i_F.readlines()):
            class_invar_List[class_id_dict[line.replace("\n","")]].append(index)
    
    edges=[]
    with open(class_classF,"r") as c_c_F:
        for line in c_c_F.readlines():
            e=line.replace("\n","").split()
            if e[0]!=e[1] and class_id_dict.has_key(e[0]) and class_id_dict.has_key(e[1]) :
                edges.append((class_id_dict[e[0]],class_id_dict[e[1]]))
    print len(edges)
    
    adjList=np.zeros((N,N))
    for e in edges:
        adjList[e[0]][e[1]]=1
        adjList[e[1]][e[0]]=1
        #pprint.pprint(adjList)
    #pprint.pprint(np.sum(adjList,axis=1))
    #B_I=BB
    B_C=N
    print SL[0][5]
    #S_star=SL[0][5]
    S_star=[]
    S_star.extend(SL[0][5])
    C_star=[]
    for i,c in enumerate(class_invar_List):
        for s in S_star:
            if s in c:
                C_star.append(i)
    C_star=list(set(C_star))
    
    print C_star
    sorted_degree=[]
    for i,deg in enumerate(adjList):
        sorted_degree.append((i,sum(deg)))
    #print sorted_degree
    sorted_degree=sorted(sorted_degree,key=lambda tup:tup[1],reverse=True) 
    print sorted_degree
    for degree in sorted_degree:
        if len(C_star)<=B_C  and degree[0] not in C_star:
            C_star.append(degree[0])
            iMax_deg=0
            temp_index=0
            for c in class_invar_List[degree[0]]:
                sum(V[c])
                if sum(V[c])>iMax_deg:
                    iMax_deg=sum(V[c])
                    temp_index=c
            #print temp_index,sum(V[temp_index]),V[temp_index]
            if sum(V[temp_index])!=0:
                S_star.append(temp_index)


    print "Invariant:",len(S_star),S_star
    print "class",len(C_star),C_star
    print time.time()-t0,"sec..."
    return 0
    '''-------- Index change to real indexing value------------ '''
    class_id_dict=[]
    with open("Data/lang2/class_id.txt","r") as c_idF:
            for line in c_idF.readlines():
                e=line.replace("\n","").split(" ")
                class_id_dict.append((e[0],e[1]))
    realClass_value=[]
    
    for class_id in C_star :
        print class_id_dict[class_id]
        realClass_value.append(class_id)
    print realClass_value
    
    invarianNo=[]
    with open("Data/lang2/invariantLineNo.txt","r") as c_idF:
            for line in c_idF.readlines():
                invarianNo.append(line.replace("\n",""))
    realInv_value=[]
    for ii in S_star :
        print invarianNo[ii]
        realInv_value.append(int(invarianNo[ii]))
    print realInv_value
    
if __name__ == '__main__':
    main()
        
            