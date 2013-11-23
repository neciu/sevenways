#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulStoneSoup
import sys
import json

if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " <tones.html> <output.h>"
    exit()
tones_filename = sys.argv[1]
output_filename = sys.argv[2]

tones_file = open(tones_filename)
tones_data = tones_file.read()
tones_file.close()

soup = BeautifulStoneSoup(tones_data)
table = soup.find("table")

rows = table.findAll('tr')

chord_table = []

for row in rows:
    chord_row = []
    cells = row.findAll('td')

    for cell in cells:
        string = cell.string

        if string is None:
            try:
                string = cell.find('font').string
            except:
                break

        try:
            chord_row.append(float(string))
        except:
            chord_row.append(string)

    chord_table.append(chord_row)

output_file = open(output_filename, 'wr')
output_file.write(json.dumps(chord_table))
output_file.close()

