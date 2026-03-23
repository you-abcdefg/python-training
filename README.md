# python-training Project


**用途（ユースケース）：**
データ分析や機械学習の入門、または業務データの簡易な可視化・分類モデル作成に役立つサンプルプロジェクトです。

このアプリは「CSV形式の表データ」を入力として、
1. データの統計情報を出力
2. データの分布や関係性をグラフで可視化
3. 機械学習（ランダムフォレスト）による分類モデルを自動で作成・評価
を一括で実行できるPythonプログラムです。

たとえば「input.csv」に数値データを用意し、プログラムを実行するだけで、
・データの基本統計量（平均・標準偏差など）
・ターゲット列（予測したい項目）のヒストグラムや特徴量の散布図
・分類モデルの精度（accuracy）
が自動で出力されます。

初心者でもすぐに試せるよう、仮想環境・Dockerの両方に対応しています。
サンプルとして `data/input.csv` をそのまま使用することで、すぐに動作確認ができます。

---

## 実行方法の選択

* 手軽に試したい方 → **仮想環境（venv）**
   * ローカル環境で簡単に実行できます
* 環境差なく同じ結果を再現したい方 → **Docker**
   * 誰でも同じ環境・同じ結果を再現できます
   * 環境構築が不要で、すぐに実行できます

---

## 入力データ（input.csv）の前提条件

このアプリを正しく動作させるために、入力データには以下の条件があります。

- すべて数値データのCSVファイルを想定しています
- 「target_column」という名前のターゲット列（予測したい項目）を必ず含めてください

---


## 実行結果例

以下は実行時の出力例です。


### 1. データの統計情報出力

```
   feature1  feature2  target_column
count      5.0       5.0            5.0
mean       3.0       4.0            0.4
std        1.58      1.58           0.55
min        1.0       2.0            0.0
max        5.0       6.0            1.0
```

### 2. グラフ表示

- ターゲット列のヒストグラム（matplotlibのウィンドウで表示）
- 特徴量同士の散布図（カスタマイズ可）

### 3. モデルの評価結果

```
Model Accuracy: 0.80
```

---

これらの出力は、input.csvの内容を変更するだけで自動的に更新されます。

---

## 使用技術

- Python 3.11
- pandas
- matplotlib
- numpy
- scikit-learn
- Docker / docker-compose

---

## フォルダ構成

```
python-training/
├── src/
│   ├── main.py
│   ├── utils.py
│   └── mytypes/
│       └── __init__.py
├── data/
│   └── input.csv
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 実行手順

### 仮想環境（venv）での実行

1. プロジェクトディレクトリへ移動  
   `cd python-training`
2. 仮想環境の作成  
   `python -m venv .venv`
3. 仮想環境の有効化（Windows）  
   `.venv\Scripts\activate`
4. 必要なライブラリのインストール  
   `pip install -r requirements.txt`
5. プログラムの実行  
   `python src/main.py`

### Dockerでの実行

1. Docker Desktopをインストール
2. プロジェクトディレクトリでビルド＆実行

   ```
   docker compose up --build
   ```

   または

   ```
   docker build -t pyproj .
   docker run --rm -it -v %cd%\data:/app/data pyproj
   ```

---

## 注意事項

- `data/input.csv` を編集することで、独自データでも簡単に試せます
- コードや構成の改善はプルリクエスト歓迎です

---

## コピペで使えるコマンドまとめ

```sh
cd python-training
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

```sh
docker compose up --build
```
