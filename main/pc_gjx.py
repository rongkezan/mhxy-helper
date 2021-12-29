import urllib3
import json
import time
from urllib.parse import urlencode

http = urllib3.PoolManager()
level = 1
for i in range(160):
    time.sleep(2)
    encoded_args = urlencode({
        "target": "box_tools",
        "from": "pc_box_tools",
        "paper_id": "2831",
        "act": "skill_calculate",
        "xls_name": "xyq_box_tools.xlsx",
        "sheet_name": "bangpaijineng",
        "max_val": "160",
        "min_val": "0",
        "from_val": "0",
        "to_val": str(level),
        "type": "1"
    })
    level += 1

    url = 'http://box.gm.163.com/cgi-bin/csa/csa_self_help_dispatch.py?' + encoded_args
    res = http.request('POST', url)
    data = json.loads(res.data)
    print(data['data']['jinqian'])
