# chatgpt-sample
ChatGPTのAPIをお試しで利用するリポジトリ

## プロジェクトインストール

```bash
poetry install
```

## credentialファイル作成

```bash
cp chatgpt_sample/.env.sample chatgpt_sample/.env
```

## プログラム実行

```bash
poetry run python chatgpt_sample/main.py
```

or 

```bash
make main
```

## フォーマット

```bash
make format
```

## テスト実行

```bash
make test
```

## 型チェック

```bash
make type-check
```

## 全てまとめてチェック

```bash
make format test type-check
```
