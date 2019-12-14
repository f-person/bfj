import re
import sys

omitempty_in_json = True

def omitempty_tag(jsonMode=False):
    if jsonMode:
        if omitempty_in_json:
            return ",omitempty"
        else:
            return ""
    
    return ",omitempty"

if len(sys.argv) == 1:
    go_struct = sys.stdin.read()
else:
    go_struct = open(sys.argv[1]).read()

json_tags = re.findall('json:"([^"]*)"', go_struct)

for m in json_tags:
    go_struct = go_struct.replace('json:\"%s\"' % m, 'json:\"%s%s\" bson:\"%s%s\"' % (m, omitempty_tag(True), m, omitempty_tag()))


print(go_struct)
