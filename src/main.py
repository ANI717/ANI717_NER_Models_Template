#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Animesh Bala Ani (ANI717): Baseline Software"""


#___Import Modules:
import os
import pickle

from regex_model.model_for_spreadsheet.extract_entities import extract_entities


#___Global Variables:
SOURCE_DIRECTORY = "../data/spreadsheets/"
RESULT_FILE = "../data/results/spreadsheets_entities.pickle"


#___List Spreadsheets:
spreadsheets = [{"file_name": os.path.join(SOURCE_DIRECTORY, item),
                 "sheet_name": "Sheet1"} for item in os.listdir(SOURCE_DIRECTORY)]


#___Exract Entities:
items = []
for spreadsheet in spreadsheets:
    items.append(extract_entities(spreadsheet))
    pass


#___Print Entities:
for item in items:
    print(item.get("entities").get("date").get("postprocessed_content"))


#___Serialize Entities:
with open(RESULT_FILE, 'wb') as handle:
    pickle.dump(items, handle, protocol=pickle.HIGHEST_PROTOCOL)


#___Unserialize Entities from Pickle:
with open(RESULT_FILE, 'rb') as handle:
    unserialized_items = pickle.load(handle)
