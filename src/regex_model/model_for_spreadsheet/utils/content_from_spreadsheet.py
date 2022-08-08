#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Animesh Bala Ani (ANI717): Baseline Software"""


#___Import Modules:
import pandas as pd


#___Functions:
def content_from_spreadsheet(file_name, sheet_name, header=None):
    
    content = pd.read_excel(file_name, sheet_name=sheet_name, header=header)
    
    return {
        "file_name": file_name,
        "sheet_name": sheet_name,
        "content": content,
        }
