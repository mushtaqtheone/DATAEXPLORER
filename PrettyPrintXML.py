# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:17:32 2018

@author: Mushtaq Shaikh
Print a XML file in a well formatted and intended way so that it's easy to understand it
"""

import xml.dom.minidom as xdom


xml_path="C:\/Users/161384/Downloads/gxmig_Sprint5Updated_17082018/gxmig/Account.xml"
xml_fpath="C:\/Users/161384/Downloads/gxmig_Sprint5Updated_17082018/gxmig/Account_formatted.xml"
xml = xdom.parse(xml_path) 
pretty_xml_as_string = xml.toprettyxml()

fxml=open(xml_fpath,'w')
fxml.write(pretty_xml_as_string)
fxml.close()
