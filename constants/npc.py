import os
import constants.path as p
from enum import Enum

yz = [os.path.join(p.flag_npc_dir, name) for name in ['yz1.png', 'yz2.png', 'yz3.png', 'yz4.png']]
alg_dhw = [os.path.join(p.flag_npc_dir, name) for name in ['alg_dhw.png']]
dtgj_pts = [os.path.join(p.flag_npc_dir, name) for name in ['dtgj_pts.png']]
dtjw_csjw = [os.path.join(p.flag_npc_dir, name) for name in ['dtjw_csjw.png']]
bjlz_cac = [os.path.join(p.flag_npc_dir, name) for name in ['bjlz_capath.png']]
xwtzg = [os.path.join(p.flag_npc_dir, name) for name in ['xwtzg1.png', 'xwtzg2.png', 'xwtzg3.png', 'xwtzg4.png']]
bptdgg = [os.path.join(p.flag_npc_dir, name) for name in ['bptdgg.png']]
bpjgr = [os.path.join(p.flag_npc_dir, name) for name in ['bpjgr.png']]
bpshs = [os.path.join(p.flag_npc_dir, name) for name in ['bpshs.png']]


class NPC(Enum):
    YZ = "驿站车夫", yz
    ALG_DHW = "傲来国->东海湾", alg_dhw
    DTGJ_PTS = "大唐国境->普陀山", dtgj_pts
    DTJW_CSJW = "大唐境外->长寿郊外", dtjw_csjw
    BJLZ_CAC = "北俱芦洲->长安城", bjlz_cac
    BPTDGG = "帮派土地公公", bptdgg
    BPJGR = "帮派机关人", bpjgr
    BPSHS = "帮派召唤兽", bpshs
    XWTZG = "玄武堂总管", xwtzg
