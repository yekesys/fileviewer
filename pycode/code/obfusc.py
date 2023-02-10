import json

import filev_utils

print("start ...")

input_str = "aba89qweurk"
a = filev_utils.txt2loi(input_str)
aa = [e-i for i,e in enumerate(a)]
print(aa)
print(json.dumps(aa))


cc = ''.join([chr(c) for c in [e+i for i,e in enumerate(aa)]])
assert cc==input_str
print(cc)


print("...done")

