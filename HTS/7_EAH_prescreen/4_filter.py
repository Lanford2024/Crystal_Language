#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Hang Xiao 2023.04
# xiaohang007@gmail.com
import os,sys,glob

ehull=0.1

pwd=os.getcwd()
with open("results_"+pwd.split("/")[-1]+"filtered_"+str(ehull)+"eV.csv",'w') as result:
    result.write("index,SLICES,POSCAR,formula,energy_per_atom,energy_per_atom_sym,space_group_number,dissimilarity,energy_above_hull_prescreen\n")


result_filtered_csv=''
with open("results_7_EAH_prescreen.csv",'r') as result:
    for i in result.readlines()[1:]:
        if  0.05 <float(i.split(',')[-1]) <= ehull:
            result_filtered_csv+=i
        

with open("results_"+pwd.split("/")[-1]+"filtered_"+str(ehull)+"eV.csv",'a') as result:
    result.write(result_filtered_csv)


                
                
                
                
