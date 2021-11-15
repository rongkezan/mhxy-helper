from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14495489'
API_KEY = 'MGp1SKRuGUl0EIM8iTSZqs9S'
SECRET_KEY = 'x0a5yBnI7TxQZGwvWA22Mg1s4zPPHdXT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def read_text_basic(filepath):
    with open(filepath, 'rb') as fp:
        img = fp.read()
        result = client.basicGeneral(img)
        if 'words_result' in result:
            items = result['words_result']
            words = []
            for item in items:
                words.append(item['words'])
            return words
        else:
            return None


def read_text_accurate(filepath):
    with open(filepath, 'rb') as fp:
        img = fp.read()
        result = client.basicAccurate(img)
        if 'words_result' in result:
            items = result['words_result']
            words = []
            for item in items:
                words.append(item['words'])
            return words
        else:
            return None


if __name__ == '__main__':
    words = read_text_basic('../resources/img/temp/game.png')
    print(words)
