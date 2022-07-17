import config
from bs4 import BeautifulSoup
import urllib.request, urllib.parse
import sys

req = urllib.request.Request(
    config.url, data=urllib.parse.urlencode(config.data).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
except urllib.error.HTTPError as err:
    print(err.code, file=sys.stderr)
    sys.exit(1)
except urllib.error.URLError as err:
    print(err.reason, file=sys.stderr)
    sys.exit(1)

bs = BeautifulSoup(body, "lxml")

matrixes = []
for tableid in config.matrix_ids:
    m =[]
    for tr in bs.find(id=tableid).find_all('tr'):
        r = []
        for td in tr.find_all('td'):
            r.append(td.text)
        m.append(r)
    matrixes.append(m)

print('matrixes are:', file=sys.stderr)
for i in range(len(matrixes[0])):
    for j in range(len(matrixes)):
        print(' '.join(matrixes[j][i]), end='  ', file=sys.stderr)
    print('', file=sys.stderr)

otp=[]
for p in config.pattern:
    otp.append(matrixes[p[0]][p[1]][p[2]])
print(''.join(otp))
