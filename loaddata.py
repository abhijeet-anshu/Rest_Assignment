import os
ex=os.system('echo [`date "+%Y-%m-%d %T"` +0000] [$$] [INFO] Process: Read \
			data in progress with pid [$$]')

from api.models import Data
import time
reader = {}

#print '-----purge old data'
#time.sleep(3)
op = Data.objects.all().delete()

import csv
data_dict = {}
count = 0

#print 'about to read csv'
#time.sleep(3)
with open('Corpus.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    count += 1
    data_dict[row['value']] = row['key']

#print 'read %d data records' % count

#print 'Attempting to bulk insert %d records' % len(data_dict.keys())

#time.sleep(3)

op = Data.objects.bulk_create([Data(key=string_rep, value=numeric_rep) 
  for numeric_rep, string_rep in data_dict.iteritems()])

#print 'Successfully inserted %d data records' % Data.objects.count()
#print 'exiting' ,
#time.sleep(3)
exit()