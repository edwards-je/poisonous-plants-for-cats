#!/usr/bin/python3.8 -tt

# Munge poison plant list

import sys

# read text file
def text_read(file):
    with open(file, 'r') as f:
        text = f.readlines()
    return text

#cut





doc = text_read("singleline.txt")

# doc = doc[165:1448]
# with open("test.txt", 'w') as f:
#     for l in doc:
#         f.write(l)
# indexList = []
# singleLine = []
# for l in doc:
#     if l.find('<div class="views-field views-field-path">')!= -1:
#         # print('hit, line', doc.index(l))
#         singleLine.append(l)
#     else:
#         pass
# print(singleLine)
# h = 1
# with open("singleline.txt", 'w') as f:
#     for i in singleLine:
#         f.write(i)
for l in doc:
    

