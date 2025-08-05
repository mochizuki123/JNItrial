@echo off
echo ========================================
echo 記事翻訳ツール - 実行スクリプト
echo ========================================

:: カレントディレクトリに移動
cd /d %~dp0

:: Python3が利用可能かチェック
python3 --version >nul 2>&1
if errorlevel 1 (
    echo ❌ エラー: Python3が見つかりません
    echo Python3をインストールしてください
    pause
    exit /b 1
)

:: 必要なファイルの存在確認
if not exist "translate_articles.py" (
    echo ❌ エラー: translate_articles.pyが見つかりません
    pause
    exit /b 1
)

if not exist ".env" (
    echo ❌ エラー: .envファイルが見つかりません
    echo .envファイルを作成してAPI keyを設定してください
    pause
    exit /b 1
)

if not exist "articles.xlsx" (
    echo ❌ エラー: articles.xlsxが見つかりません
    echo articles.xlsxファイルを配置してください
    pause
    exit /b 1
)

echo ✅ 環境チェック完了
echo 🚀 翻訳処理を開始します...
echo.

:: 翻訳スクリプトを実行
python3 translate_articles.py

:: 実行結果の確認
if errorlevel 1 (
    echo.
    echo ❌ エラーが発生しました
    pause
    exit /b 1
) else (
    echo.
    echo ✅ 処理が完了しました
    echo 📁 結果ファイル: articles_translated.xlsx
)

pause 