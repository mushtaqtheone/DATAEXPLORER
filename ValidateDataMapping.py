# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:24:11 2018

@author: Mushtaq Shaikh
Script performs following validations
-------------------------------------
1) Validates all xml tag are described as per GX Model. This includes all tags are correctly
called out,data types, length, hierarchy and each entity has publicid
2) Required=Yes and Not Null is not there
3) Derivation mentioned given is matching with transformation logic
4) Compare PLA and XML column data types

Generate report:
----------------
1) All the anamolies for above mentioned validations
2) List down all the PLA extract based on the provided underlying PLA tables
3) In case any entity or column is missing in PLA extract definition, it will highlight it

Fill Up the Technical Mapping sections
-------------------------------------
"""

import pandas as pd

#Files to be Read
file="Conversion_Data_Mapping_Auto_Home_Umb_V1.6.xlsx"
Metadata_File="GWPC_CONV_AUTO_UMB_PLA_EXTRACT_V1.1.xlsx"

# Reading the Data Mapping sheet
df=pd.read_excel(file,sheetname="Mapping - PA Policy",header=3)

#Selection Criteria
#Filter only the required one
df_Req=df[(df.Entity.notnull()) & (df.Required == 'Yes') ]
#Filter only S4 and S5 Sprints
df_SprintOnly=df_Req[df_Req.isin({'Sprint':['S4','S5']})]

df_metadata=pd.read_excel(Metadata_File,sheetname=None,skiprows=2)

for key,df_value in df_metadata.items():
    print(key)
#print(df_SprintOnly)
