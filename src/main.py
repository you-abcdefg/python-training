
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import openpyxl
import os

# データの読み込み
def load_data(file_path):
    return pd.read_csv(file_path)

# データの前処理
def preprocess_data(df):
    df.fillna(0, inplace=True)
    return df

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

def visualize_data(df, base_dir):
    # Docker環境では/app/screenshots、ローカルでは../screenshots
    docker_screenshots = '/app/screenshots'
    local_screenshots = os.path.join(base_dir, '../screenshots')
    screenshots_dir = docker_screenshots if os.path.exists(docker_screenshots) else local_screenshots
    os.makedirs(screenshots_dir, exist_ok=True)
    # ヒストグラム
    plt.figure(figsize=(10, 6))
    plt.hist(df['target_column'], bins=30, alpha=0.7)
    plt.title('Target Column Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    hist_path = os.path.join(screenshots_dir, 'histogram.png')
    plt.savefig(hist_path)
    plt.close()
    # 散布図（特徴量が2つ以上ある場合のみ）
    features = [col for col in df.columns if col != 'target_column']
    if len(features) >= 2:
        plt.figure(figsize=(8, 6))
        plt.scatter(df[features[0]], df[features[1]], c=df['target_column'], cmap='viridis', alpha=0.7)
        plt.title('Feature Scatter Plot')
        plt.xlabel(features[0])
        plt.ylabel(features[1])
        scatter_path = os.path.join(screenshots_dir, 'scatter.png')
        plt.savefig(scatter_path)
        plt.close()

def main():
    # スクリプトのディレクトリを基準に相対パスを解決
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '../data/input.csv')
    data = load_data(csv_path)
    processed_data = preprocess_data(data)
    X = processed_data.drop('target_column', axis=1)
    y = processed_data['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f'Model Accuracy: {accuracy:.2f}')
    visualize_data(processed_data, base_dir)

if __name__ == '__main__':
    main()
