import json
from typing import List

def add_member_reference(id):
  member_references.append([
        'MemberReference',
        {'IdRef': id}
      ]
  )

output_data = {}
member_references=[]
add_member_reference(3)
classes_with_id = []


with open('simplified.json', 'r') as input:
  data:List[List] = json.load(input)
  for index, elem in enumerate(data):
    elem_type = elem[0]
    if elem_type == 'ClassWithId':
      add_member_reference(elem[1]['ObjectId'])
      classes_with_id.append(elem)
    if elem_type == 'SerializedStreamHeader':
      serialized_stream_header = elem
    if elem_type == 'BinaryLibrary':
      binary_library = elem
    if elem_type == 'BinaryArray':
      binary_array = elem
    if elem_type == 'ClassWithMembersAndTypes':
      class_with_members_and_types = elem


number_class_with_id = len(classes_with_id)

binary_array[1]['Lengths'] = [number_class_with_id+1]

output_data= {
  '0': serialized_stream_header,
  '1': binary_library,
  '2': binary_array
}
  
for index,member_ref in enumerate(member_references):
  id = member_ref[1]['IdRef']
  output_data[id] = member_ref



output_data['%d'%(number_class_with_id+4)] = class_with_members_and_types

for index,cwi in enumerate(classes_with_id):
  new_id = number_class_with_id + 5 + index
  output_data['%d' % new_id] = cwi



output_data['%d'%(number_class_with_id * 2 + 5)] = ["MessageEnd", None]




with open('final.json', 'w') as output:
  output.write(json.dumps(output_data))

asd = ''







