#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:22:50 2019

@author: lidong
"""
##extract the same Gene codes from multiple columns for xiaoxi
from pandas import DataFrame
from sklearn import linear_model
import Tkinter as tk 
import statsmodels.api as sm
import os
import numpy as np
# =============================================================================
# input data
# =============================================================================
root ='/Users/lidong/Downloads/extract-common-genecodes-master'
filename='Target for 30c and 10b.csv'
#filename='Target for 30c and 10b_sheet2.csv'

filenamefull=os.path.join(root,filename)
Data=np.genfromtxt(filenamefull,delimiter=';',skip_header=0, dtype='str')
Data=Data[:,]
Col1=Data[1:,0]
Col2=Data[1:,1]
Col3=Data[1:,2]

# =============================================================================
# extract the common genecode from three columns (data sets)
# =============================================================================
#nD = Col1.size
#
#for i in range(nD):
#    select_filter=(Col3==Col1[i])
#    Sheet1_common=Col2[select_filter]
#    if Sheet1_common.size>0:####if Sheet1_common is not blank then print it.
#        print(Sheet1_common)
##Note this is wrong because it corespoding to the sequence of the lists.
# =============================================================================
# extract
# =============================================================================

#def common_member(Col1_set, Col2_set,Col3_set): 
#    Col1_set = set(Col1) 
#    Col2_set = set(Col2)
#    Col3_set = set(Col3)
#    if (Col1_set & Col2_set & Col3_set)>0: 
#        print(Col1_set & Col2_set & Col3_set) 
#    else: 
#        print("No common elements")  
#           
#   
#common_member(Col1, Col2, Col3) 


# =============================================================================
# 
# =============================================================================
   
Col1_set = set(Col1) 
Col2_set = set(Col2)
Col3_set = set(Col3)
if (Col1_set & Col2_set & Col3_set)>0: 
    ex_data=Col1_set & Col2_set & Col3_set
else: 
    print("No common elements")  
           
   


