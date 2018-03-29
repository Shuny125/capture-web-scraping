# site-capture
ExcelベースのURLリストの情報から自動でサイトを辿り、キャプチャ（PC/SP）を保存する機能です。  
同時に保存したキャプチャは、新しく生成したExcelに添付されます。

## Dependency
動作確認済み環境  
macOS Sierra 10.12.6  
Python 3.5.0  

Selenium 導入手順の参考ページ。  
https://qiita.com/Shuny125/items/7e68127c5ea0df04b82f

Python ライブラリインストール
```
$ pip install -r requirements.txt
```

## Usage
「url.xlsx」に必要な情報を入れてください。  
A列：ID  
B列：タイトル  
C列：URL  

必要な情報を入れたら、以下で実行します。
```
$ python capture.py
```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Shuny125](https://github.com/Shuny125)

## References
http://xlsxwriter.readthedocs.io/
