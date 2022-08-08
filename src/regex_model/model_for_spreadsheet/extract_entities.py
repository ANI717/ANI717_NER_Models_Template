#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Animesh Bala Ani (ANI717): Baseline Software"""


#___Import Modules:
from regex_model.model_for_spreadsheet.utils.content_from_spreadsheet import content_from_spreadsheet
from regex_model.model_for_spreadsheet.utils.list_from_dataframe import list_from_dataframe

from regex_model.model_for_spreadsheet.extract_entity import extract_date
from regex_model.postprocess_entity import postprocess_date


#___Functions:
def extract_entities_from_list(data):
    
    # initialize local variables
    date = None
    date_anchors = []
    date_targets = []
    
    # extract matched anchors and targets
    for index in range(len(data)):
        extract_date.extract_anchors(index, data, date_anchors)
        extract_date.extract_targets(index, data, date_targets)
    
    
    # extract actual targets
    date = extract_date.find_target(date_anchors, date_targets)
    if date:
        date = postprocess_date.postprocess_item(date)
    
    return date, date_anchors, date_targets



def extract_entities(spreadsheet):
    
    content = content_from_spreadsheet(spreadsheet.get("file_name"), spreadsheet.get("sheet_name"))
    content_list = list_from_dataframe(content.get("content"), filter_item=True)
    
    (date, date_anchors, date_targets) = extract_entities_from_list(content_list.get("list_by_row") + content_list.get("list_by_column"))
    
    return {
        "file_name": spreadsheet.get("file_name"),
        "sheet_name": spreadsheet.get("sheet_name"),
        "content": content.get("content"),
        "list_by_row": content_list.get("list_by_row"),
        "list_by_column": content_list.get("list_by_column"),
        "date": date,
        "date_anchors": date_anchors,
        "date_targets": date_targets,
        }
