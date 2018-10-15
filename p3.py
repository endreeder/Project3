from urllib.request import urlretrieve
import re
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
lf = 'local.log'

local_file, headers = urlretrieve(url, lf)

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
open('local.log').read(64)
count=0
for line in open('local.log'):
  count+=1
print(count)
things = {}
errors=[]
for line in open('local.log'):
        pieces = regex.split(line)
        if len(pieces) > 7:
                filename = pieces[4]
                if filename in things:
                        things[filename] += 1
                else:
                        things[filename] = 1
print(things)




  
  # NOTE MOVE THIS TO THE BOTTOM
print('Question 1: How many total requests were made in the time period represented in the log?')

