# 記事翻訳ツール

OpenAI APIを使用して英文記事を日本語に翻訳し、要約するツールです。

## セットアップ

### 1. 必要なパッケージのインストール

```bash
pip3 install openai pandas openpyxl python-dotenv
```

### 2. 環境変数の設定

プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下の内容を記入してください：

```bash
# OpenAI API Key
OPENAI_API_KEY=your_actual_openai_api_key_here

# 入力・出力ファイル名
INPUT_FILE=articles.xlsx
OUTPUT_FILE=articles_translated.xlsx
```

**重要**: `.env`ファイルには実際のAPI keyを設定してください。

### 3. 入力ファイルの準備

`articles.xlsx`ファイルをプロジェクトのルートディレクトリに配置し、以下の列を含めてください：

- `本文`: 翻訳対象の英文記事
- `和訳`: 翻訳結果（空欄でOK）
- `要約`: 要約結果（空欄でOK）

## 使用方法

```bash
python3 translate_articles.py
```

## 出力

処理が完了すると、`articles_translated.xlsx`ファイルが生成され、翻訳と要約が追加されます。

## 注意事項

- `.env`ファイルは機密情報を含むため、Gitにコミットされません
- API keyは安全に管理してください
- 処理には時間がかかる場合があります（API制限のため）

## トラブルシューティング

### API keyエラー
```
❌ エラー: OPENAI_API_KEYが設定されていません
```
→ `.env`ファイルに正しいAPI keyを設定してください

### ファイルが見つからない
```
❌ エラー: articles.xlsxが見つかりません
```
→ 入力ファイルが正しい場所にあるか確認してください 