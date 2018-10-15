from urllib.request import urlretrieve
import re
from collections import Counter
from collections import OrderedDict
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


sorted2= sorted(things, key=things.get, reverse=True)

print('Here are the files that were requested in order of most frequently to least frequently')

print(sorted2)
