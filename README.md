# capture-web-scraping
Excel ベースの URL リストの情報から自動でサイトを辿り、キャプチャ（PC/SP）を保存する機能です。  
同時に保存したキャプチャは、新しく生成した Excel に添付されます。

## Dependency
動作確認済み環境  
macOS Sierra 10.12.6  
Python 3.5.0  
※Windows 確認中

## Setup
### Python
https://www.python.org/downloads/windows/  
3系の最新バージョンをインストール  
→「Download Windows x86-64 executable installer」

ターミナルを開いて、以下のコマンドを実行。
```
$ python —V
```
バージョンが表示されたらOK。

### pip
ターミナルを開いて、以下のコマンドを実行。
```
$ easy_insatll pip
```

### selenium
ターミナルを開いて、以下のコマンドを実行。
```
$ pip install selenium
```

### Python ライブラリインストール
ターミナルを開いて「requirements.txt」と同じディレクトリにいる状態で、以下のコマンドを実行。
```
$ pip install -r requirements.txt
```

### Safari 設定
Safari の「環境設定」から「詳細」タブを開き、「メニューバーに"開発"メニューを表示」にチェック。

表示された「開発」メニューから「リモートオートメーションを許可」にチェック。

## Usage
### url.xlsx
必要な情報を記入。  
A列：ID  
B列：タイトル  
C列：URL  

### 実行
ターミナルを開いて、以下のコマンドを実行。
```
$ python capture.py
```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Shuny125](https://github.com/Shuny125)

## References
http://xlsxwriter.readthedocs.io/
