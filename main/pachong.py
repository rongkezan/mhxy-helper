from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
browser.find_element("kw").send_keys("selenium")
#通过id = kw定位百度输入框，通过键盘方法send_keys()向输入框中输入selenium。
browser.find_element("su").click()
#通过id=su定位搜索按钮，并向按钮发送单击事件click()
browser.quit()
