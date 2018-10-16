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

print('How many total requests were made in the time period represented in the log?')
print(count)

day= count / 375
week= count / 52
month= count / 12

print('How many requests were made on each day?(On Average)')
print(day)

print('Per week?(On Average)')
print(week)

print('Per month?(On Average)')
print(month)
c1='302'
c2='304'
c3='400'
c4='401'
c5='403'
c6='404'
sent=0
error=0
for line in open('local.log'):
        code = regex.split(line)
    if len(code) > 7:
                if code[6] == c1:
                        sent+=1
                if code[6] == c2:
                        sent+=1
                if code[6] == c3:
                        error+=1
                if code[6] == c4:
                        error+=1
                if code[6] == c5:
                        error+=1
                if code[6] == c6:
                        error+=1


print('What percentage of the requests were not successful (any 4xx status code)?')
pe=error/count*100
print(pe, '%')
print('What percentage of the requests were redirected elsewhere (any 3xx codes)?')
ps=sent/count*100
print(ps, '%')
things = {}


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
