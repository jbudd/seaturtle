import csv
import re
import pandas as pd

import sys


filename = sys.argv[1]
data = open(filename, 'r')
data = data.readlines()


# data = re.sub(r"\D",", ",data[0])

count = 0
master_list = [] 
string = ''
for d in data[0]:
	string += d
	if d == ']':
		count += 1
		if count == 3:
			master_list.append(string)
			string = ''
			count = 0

clean_list = []
for d in master_list:
	d = d.split(',')
	items = []
	for i in d:
		item = ''
		for c in i:
			if (c != '[') and (c != ']') and (c != '(') and (c != ')'):
				item += c
		items.append(float(item))
	clean_list.append(items)

df = pd.DataFrame(clean_list)
df.columns = ['Accel_X','Accel_Y','Accel_Z','Mag_X','Mag_Y','Mag_Z','Mag_o', 'Gyro_X', 'Gyro_Y', 'Gyro_Z', 'Pressure', 'Temp', 'Timestamp']
df['Time'] = df.Timestamp - df.Timestamp.values[0]
df[['Accel_X', 'Accel_Y', 'Accel_Z']] /= (1000/9.8)

df['v_X'] = 0
df['v_Y'] = 0
df['v_Z'] = 0
df['X'] = 0
df['Y'] = 0
df['Z'] = 0
for i in df.index[1:]:
	df['v_X'].ix[i] = df['v_X'].ix[i-1] + df['Accel_X'].ix[i-1]*(df['Time'].ix[i]-df['Time'].ix[i-1])
	df['v_Y'].ix[i] = df['v_Y'].ix[i-1] + df['Accel_Y'].ix[i-1]*(df['Time'].ix[i]-df['Time'].ix[i-1])
	df['v_Z'].ix[i] = df['v_Z'].ix[i-1] + df['Accel_Z'].ix[i-1]*(df['Time'].ix[i]-df['Time'].ix[i-1])

	df['X'].ix[i] = df['X'].ix[i-1] + df['v_X'].ix[i-1]*(df['Time'].ix[i]-df['Time'].ix[i-1])
	df['Y'].ix[i] = df['Y'].ix[i-1] + df['v_Y'].ix[i-1]*(df['Time'].ix[i]-df['Time'].ix[i-1])
	df['Z'].ix[i] = df['Z'].ix[i-1] + df['v_Z'].ix[i-1]*(df['Time'].ix[i]-df['Time'].ix[i-1])



print df.head()

df.to_csv(filename + '.csv' , index = False)


