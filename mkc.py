from omrc import omrc
import pprint
c = omrc[:]

cc = []

for i in range(len(c[1:])): 
    cc.append(round(c[i+1][0] - c[i][0], 3))
# cc[0] = c[0][0]

for n in range(len(cc)): 
    c[n+1][0] = cc[n]

with open("omrc1.py", "w", encoding="utf-8") as f: 
    f.write(f"omrc = {pprint.pformat(c)}")