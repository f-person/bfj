import re
import sys

if len(sys.argv) == 1:
    go_struct = sys.stdin.read()
else:
    go_struct = open(sys.argv[1]).read()

json_tags = re.findall('json:"([^"]*)"', go_struct)

for m in json_tags:
    go_struct = go_struct.replace('json:\"%s\"' % m, 'json:\"%s\" bson:\"%s\"' % (m, m))

print(go_struct)
