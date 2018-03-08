#! /usr/local/bin/python3
import json
import yate
import athletemodel

names = athletemodel.get_names_from_store()

print(yate.start_response("application/json"))
print(json.dumps(sorted(names)))