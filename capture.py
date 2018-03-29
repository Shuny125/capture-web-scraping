import xlrd
import os
import xlsxwriter
import math
import time
from selenium import webdriver

## -------------------------------------
## ExcelのURLからスクショを保存
## -------------------------------------

## ExcelからURLを取得
book = xlrd.open_workbook('url.xlsx')
sheet = book.sheet_by_index(0)

## 取得した情報を保存しておくための入れ物
IDLIST = []
TITLELIST = []
URLLIST = []

## IDを取得
for row in range(sheet.nrows):
    ## セルの値（URL）を取得
    ID = sheet.cell(row, 0).value
    IDLIST.append(ID)

## タイトルを取得
for row in range(sheet.nrows):
    ## セルの値（URL）を取得
    TITLE = sheet.cell(row, 1).value
    TITLELIST.append(TITLE)

## PCキャプチャ
## ブラウザを起動（ページ全体をキャプチャしてくれるためSafariを使用）
driver = webdriver.Safari()
driver.maximize_window()

##  URLを取得（キャプチャ保存）
for row in range(sheet.nrows):
    ## セルの値（URL）を取得
    URL = sheet.cell(row, 2).value
    URLLIST.append(URL)

    ## 画面遷移
    driver.get(URL)

    ## 遷移直後だと崩れた状態でスクショされる可能性があるため、1秒待機
    time.sleep(1)

    ## 画面キャプチャを保存
    FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), IDLIST[row] + '.png')
    driver.save_screenshot(FILENAME)

## ブラウザを閉じる
driver.quit()

## SPキャプチャ
## ブラウザを起動（ページ全体をキャプチャしてくれるためSafariを使用）
driver = webdriver.Safari()
## UA判定が必要な場合は上記を削除し、以下を使用
# USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A356 Safari/604.1"
# driver = webdriver.PhantomJS(desired_capabilities={'phantomjs.page.settings.userAgent': USER_AGENT})
driver.set_window_size(375, 720)

##  URLを取得（キャプチャ保存）
for row in range(sheet.nrows):
    ## セルの値（URL）を取得
    URL = sheet.cell(row, 2).value

    ## 画面遷移
    driver.get(URL)

    ## 遷移直後だと崩れた状態でスクショされる可能性があるため、1秒待機
    time.sleep(1)

    ## 画面キャプチャを保存
    FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), IDLIST[row] + '_sp.png')
    driver.save_screenshot(FILENAME)

## ブラウザを閉じる
driver.quit()


## -------------------------------------
## 保存したスクショをExcelに添付
## -------------------------------------

## 添付した数をカウントするための変数
count = 0

for i in range(math.ceil((row+1)/10)):
    ## 画像添付用のExcelを作成
    workbook = xlsxwriter.Workbook('capture' + str(i+1) + '.xlsx')

    ## 残り添付数を計算
    if (row+1)-count >= 10:
        num = 10
    else:
        num = (row+1)%10

    for j in range(num):
        ## シートを追加
        worksheet = workbook.add_worksheet(IDLIST[count] + '_' + TITLELIST[count])

        ## 対象ページの情報を記載
        worksheet.write('A1', IDLIST[count])
        worksheet.write('A2', TITLELIST[count])
        worksheet.write('A3', URLLIST[count])

        ## 画像を添付
        IMAGE_SP = IDLIST[count] + '_sp.png'
        IMAGE_PC = IDLIST[count] + '.png'
        worksheet.insert_image('B4', IMAGE_SP, {'x_scale': 0.45, 'y_scale': 0.45})
        worksheet.insert_image('H4', IMAGE_PC, {'x_scale': 0.3, 'y_scale': 0.3})

        ## 添付するごとにカウントを増やす
        count = count+1

    ## 10シートごとにExcelを閉じる
    workbook.close()
