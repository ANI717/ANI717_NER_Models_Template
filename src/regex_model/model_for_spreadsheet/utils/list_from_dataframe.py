#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Animesh Bala Ani (ANI717): Baseline Software"""


#___Import Modules:
import math

    
#___Functions:
def filter_content(item, filter_item=True):
    if filter_item:
        if item == "":
            return False
        else:
            try:
                if math.isnan(item):
                    return False
            except:
                pass
    return True


def list_from_dataframe(df, filter_item=True):
    
    list_by_row = [item for row in df.to_numpy() for item in row if filter_content(item, filter_item)]
    list_by_column = [item for row in df.to_numpy().transpose() for item in row if filter_content(item, filter_item)]
    
    return {
        "list_by_row": list_by_row,
        "list_by_column": list_by_column,
        }
