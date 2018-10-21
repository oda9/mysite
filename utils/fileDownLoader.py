import os, shutil
from time import sleep
from selenium import webdriver

path = os.getcwd() + "\\files\csv"

# ダウンロードフォルダの初期化
'''
shutil.rmtree(path)
while True:
    if os.path.exists(path):
        print("削除中：" + path)

    else:
        print("削除完了：" + path)
        break


# csvフォルダを再作成
os.mkdir(path)
'''

# ファイルダウンロード準備
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs", {"download.default_directory" : r"" + path + ""})
chrome = webdriver.Chrome(executable_path = "..\exe\chromedriver_win32.exe", options = chromeOptions)

# ファイルダウンロード先のURL
BASE_URL = "https://kabuoji3.com/stock/"
codeList = ["8267","3626"]
yearList = ["1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]

for code in codeList:
    for year in yearList:

        fileName = code + "_" + year + ".csv"

        # ダウンロード済みの場合は、スキップ
        if os.path.exists(path + "\\" + fileName):
            print("ダウンロード済：" + fileName)
            continue

        url = BASE_URL + code + "/" + year + "/"
        chrome.get(url)

        # name=csvのボタンをクリック
        chrome.find_element_by_name('csv').click()
        chrome.find_element_by_name('csv').click()

        # ダウンロードが開始されるまでタイムラグがあるので待機
        sleep(3)

        # ファイルダウンロードの監視
        while True:
            if os.path.exists(path + "\\" + fileName + ".crdownload"):
                print("ダウンロード中：" + fileName)

            else:
                print("ファイルダウンロード完了：" + fileName)
                break

        # サイトへの負荷を考慮し、1分間隔で処理を実施
        sleep(60)

print("ファイルダウンロード処理完了")
chrome.close()
