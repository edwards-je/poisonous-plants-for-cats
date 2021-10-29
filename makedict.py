#!/usr/bin/python3.8

"""
Messy code to take in newline-delimited text file and convert to dict of dicts.
Eventually made into SQL database
"""

import sys

# read text file to list, each line separate entry
def text_read(file):
    with open(file, 'r') as f:
        text = f.readlines()
    return text

mungedList = []
rawList = text_read('data/rawdata.txt')

# text clean up 
for l in rawList:
    l = (l.replace('</a ', ' |'))
    l = l.replace('<b Scientific Names:</b  <i ', '')
    l = l.replace('</i', '')
    l = l.replace('<b Family:</b  ', '')
    l = (l.replace('</span', ''))
    l = l.replace(' \n', '')
    mungedList.append(l)


# dict of dicts schema
plants = {
    'key' : {'name' : '', 
            'additional common names': '',
            'scientific name' : '', 
            'family' : ''}
            }


# example format for entry
# plants[1] = {
#     'name' : 'Adam-and-Eve',
#     'additional common names' : 'Arum, Lord-and-Ladies, Wake Robin, Starch Root, Bobbins, Cuckoo Plant',
#     'scientific name' : 'Arum maculatum',
#     'family' : 'Araceae'
# }


# loop through list and enter into plants dict. assigns primary key.
for count, ele in enumerate(mungedList, 1):
    m = ele.split(' | ')
    plants[count] = {
        'name' : m[0],
        'additional common names' : m[1],
        'scientific name' : m[2],
        'family' : m[3]
        }


plants_id = {}
for i in plants:
    plants_id[plants[i].get("name")] = i


x = sys.argv[1]
if x in plants_id:
    print(plants_id[x], plants[plants_id[x]])
    
