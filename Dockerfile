# ベースイメージ
FROM python:3.11

# 作業ディレクトリ作成
WORKDIR /app

# 必要ファイルをコピー
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/

# デフォルトコマンド
CMD ["python", "src/main.py"]
