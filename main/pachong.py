import urllib.request
import urllib.parse
import requests

url = "https://xyq.cbg.163.com/equip?s=795&eid=202110212100113-795-3RG0CJJPZTGL"
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ntes_nnid=f4f29d7637df68be38b39e51acb25a57,1631070039828; _ntes_nuid=f4f29d7637df68be38b39e51acb25a57; _ns=NS1.2.810954774.1631428582; fingerprint=9grxczfc7ucb4n6v; gdxidpyhxdE=q%2BOtLS%2BpB2%2BVVevfjij%2BOOsz5C73f5saJ%2FA%2BYfhyY7yqagpwcHQS8aEM6%2FeIz9qRpnuL6%2FtKwkP%5CbymmfJGnd0bbZj%5CuuQXS4Q4qsNuDCXbqp2NmtGfYfJ5rcgd%2FHj2Wt8EoNvSoCMCp7mSv%2ByBxPnZHiZAWciaMcZYiowYLn%5CkRCBpn%3A1631691659797; _9755xjdesxxd_=32; YD00000722197596%3AWM_NI=JSJzPrt2Mz2ezKw8wBnsKEc50LynwjlA76pjItT%2Fur0ThstQsb4VjR9GoiI8LvnMnVKmi5sBZ0VcaTw67E%2Bt9%2Bos1vZkLTgudcRaD1%2BcRVzQiX%2BFUklicYL7wgThdUMeank%3D; YD00000722197596%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee93b23bb0ebc0d8f652fb9a8bb7d44a978e8aaab63af6ee9faaf2478e8f8c95ed2af0fea7c3b92a8a8d869bd37ab8ee839bb16fba95b9d9f64aaead85a6e23ff494b78ff662b09ff9d7f3628bac9cd0f87af48ca894f75bb1befcb7e95afb99a18acc3490aaa2aeed5e89b3a7d6f24a9af09a84e460b5eaf9a6aa80fbf5a194b47e9ab584b5e67fa8bd9e82c73be9bd9eb7f95bab88e5a7d861b0b7adbacf3db5b99c89e75f8fbbaf8fea37e2a3; YD00000722197596%3AWM_TID=t2UaaVscVeZEFURBEVY7z73QcsMNRCpn; area_id=44; recommend_typeids=1,2,3,4; recommend_url=https://xyq.cbg.163.com/cgi-bin/query.py?act=recommend_search&recommend_type=1; _nietop_foot=%u68A6%u5E7B%u897F%u6E38%u7535%u8111%u7248%7Cxyq.163.com; _ga=GA1.2.1218248413.1638846326; NTES_P_UTID=XbR1LyYZFozE5Vs1vh8nZIzVNN7YgNts|1638875215; P_INFO=rkzlyn4@163.com|1638875215|0|epay|00&99|zhj&1638871113&cbg#zhj&330100#10#0#0|&0|cbg_qrcode&cbg&epay_client|rkzlyn4@163.com; NTES_CMT_USER_INFO=471519737%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0s6J7V%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7Ccmt6bHluNEAxNjMuY29t; timing_user_id=time_m7lomTTWQm; _external_mark=www.baidu.com; __session__=1; login_user_school=15; offsale_num=0; unpaid_order_num=0; unpaid_order_price_total=0.00; alert_msg_flag=1; last_login_roleid=18553108; login_user_nickname=%25E7%25BB%25914%25E5%259B%25BA%25E4%25BC%25A4%25E6%2588%2592%25E6%258C%2587y; login_user_urs=rkzlym@163.com; last_login_role_serverid=130; wallet_data=%7B%22is_locked%22%3A%20false%2C%20%22checking_balance%22%3A%200%2C%20%22balance%22%3A%200%2C%20%22free_balance%22%3A%200%7D; is_user_login=1; login_user_icon=5; login_user_roleid=18553108; login_user_level=109; cbg_qrcode=JCsi_kYttecEsiSBPcjZ3G5p5C4RCKUTOTp58wXt; NTES_SESS=R0NQ2HIkMNCcQUsaYCCVtyN21t4DHhBf70uUqYUOwrr1zN87uIq5FPFyym.BP_Hkp_AmyKLoBnJC__JMUfcA.VrLU6V07RAT6YJRRn77suSwp7aJ7eR4nfGp82g3vpPZynA7lO2acMlAyke8c71dZdt8Etw.jZdbiQxBSEy.uKQJDqYhlH8GAlmg1eynxRE3z9IDTpX2KVymp; sid=QfHqQKbO60IaRi8pidsE-ECOfhYbFr25LHbpqNjH; cur_servername=%25E8%259D%25B4%25E8%259D%25B6%25E6%25B3%2589; trace_session_id=017DB295-41CD-B5C4-001C-9DDC03BDBEAF; new_msg_num=11; last_login_serverid=130; remind_offsale=1; reco_sid=fugFq4R1NaYdrcDvij_3U3gza_zf1U-yO89gIQKO',
    'Host': 'xyq.cbg.163.com',
    'Referer': 'https://xyq.cbg.163.com/cgi-bin/login.py?ret_url=https%3A%2F%2Fxyq.cbg.163.com%2Fcgi-bin%2Fequip_detail.py%3F%26s%3D795%26eid%3D202110212100113-795-3RG0CJJPZTGL&act=prepare_login',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}
r = requests.get(url, headers=header)
print(r.text)
# request = urllib.request.Request(url, headers=header)
# response = urllib.request.urlopen(request).read()
# print(response)
#
fh = open("./cbg.html", "wb")  # 将文件写入到当前目录中
fh.write(r.text)
fh.close()
