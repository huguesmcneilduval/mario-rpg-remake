
import json
from typing import Dict, List

objects = []
with open('action.json', 'r') as actions_f:
  actions:Dict[str,List] = json.load(actions_f)

  for value in actions.values():
    elem_type = value[0]
    if elem_type != 'MemberReference':
      objects.append(value)


with open('simplified.json', 'w') as output:
  output.write(json.dumps(objects))


