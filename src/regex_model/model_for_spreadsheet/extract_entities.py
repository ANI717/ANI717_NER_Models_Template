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
    
    # initialize variables
    date_content = None
    date_anchors = []
    date_targets = []
    
    # extract anchors and targets
    for index in range(len(data)):
        extract_date.extract_anchors(index, data, date_anchors)
        extract_date.extract_targets(index, data, date_targets)
    
    
    # extract content
    date_content = extract_date.extract_content(date_anchors, date_targets)
    date = {
        "content": date_content,
        "anchors": date_anchors,
        "targets": date_targets,
        "postprocessed_content": postprocess_date.postprocess_item(date_content.get("content")),
        }
    
    return date



def extract_entities(spreadsheet):
    
    content = content_from_spreadsheet(spreadsheet.get("file_name"), spreadsheet.get("sheet_name"))
    content_list = list_from_dataframe(content.get("content"), filter_item=True)
    
    date = extract_entities_from_list(content_list.get("list_by_row") + content_list.get("list_by_column"))
    
    return {
        "file_name": spreadsheet.get("file_name"),
        "sheet_name": spreadsheet.get("sheet_name"),
        "content": {
            "content": content.get("content"),
            "list_by_row": content_list.get("list_by_row"),
            "list_by_column": content_list.get("list_by_column"),
            },
        "entities": {
            "date": date
            },
        }
