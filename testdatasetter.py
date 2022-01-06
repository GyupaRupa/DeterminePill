import pandas as pd
import requests
import time

def main():
    csv = pd.read_csv('pills.csv').loc[:, ['품목일련번호', '큰제품이미지', '의약품제형', '품목명']]
    csvdatas = csv.to_dict('records')
    result = {
        '기타': [],
        '마름모형': [],
        '반원형': [],
        '사각형': [],
        '삼각형': [],
        '오각형': [],
        '원형': [],
        '육각형': [],
        '장방형': [],
        '타원형': [],
        '팔각형': []
    }

    for row in csvdatas:
        result[row['의약품제형']].append(row)

    for i in range(0, 100):
        # print(result['장방형'][i]['큰제품이미지'])
        # download(i, result['장방형'][i]['큰제품이미지'])
        pass
    print(result['장방형'][11])

def download(filename, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36'} 
    img = requests.get(url=url, verify=False).content
    # time.sleep(1)
    with open("./testimgs/" + str(filename) + ".jpg", 'wb') as handler:
        handler.write(img)


if __name__ == '__main__':
    main()