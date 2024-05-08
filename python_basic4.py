import os
import sys
import argparse
import random
import statistics
import pprint

print("osは基本ソフトウェアを利用するためのライブラリです")
path = os.getcwd()
print(f"os.getcwd()は現在の位置を取得します=={path}")

# 一段上の階層に移動
os.chdir("..")
print(f"os.chdir()はlinux cdと同様のことができます==={os.getcwd()}")

print(f"argv属性を利用してコマンドラインモジュールから受け取った引数をリストで格納することができます")
print(f"sys.argv==={sys.argv}")

# argvよりも効率的に引数を受け取って扱う方法
parser = argparse.ArgumentParser() # パーサーオブジェクトの作成
parser.add_argument("--head", nargs='?') # headの要素を指定 nargsに指定できるのは 数字=その個数, '?'=1つ？ "*" 0個以上の任意の数 "+"1個以上の任意の数
parser.add_argument("body",nargs="+") # body要素の指定　nargsで要素数を指定
args = parser.parse_args() # 引数の取得
print("変数の与え方は --head 最初の要素 残りの要素という形になります")
print(f"argsの中身は==={args}")