#!/usr/bin/python3
"""
7-add_item script
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
file script
"""


arglist = []
for i in sys.argv:
    if i == sys.argv[0]:
        pass
    else:
        arglist.append(i)

file = "add_item.json"
if os.path.exists(file):
    data = load_from_json_file(file)
    data = data + arglist
    save_to_json_file(data, file)
else:
    save_to_json_file(arglist, file)
