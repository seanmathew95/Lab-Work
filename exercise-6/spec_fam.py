import re
import sys
file_to_read = sys.argv[1]
ebird_file = open(file_to_read)

ebird_dict={}
for line in ebird_file:
	csv=re.split(",", line)
	family=csv[7]
	species=csv[3]
	ebird_dict[species]=family

for key in ebird_dict:
	print("Species " + key + " belongs to Family " + ebird_dict[key])

