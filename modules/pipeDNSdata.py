# Tools for reading the DNS data of pipe flow located in './data/pipe_DNS/'
#
# Author: Saleh Rezaeiravesh, saleh.rezaeiravesh@manchester.ac.uk
#---------------------------------------------------------------------------
#
import numpy as np
import sys
import matplotlib.pyplot as plt


def dataReader_(dirName,fileName):
    """ 
    Read in  post-processed data of turbulent pipe flow.
    """
    dataBase={};

    F1=open(dirName+'/'+fileName,'r')

    ain=F1.readlines();
    ain_sep=[];
    for i in range(len(ain)):
        ain_sep.append(ain[i].split())

    dataBase.update({'uTau':float(ain_sep[3][3])})
    nu=float(ain_sep[4][3]);
    #ReTau=dataBase["uTau"]*1.0/nu;
    dataBase.update({'nu':nu})

    #iSkip: no of lines to skip from the beginning of the input file
    iSkip=8
    nR=len(ain_sep)-iSkip;  #n: no of data points in radial direction
    nVar=len(ain_sep[iSkip-2])-1;   #no of variables whose data written in the file

    #read profiles of the variables and make a dictionary out of them
    for i in range(nVar):
        temp=[]
        for j in range(nR):
           temp.append(float(ain_sep[iSkip+j][i]))
        temp=np.asarray(temp)   

        varName=str(ain_sep[iSkip-2][i+1])
        if varName=='1-r': varName='y'
        if varName in ['Ur','Ut','Uz','dUz/dy', 'P']: varName+='+'                  

        dataBase_new={varName:temp}
        dataBase.update(dataBase_new)
    return dataBase
#

#external functions
def readMain(Re):
    """
    Read pipe DNS data at Reynolds number `Re`
    Acceptable `Re`=[550,1000,2000,5200]
    """
    if Re not in [550,1000,2000,5200]:
       raise ValueError("Invalid Reynolds number! Re should be: 550, 1000, 2000, and 5200.") 

    Restr={'550':'550','1000':'1K','2000':'2K','5200':'5K'}

    fileName='PIPE_Re'+Restr[str(Re)]+'_MEAN.dat'

    db=dataReader_('./data/pipe_DNS/',fileName)   #for calling from notebooks
    #db=dataReader_('../data/pipe_DNS/',fileName)   #for calling directly here
    db.update({'Re':Re})
    db.update({'Uz':db['Uz+']*db['uTau']/0.5})  #According to Jie Yao: Ub=0.5

    #print(db.keys())   
    #print(db['Re'])
    #print(db['uTau'])
    #print(db['nu'])
    #plt.semilogx(db['y+'],db['Uz'])
    #plt.show()

    return db

def read():
    """
    Construct a database of the turbulent pipe flow QoIs required for the wall functions.
    This function can be directly called in the notebooks and returns databse at all available Reynolds numbers.
    """
    db={}
    for Re_ in [550,1000,2000,5200]:
        db_=readMain(Re_)
        db1={'Re':Re_,'y':db_['y'],'y+':db_['y+'],'uTau':db_['uTau'],'Uz':db_['Uz'],'Uz+':db_['Uz+']}

        db.update({'Re'+str(Re_):db1})
    return db    
