import sys
import json

if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " chord_table.json <output.h>"
    exit()
chord_table_filename = sys.argv[1]
output_filename = sys.argv[2]

chord_table_file = open(chord_table_filename)
chord_table = json.loads(chord_table_file.read())
chord_table_file.close()

original_chords = [
    105,70,52,52,41,49,52,105,70,41,41,35,39,41,105,66,39,39,33,35,39,105,70,41,49,52,105,52,0,0,141,52,105,41,141,49,52,105,41,0,0,141,41,105,35,141,39,41,99,39,0,0,133,39,99,33,133,35,39,105,41,141,49,105,52,141,105,41,41,49,52,52,52,0,0,118,49,49,52,59,59,59,0,0,118,59,49,52,59,39,0,0,105,41,141,49,105,52,141,105,41,41,49,52,52,52,0,0,118,49,49,52,59,59,59,0,0,118,59,0,0,158,49,52,118,59,158,39,0,0,105,41,141,49,105,52,79,66,52,39,0,0,79,66,52,39,0,0,79,66,52,39,0,0,79,66,52,39,0,0,79,66,52,39,0,0,79,66,52,39,0,0,79,39,39,0,105,33,35,79,39,33,105,35,39,79,39,39,0,105,33,35,79,39,33,105,35,39,70,35,34,0,105,29,33,70,35,29,105,33,35,70,35,34,0,105,29,33,70,35,29,105,33,35,105,70,35,34,26,0,0,105,70,35,34,26,0,0,105,70,52,52,33,35,39,41,79,39,0
]

times_array = [
    16,16,125,111,48,32,20,16,16,125,111,48,32,20,16,16,125,111,48,32,20,32,32,96,96,116,16,42,1,2,16,45,39,21,16,24,21,16,42,1,2,16,45,39,21,16,24,21,16,42,1,2,16,45,39,21,16,24,21,16,45,16,45,16,45,61,8,39,53,31,31,39,39,1,2,8,39,53,31,31,39,39,1,2,16,61,32,48,48,39,1,2,16,45,16,45,16,45,61,8,39,53,31,31,39,39,1,2,8,39,53,31,31,39,39,1,2,16,42,1,2,16,24,21,16,45,16,42,1,2,16,45,16,45,32,90,32,32,32,136,2,4,32,32,32,136,2,4,16,16,16,68,1,2,16,16,16,68,1,2,16,16,16,68,1,2,16,16,16,68,1,2,8,31,20,1,16,24,21,16,24,21,16,24,21,8,31,20,1,16,24,21,16,24,21,16,24,21,8,31,20,1,16,24,21,16,24,21,16,24,21,8,31,20,1,16,24,21,16,24,21,16,24,21,8,8,47,159,142,2,4,8,8,47,159,142,2,4,32,32,96,64,48,48,32,20,64,185,1
]

lookup_column = 4

for row in chord_table:
    print row

result_array = []
for original_chord in original_chords:
    result = 0
    for row in chord_table:
        if original_chord == row[lookup_column]:
            result = row[2]
    result_array.append(result)

result_array = [int(c) for c in result_array]

print 'Tones:\n{}'.format(result_array)
print 'Times:\n{}'.format(times_array)
print 'Number of elements: {} and {}'.format(len(result_array), len(times_array))
print 'Times sum: {}'.format(sum(times_array))

tone_distributions = []
for tone in sorted(set(result_array)):
    tone_distributions.append({'tone': tone, 'time': 0})

for x in range(len(times_array)):
    distribution = [d for d in tone_distributions if result_array[x] == d['tone']]
    distribution[0]['time'] += times_array[x]

print tone_distributions

number_of_thresholds = 7
times_sum = sum(times_array)

groups = []

accumulator = 0
i = 0
for x in range(number_of_thresholds):
    group = []
    while True:
        try:
            group.append(tone_distributions[i])
        except:
            break
        accumulator += tone_distributions[i]['time']

        i += 1

        current_thershold = times_sum * (x + 1) / number_of_thresholds
        if accumulator > current_thershold:
            groups.append(group)
            break

for group in groups:
    print 'Group: {}'.format(group)
    print 'Times sum in group: {}'.format(sum([d['time'] for d in group]))
    print 'Max tone in group: {}'.format(max([d['tone'] for d in group]))





