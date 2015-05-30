from collections import OrderedDict
import json

d = OrderedDict()
dd = OrderedDict()
dd['wibble'] = 'haha'
dd['wobble'] = 'hehe'
d['foo'] = 1
d['bar'] = 2
d['spam'] = dd
d['grok'] = 'huehue'

print json.dumps(d)
