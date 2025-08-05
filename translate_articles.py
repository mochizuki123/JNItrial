# translate_articles.py
import openai
import pandas as pd
import time

openai.api_key = "YOUR_API_KEY"  # あなたのOpenAIのAPIキーに置き換えてください

# ファイル名はアナリストが指定したExcel
input_file = "articles.xlsx"
output_file = "articles_translated.xlsx"

# Excel読み込み
df = pd.read_excel(input_file)

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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        result = response['choices'][0]['message']['content']
        translation = result.split("翻訳:")[1].split("要約:")[0].strip()
        summary = result.split("要約:")[1].strip()
        return translation, summary
    except Exception as e:
        print(f"Error: {e}")
        return "", ""

# 実行処理
for idx, row in df.iterrows():
    if pd.isna(row['本文']):
        continue
    if not pd.isna(row.get('和訳')) and not pd.isna(row.get('要約')):
        continue  # 既に処理済みならスキップ

    translation, summary = translate_and_summarize(row['本文'])
    df.at[idx, '和訳'] = translation
    df.at[idx, '要約'] = summary
    time.sleep(2)

df.to_excel(output_file, index=False)
print("✅ 翻訳・要約完了！")
