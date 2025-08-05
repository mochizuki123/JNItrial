#!/bin/bash

echo "========================================"
echo "記事翻訳ツール - 実行スクリプト"
echo "========================================"

# スクリプトのディレクトリに移動
cd "$(dirname "$0")"

# Python3が利用可能かチェック
if ! command -v python3 &> /dev/null; then
    echo "❌ エラー: Python3が見つかりません"
    echo "Python3をインストールしてください"
    read -p "Enterキーを押して終了..."
    exit 1
fi

# 必要なファイルの存在確認
if [ ! -f "translate_articles.py" ]; then
    echo "❌ エラー: translate_articles.pyが見つかりません"
    read -p "Enterキーを押して終了..."
    exit 1
fi

if [ ! -f ".env" ]; then
    echo "❌ エラー: .envファイルが見つかりません"
    echo ".envファイルを作成してAPI keyを設定してください"
    read -p "Enterキーを押して終了..."
    exit 1
fi

if [ ! -f "articles.xlsx" ]; then
    echo "❌ エラー: articles.xlsxが見つかりません"
    echo "articles.xlsxファイルを配置してください"
    read -p "Enterキーを押して終了..."
    exit 1
fi

echo "✅ 環境チェック完了"
echo "🚀 翻訳処理を開始します..."
echo

# 翻訳スクリプトを実行
python3 translate_articles.py

# 実行結果の確認
if [ $? -eq 0 ]; then
    echo
    echo "✅ 処理が完了しました"
    echo "📁 結果ファイル: articles_translated.xlsx"
else
    echo
    echo "❌ エラーが発生しました"
fi

read -p "Enterキーを押して終了..." 