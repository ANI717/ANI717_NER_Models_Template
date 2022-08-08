#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Animesh Bala Ani (ANI717): Baseline Software"""


#___Import Modules:
import re
from datetime import datetime


#___Global Variables:
ANCHOR_PATTERNS = [".*date"]
TARGET_PATTERTNS = [".*\d{1,2}(\/|-| )\d{1,2}(\/|-| )\d{2,4}"]


#___Functions:
def extract_anchors(index, data, anchors=[]):
    
    if type(data[index]) == str:
        content = data[index].strip().lower()
    else:
        content = None
    
    if content:
        if re.match("|".join(ANCHOR_PATTERNS), content):
            anchors.append({
                "content": content,
                "index": index
                })
        


def extract_targets(index, data, targets=[]):
    
    if type(data[index]) == str:
        content = data[index].strip().lower()
    elif type(data[index]) == datetime:
        content = data[index].strftime("%m/%d/%Y").strip().lower()
    else:
        content = None
    
    if content:
        if re.match("|".join(TARGET_PATTERTNS), content):
            targets.append({
                "content": content,
                "index": index
                })


def find_target(anchors, targets):
    pass
