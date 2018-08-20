# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 21:06:52 2018

@author: Mushtaq Shaikh
Read all the fixed length files in a given directory, interpret those by reading the Extract Layout
defined and load it into a Spreadsheet
"""

import pandas as pd
import os,fnmatch
import logging

def WritePLAtoExcel(Metadata_File,Metadata,Data_File,OutFile):

    df=pd.read_excel(Metadata_File,Metadata,skiprows=2)
    
    list_col_names=[]
    list_widths=[]
    df1=df[df["Source Field Name"].notnull()]
    for index,row in df1.iterrows():
        
        logging.info(str(row["Source Field Name"]) + "||" + str(row["Source Field Length"]))
        list_col_names.append(row["Source Field Name"])
        list_widths.append(int(row["Source Field Length"]))
    
    
    df_pla=pd.read_fwf(filepath_or_buffer=Data_File,widths=list_widths,header=None,names=list_col_names,skiprows=0,skipfooter=0)
    
    return df_pla;
    
Metadata_File="GWPC_CONV_AUTO_UMB_PLA_EXTRACT_V1.3.xls"
OutFile="PLA_Export.xlsx"
SourceDir="."
FilePattern="AUTO*.txt"
writer = pd.ExcelWriter(OutFile, engine='xlsxwriter')

logging.basicConfig(filename='PLA_LOAD.log',level=logging.INFO)
logging.info('Starting PLA Files into Excel Workbook...')
All_Files=os.listdir(SourceDir)
for file in All_Files:
    if fnmatch.fnmatch(file,FilePattern):
        Metadata=file.split("_")[1]
        pla_data=WritePLAtoExcel(Metadata_File,Metadata,file,OutFile)
        pla_data.to_excel(writer, sheet_name=file)
        logging.info('Write Completed for ' + str(file))    
writer.save()
logging.info('Write Completed')