#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Animesh Bala Ani (ANI717): Baseline Software"""


#___Import Modules:
import os

from regex_model.model_for_spreadsheet.extract_entities import extract_entities


#___Global Variables:
SOURCE_DIRECTORY = "../data/spreadsheets/"


#___List Spreadsheets:
spreadsheets = [{"file_name": os.path.join(SOURCE_DIRECTORY, item),
                 "sheet_name": "Sheet1"} for item in os.listdir(SOURCE_DIRECTORY)]


#___Exract Entities:
items = []
for spreadsheet in spreadsheets:
    items.append(extract_entities(spreadsheet))
    pass


#___Print Entities
for item in items:
    print(item.get("entities").get("date").get("postprocessed_content"))
