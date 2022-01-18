import os
import constants as c
from enum import Enum

yz = [os.path.join(c.flag_ch_dir, name) for name in ['yz1.png', 'yz2.png', 'yz3.png', 'yz4.png']]
alg_dhw = [os.path.join(c.flag_ch_dir, name) for name in ['alg_dhw.png']]
dtgj_pts = [os.path.join(c.flag_ch_dir, name) for name in ['dtgj_pts.png']]
dtjw_csjw = [os.path.join(c.flag_ch_dir, name) for name in ['dtjw_csjw.png']]
bjlz_cac = [os.path.join(c.flag_ch_dir, name) for name in ['bjlz_cac.png']]
cac_bp = [os.path.join(c.flag_ch_dir, name) for name in ['xwtzg.png']]
bptdgg = [os.path.join(c.flag_ch_dir, name) for name in ['bptdgg.png']]
bpjgr = [os.path.join(c.flag_ch_dir, name) for name in ['bpjgr.png']]
xwtzg = [os.path.join(c.flag_ch_dir, name) for name in ['xwtzg.png']]
bpzhs = [os.path.join(c.flag_ch_dir, name) for name in ['bpzhs.png']]


class NPC(Enum):
    YZ = "驿站车夫", yz
    ALG_DHW = "傲来国->东海湾", alg_dhw
    DTGJ_PTS = "大唐国境->普陀山", dtgj_pts
    DTJW_CSJW = "大唐境外->长寿郊外", dtjw_csjw
    BJLZ_CAC = "北俱芦洲->长安城", bjlz_cac
    CAC_BP = "长安城->帮派", cac_bp
    BPTDGG = "帮派土地公公", bptdgg
    BPJGR = "帮派机关人", bpjgr
    BPZHS = "帮派召唤兽", bpzhs
    XWTZG = "玄武堂总管", xwtzg