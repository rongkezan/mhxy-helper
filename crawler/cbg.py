from selenium import webdriver
from selenium.webdriver.common.by import By


def switch_latest_window():
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])


options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
driver.get("https://xyq.cbg.163.com/cgi-bin/xyq_overall_search.py?act=show_search_role_form")

# 搜索页
level_min_input = driver.find_element(By.ID, "level_min")
level_min_input.send_keys("175")
server_3 = driver.find_element(By.ID, "server_type").find_element(By.CSS_SELECTOR, "[data_value='3']")
server_3.click()
btn_do_query = driver.find_element(By.ID, "btn_do_query")
btn_do_query.click()

# 角色列表页
switch_latest_window()
query_result = driver.find_element(By.ID, "query_result")
characters = query_result.find_elements(By.TAG_NAME, "a")
urls = []
for character in characters:
    url = character.get_attribute("href")
    if url.startswith("https://xyq.cbg.163.com/"):
        urls.append(url)

# for url in urls:
#     driver.get(url)
#     price = driver.find_element(By.CLASS_NAME, "price").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
#     print(price)
#     time.sleep(1)

url = urls[0]
driver.get(url)
# 价格
price = driver.find_element(By.CLASS_NAME, "price").find_element(By.TAG_NAME, "span").get_attribute("innerHTML").split('￥')[1].split('（')[0]
print(float(price))
# 乾元丹
num_qyd = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")[13].find_elements(By.TAG_NAME, "td")[0].get_attribute("innerHTML").split('>').pop()
print(int(num_qyd))
# 人物修炼
rw_xl_trs = driver.find_element(By.ID, "role_info_box").find_elements(By.CLASS_NAME, "cols")[1].find_elements(By.TAG_NAME, "table")[0].find_elements(By.TAG_NAME, "tr")
rw_xl = []
for i in range(len(rw_xl_trs)):
    xl = rw_xl_trs[i].find_element(By.TAG_NAME, "td").get_attribute("innerHTML")
    rw_xl.append(xl)
print(rw_xl)
# 宠物修炼
cw_xl = []
rw_xl_trs = driver.find_element(By.ID, "role_info_box").find_elements(By.CLASS_NAME, "cols")[1].find_elements(By.TAG_NAME, "table")[1].find_elements(By.TAG_NAME, "tr")
for i in range(len(rw_xl_trs)):
    xl = rw_xl_trs[i].find_element(By.TAG_NAME, "td").get_attribute("innerHTML")
    cw_xl.append(xl)
print(cw_xl)
role_skill = driver.find_element(By.ID, "role_skill")
role_skill.click()
sm_list = driver.find_element(By.CLASS_NAME, "skill").find_elements(By.TAG_NAME, "li")
sm_skills = []
for sm_li in sm_list:
    sm = sm_li.find_element(By.TAG_NAME, "p").get_attribute("innerHTML")
    sm_skills.append(sm)
print(sm_skills)
qz = []
fz_list = driver.find_element(By.ID, "role_info_box").find_elements(By.CLASS_NAME, "cols")[1].find_elements(By.TAG_NAME, "tbody")[0].find_elements(By.TAG_NAME, "td")
for fz in fz_list:
    str = fz.get_attribute("innerHTML")
    if str.__contains__("强壮") or str.__contains__("神速"):
        str = str.split("<p>")[1].split("</p>")[0]
        qz.append(str)
print(qz)

