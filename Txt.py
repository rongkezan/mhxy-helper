from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14495489'
API_KEY = 'MGp1SKRuGUl0EIM8iTSZqs9S'
SECRET_KEY = 'x0a5yBnI7TxQZGwvWA22Mg1s4zPPHdXT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def read_text(filepath):
    with open(filepath, 'rb') as fp:
        img = fp.read()
        return client.basicAccurate(img)


text = read_text('img/temp/temp_chengyu.jpg')
print(text)
# print(text['words_result'][0])