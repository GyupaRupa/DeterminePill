import requests
import pandas as pd
import time

def main():
    csv = pd.read_csv('pills.csv').loc[:, ['품목일련번호', '큰제품이미지']].head(100)
    datas = csv.to_dict()

    for i in range(100):
        download(i, datas['큰제품이미지'][i])


def download(filename, url):
    img = requests.get(url).content
    # time.sleep(1)
    with open("./testimgs/" + str(filename) + ".jpg", 'wb') as handler:
        handler.write(img)

if __name__ == '__main__':
    main()