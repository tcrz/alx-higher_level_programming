#!/usr/bin/python3
import sys
import os
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

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
    save_to_json_file([], file)
