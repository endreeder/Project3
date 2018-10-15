from urllib.request import urlretrieve
import re

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
lf = 'local.log'

local_file, headers = urlretrieve(url, lf)
fh = open('local.log')

for line in fh:
  print(line)




# NOTE MOVE THIS TO THE BOTTOM
print('Question 1: How many total requests were made in the time period represented in the log?')
count=0
for line in fh:
  count+=1
  
  
print(count)
