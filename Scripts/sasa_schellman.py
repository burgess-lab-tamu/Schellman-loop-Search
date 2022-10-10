#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pymol
from pymol import cmd, stored
import numpy as np
import __main__
import pandas as pd
import sys
import datetime


# In[12]:


def hot_spot_sasa(csv_path, output):
    __main__.pymol_argv = [ 'pymol', '-qc']
    df = pd.read_csv(csv_path + '.csv')
    pdb_id = list(df.iloc[:,1])
    chain_id = list(df.iloc[:,2])
    start_id = list(df.iloc[:,3])
    loop_type = list(df.iloc[:,4])
    total = []
    for i in range(10):
        if i > 0 and i%50 == 0:
            df = pd.DataFrame(total)
            df.to_csv(output + '.csv')
        cmd.select('all')
        cmd.delete('all')
        oldDS = cmd.get("dot_solvent")
        cmd.set("dot_solvent", 1)
        cmd.load('PDB_10000_final/' + pdb_id[i] + '.pdb', 'test')
        cmd.remove('solvent')
        cmd.remove('ino.')
        cmd.remove('org.')
        count = 0
        resn = []
        if loop_type[i] == 'common':
	    area_complex_total = cmd.get_area('test & c. ' + chain_id[i], load_b = 1)
            area_complex = 0
            for j in range(6):
                area = cmd.get_area('test & c. ' + chain_id[i] + ' & resi %s' % (start_id[i] + j), load_b = 1)
                area_complex+= area
            cmd.extract('chA', 'test & c. ' + chain_id[i])
	    area_chain_total = cmd.get_area('chA & c. ' + chain_id[i], load_b = 1)
            area_single_chain = 0
            for j in range(6):
                area = cmd.get_area('chA & c. ' + chain_id[i] + ' & resi %s' % (start_id[i] + j), load_b = 1)
                area_single_chain+=area
            sasa_average = (area_chain_total - area_complex_total)/6
	    sasa_percentage = (area_single_chain - area_complex)/(area_chain_total - area_complex_total)
        if loop_type[i] == 'wide':
            area_complex_total = cmd.get_area('test & c. ' + chain_id[i], load_b = 1)
            area_complex = 0
            for j in range(7):
                area = cmd.get_area('test & c. ' + chain_id[i] + ' & resi %s' % (start_id[i] + j), load_b = 1)
                area_complex+=area
            cmd.extract('chA', 'test & c. ' + chain_id[i])
            area_chain_total = cmd.get_area('chA & c. ' + chain_id[i], load_b = 1)
            area_single_chain = 0
            for j in range(7):
                area = cmd.get_area('chA & c. ' + chain_id[i] + ' & resi %s' % (start_id[i] + j), load_b = 1)
                area_single_chain+=area
            sasa_average = (area_chain_total - area_complex_total)/7
	    sasa_percentage = (area_single_chain - area_complex)/(area_chain_total - area_complex_total)
        subdata = []
        subdata.append([pdb_id[i], chain_id[i], start_id[i], loop_type[i], sasa_average, sasa_percentage])
        #print(subdata)
        total.extend(subdata)
        cmd.select('all')
        cmd.delete('all')
        cmd.set("dot_solvent", oldDS)
    df = pd.DataFrame(total)
    df.to_csv(output + '.csv')


# In[11]:


if __name__== "__main__":
    hot_spot_sasa(sys.argv[1],sys.argv[2])

