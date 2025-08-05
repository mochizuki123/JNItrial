# translate_articles.py
import openai
import pandas as pd
import time
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# 環境変数からAPI keyを取得
api_key = os.getenv("OPENAI_API_KEY")

# ファイル名は環境変数から取得（デフォルト値付き）
input_file = os.getenv("INPUT_FILE", "articles.xlsx")
output_file = os.getenv("OUTPUT_FILE", "articles_translated.xlsx")

# API keyが設定されているかチェック
if not api_key or api_key == "your_openai_api_key_here":
    print("❌ エラー: OPENAI_API_KEYが設定されていません")
    print("1. .envファイルを作成してください")
    print("2. OPENAI_API_KEY=your_actual_api_key を設定してください")
    exit(1)

# OpenAIクライアントを初期化
client = openai.OpenAI(api_key=api_key)

# Excel読み込み（2行目をヘッダーとして読み込み）
try:
    df = pd.read_excel(input_file, header=1)
    print(f"✅ {input_file}を読み込みました")
    print(f"📊 列名: {list(df.columns)}")
    print(f"📊 データ行数: {len(df)}")
except FileNotFoundError:
    print(f"❌ エラー: {input_file}が見つかりません")
    exit(1)
except Exception as e:
    print(f"❌ エラー: Excelファイルの読み込みに失敗しました - {e}")
    exit(1)

def translate_and_summarize(text):
    prompt = f"""
    以下の英文を日本語に翻訳し、その内容を100文字程度で日本語で要約してください。
    
    英文:
    {text}
    
    出力形式:
    翻訳: ○○○
    要約: ○○○
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        result = response.choices[0].message.content
        translation = result.split("翻訳:")[1].split("要約:")[0].strip()
        summary = result.split("要約:")[1].strip()
        return translation, summary
    except Exception as e:
        print(f"Error: {e}")
        return "", ""

# 実行処理
print("🚀 翻訳・要約処理を開始します...")
processed_count = 0

for idx, row in df.iterrows():
    if pd.isna(row['本文']):
        continue
    if not pd.isna(row.get('和訳')) and not pd.isna(row.get('要約')):
        continue  # 既に処理済みならスキップ

    print(f"📝 処理中: {idx + 1}/{len(df)}")
    translation, summary = translate_and_summarize(row['本文'])
    df.at[idx, '和訳'] = translation
    df.at[idx, '要約'] = summary
    processed_count += 1
    time.sleep(2)

df.to_excel(output_file, index=False)
print(f"✅ 翻訳・要約完了！ {processed_count}件を処理しました")
print(f"📁 結果は {output_file} に保存されました")
