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
jan=0
feb=0
mar=0
apr=0
may=0
jun=0
jul=0
aug=0
sep=0
oct=0
nov=0
dec=0
with open('jan.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Jan.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        jan += 1
        myfile.close()
with open('feb.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Feb.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        feb += 1
        myfile.close()

with open('mar.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Mar.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        mar += 1
        myfile.close()

with open('apr.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Apr.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        apr += 1
        myfile.close()        


with open('may.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*May.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        may += 1
        myfile.close()


with open('jun.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Jun.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        jun += 1
        myfile.close()


with open('jul.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Jul.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        jul += 1
        myfile.close()


with open('aug.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Aug.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        aug += 1
        myfile.close()


with open('sep.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Sep.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        sep += 1
        myfile.close()


with open('oct.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Oct.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        oct += 1
        myfile.close()


with open('nov.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Nov.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        nov += 1
        myfile.close()


with open('dec.log', mode='wt', encoding='utf-8') as myfile:
        for line in open('local.log'):
                if bool(re.match('.*Dec.*',line.strip())):
                        myfile.write(line.strip()+"\n")
                        dec += 1
        myfile.close()

print('How many total requests were made in the time period represented in the log?')
print(count)
day= count / 375
week= count / 52
print('How many requests were made on each day?(On Average)')
print(day)
print('Per week?(On Average)')
print(week)
print('Per month?(On Average)')
print(jan, 'in Jan,')
print(feb, 'in Feb,')
print(mar, 'in Mar,')
print(apr, 'in Apr,')
print(may, 'in May,')
print(jun, 'in Jun,')
print(jul, 'in Jul,')
print(aug, 'in Aug,')
print(sep, 'in Sep,')
print(oct, 'in Oct,')
print(nov, 'in Nov,')
print(dec, 'in Dec')
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

with open('files.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(sorted2))
        myfile.close()

print('To see the files requested in order of most frequently to least frequently, please view the newly created files.txt')
print('Also, you can find a seperate log for each month in the same directory as this file')

