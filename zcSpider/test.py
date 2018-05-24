import arrow
from datetime import datetime
import requests
import json

def fb_gid_get_nday(xtfb, timStr, fgExt=False):
    if timStr == '':
        ktim = xtfb.time_now
    else:
        ktim = arrow.get(timStr)

    nday = 55

    for tc in range(0, nday):
        xtim = ktim.shift(days=+tc)
        xtimStr = xtim.format('YYYY-MM-DD')
        print(xtimStr)

'''
xtfb = 0

lyCount = 251
pageCount = lyCount // 30 + (1 if lyCount % 30 > 0 else 0)
print(pageCount)
for i in range(pageCount):
    print(i)


#fb_gid_get_nday(xtfb, '2010-01-20')

content = requests.get('http://odds.500.com/fenxi1/ouzhi.php?id=278468&ctype=1&start=200&r=1&style=0&guojia=0&chupan=1').text
print(content)

start = datetime(2010, 1, 1, 0, 0, 0)
end = datetime(2010, 4, 1, 0, 0, 0)

for day in arrow.Arrow.range('day', start, end):
    dayStr = day.format('YYYY-MM-DD')
    print(dayStr)
'''

sjson = '''
    [
    ["0.850", "半球\/一球", "1.049"],
    ["4.000", "两球半", "0.160"],
    ["3.150", "两球", "0.210"],
    ["2.100", "球半\/两球", "0.350"],
    ["3.500", "两球\/两球半", "0.180"],
    ["1.600", "球半", "0.470"],
    ["5.400", "两球半\/三球", "0.110"],
    ["0.300", "平手", "2.450"],
    ["0.640", "半球", "1.200"],
    ["0.240", "受平手\/半球", "2.890"],
    ["0.200", "受半球", "3.250"],
    ["1.070", "一球", "0.720"],
    ["1.350", "一球\/球半", "0.570"],
    ["0.130", "受半球\/一球", "4.750"],
    ["0.470", "平手\/半球", "1.600"]
]
'''

vjson = json.loads(sjson)
if len(vjson) > 1:
    for key, data in enumerate(vjson):
        if key == 0: continue
        print('{0} {1} {2}'.format(data[0], data[1], data[2]))


print(arrow.now().timestamp)
print(arrow.now().float_timestamp)
print(int(arrow.now().float_timestamp * 1000))

