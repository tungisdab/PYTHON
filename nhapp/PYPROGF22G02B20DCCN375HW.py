# B20DCCN375 - Nguyen Cong Khanh - Nhom 02

import re
import pandas as pd


a = {}
def check(id):
    global a
    if id == 'NAN': return True
    if id in a:
        return False
    a[id] = 1
    if not re.match("B\d{2}\w{4}\d{3}", id):
        return False
    return True
cnt = 0
data = pd.read_excel('book1.xlsx')
for i in range(len(data)):
    id1, name1 = str(data.loc[i][0]).strip().upper(), data.loc[i][1]
    id2, name2 = str(data.loc[i][3]).strip().upper(), data.loc[i][4]
    id3, name3 = str(data.loc[i][6]).strip().upper(), data.loc[i][7]
    if not (check(id1) and check(id2) and(id3)):
        cnt += 1
        print(data.loc[i].to_string())
        print("-------------------------------------------")
print("Invalid group(s): ", cnt)