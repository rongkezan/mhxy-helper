import urllib3
import json
from urllib.parse import urlencode

http = urllib3.PoolManager()
level = 100
for i in range(79):
    encoded_args = urlencode({
        'target': 'box_tools',
        'from': 'pc_box_tools',
        'paper_id': '2798',
        'act': 'accumulation',
        'xls_name': 'xyq_box_tools.xlsx',
        'sheet_name': 'shimenjineng',
        'max_val': '180',
        'min_val': '0',
        'from_val': str(level),
        'to_val': str(level + 1)
    })
    level += 1

    url = 'http://box.gm.163.com/cgi-bin/csa/csa_self_help_dispatch.py?' + encoded_args
    res = http.request('POST', url)
    data = json.loads(res.data)
    print(data)
    print(data['data']['money'])
