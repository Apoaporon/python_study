# python データ分析試験のメモ

## 仮想環境
- 抜ける時は deactivate

## pip
- install version指定
- uninstall package名
- pip freeze
    - インストールされているパッケージの一覧出力( pip freeze > requirements.txtで使われるのが一般的)
- pip install -U package名
    -　アップグレード

## IPython
- IPythonは、TABキーによる補完と[?]によるオブジェクトの説明表示に対応している。この機能は標準のpythonのインタープリターには無い機能

## Jpyter notebook
- %などをつけるのは、マジックコマンド実行のため
    - %who:使われている変数一覧
    - %timeit:処理時間計算
- !, !!はhせるコマンドを実行するためのコマンド
    - !ls
    - !dir
    - !!: コマンドの出力をリスト形式で取得
## 数式
足し算を繰り返す記号はΣ（シグマ）を使い、すべてを掛け合わせる記号はΠ（パイ）を使います。
Π（パイ）は掛け合わせます。次の式は、iに1から4まで順番に代入し、掛け合わせます。解は「1×2×3×4=24」です。

$$
\prod_{i=1}^{4} i = 1 \times 2 \times 3 \times 4 = 24
$$

## numpy
- Numpyの配列は1つのデータ型しか扱えない。intとfloatを同じ配列内に入れるとint->floatに変換される

## dataframe
- データフレームのインデックス属性、カラム属性は、df.index[0]という指定方法はできず、変更する際は一度に変換する必要がある

```python
df.index[0] = ['1行目'] # これはエラーになる
df.index = ['1行目', '2行目'] # このように一括変換
df.rename(index={'1行目': '01'}, columns={'A列': 'a'}) # renameメソッドを活用する
```

- read_htmlはtable属性をdataframeとして読み込む

- groupby
    - groupby関数はデータを「分割→適用→結合」する関数です
    - Grouperオブジェクトを引数にすることで周期を指定できます←指定してないとエラー？

## matplotlib
- subplots
    - subplots(2):上下に描画スペースが作成される
    - subplots(2,2): 2*2の描画スペースが作成
    - subplots(1,2) or subplots(2, ncols=2):左右に描画スペースが作成
- subplot関数でも上記と同様のことが可能
    - subplot(121), (122):(行、列、位置)を指定している(0スタートではなく1スタートであることに注意)

## scikit-learn
- カテゴリ変数エンコーディング
    - 「北海道」「東京」「沖縄」というデータがあった場合、scikit-learnのLabelEncoderクラスでカテゴリ変数エンコーディングすると、「0」「1」「2」
- OneHotエンコーディング
    - 値の分だけ列を増やし、各行の該当する値の列に1、それ以外の列に0が入力されます。
- pandas get_dummies関数はDataFrameが返るが、scikit-learnのOneHotEncoderは疎行列がが返り、1の場所のみを記憶するのでメモリ消費を抑えられる。

- SVM
    - liner:データを直線で分類
    - rbf(radial basis function):放射基底関数、直線、曲線で分類可能
    - Cの値：小さくすると柔軟性が持てるが、誤判定が増える。大きくすると、厳密性が出るが、訓練データに過剰適合してしまう

- 主成分分析
    - 教師なし学習に分類されるもの